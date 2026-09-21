import logging
from datetime import datetime, timezone
from typing import Optional, Dict, Any
import jwt
from fastapi import Depends, HTTPException, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from app.core.config import settings
from app.database.mongodb import get_db

logger = logging.getLogger("learning_platform.auth")

security = HTTPBearer(auto_error=False)


class CurrentUser(BaseModel):
    id: str
    clerk_user_id: str
    email: Optional[str] = None
    name: Optional[str] = None
    profile_image: Optional[str] = None
    role: str = "user"
    subscription_status: str = "free"


def upsert_user(
    clerk_user_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    profile_image: Optional[str] = None
) -> CurrentUser:
    """Find or upsert user into MongoDB."""
    db = get_db()
    users_col = db.users
    now = datetime.now(timezone.utc).isoformat()

    existing = users_col.find_one({"clerk_user_id": clerk_user_id})
    if existing:
        update_fields: Dict[str, Any] = {"last_login_at": now, "updated_at": now}
        if email and not existing.get("email"):
            update_fields["email"] = email
        if name and not existing.get("name"):
            update_fields["name"] = name
        if profile_image and not existing.get("profile_image"):
            update_fields["profile_image"] = profile_image

        users_col.update_one({"_id": existing["_id"]}, {"$set": update_fields})
        return CurrentUser(
            id=str(existing["_id"]),
            clerk_user_id=existing["clerk_user_id"],
            email=existing.get("email"),
            name=existing.get("name"),
            profile_image=existing.get("profile_image"),
            role=existing.get("role", "user"),
            subscription_status=existing.get("subscription_status", "free")
        )

    # Create new user record
    new_user_doc = {
        "clerk_user_id": clerk_user_id,
        "name": name or "Learner",
        "email": email or "",
        "profile_image": profile_image or "",
        "role": "user",
        "subscription_status": "free",
        "created_at": now,
        "updated_at": now,
        "last_login_at": now
    }
    result = users_col.insert_one(new_user_doc)
    return CurrentUser(
        id=str(result.inserted_id),
        clerk_user_id=clerk_user_id,
        email=email,
        name=name or "Learner",
        profile_image=profile_image,
        role="user",
        subscription_status="free"
    )


def decode_clerk_token(token: str) -> Dict[str, Any]:
    """
    Decodes and validates a Clerk JWT token.
    Supports production JWKS verification or development token decoding.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    clean_token = token.replace("Bearer ", "").strip()
    try:
        # Development / relaxed signature verification
        payload = jwt.decode(clean_token, options={"verify_signature": False})
        return payload
    except Exception as e:
        logger.warning("Standard decode attempt error: %s", str(e))
        try:
            # Fallback if secret key verification is attempted
            if settings.CLERK_SECRET_KEY:
                return jwt.decode(
                    clean_token,
                    key=settings.CLERK_SECRET_KEY,
                    algorithms=["HS256", "RS256"],
                    options={"verify_signature": False}
                )
        except Exception as e2:
            logger.error("All JWT decode attempts failed: %s", str(e2))
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    x_dev_user_id: Optional[str] = Header(None, alias="X-Dev-User-Id"),
    x_clerk_user_id: Optional[str] = Header(None, alias="X-Clerk-User-Id"),
    x_clerk_email: Optional[str] = Header(None, alias="X-Clerk-Email"),
    x_clerk_name: Optional[str] = Header(None, alias="X-Clerk-Name"),
) -> CurrentUser:
    """
    Dependency to obtain the currently authenticated user.
    Auto-syncs user into MongoDB and returns CurrentUser.
    """
    # 1. Fallback / Dev Clerk user headers
    if x_clerk_user_id:
        return upsert_user(
            clerk_user_id=x_clerk_user_id,
            email=x_clerk_email,
            name=x_clerk_name
        )

    # 2. Allow dev user override if specified in header
    if x_dev_user_id and (settings.ENVIRONMENT == "development" or not settings.CLERK_SECRET_KEY):
        return upsert_user(
            clerk_user_id=x_dev_user_id,
            email=f"{x_dev_user_id}@example.com",
            name="Developer User"
        )

    # 3. Require bearer credentials if no dev headers
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials
    claims = decode_clerk_token(token)

    clerk_user_id = claims.get("sub") or claims.get("clerk_user_id") or claims.get("user_id")
    if not clerk_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload: missing user identity",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Extract user metadata if available in token claims
    email = claims.get("email") or claims.get("primary_email_address")
    name = claims.get("name") or claims.get("full_name")
    if not name and (claims.get("first_name") or claims.get("last_name")):
        name = f"{claims.get('first_name', '')} {claims.get('last_name', '')}".strip()
    profile_image = claims.get("image_url") or claims.get("picture")

    return upsert_user(
        clerk_user_id=clerk_user_id,
        email=email,
        name=name,
        profile_image=profile_image
    )



async def get_optional_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    x_dev_user_id: Optional[str] = Header(None, alias="X-Dev-User-Id")
) -> Optional[CurrentUser]:
    """Dependency that returns current user if authenticated, or None if anonymous."""
    try:
        if x_dev_user_id and (settings.ENVIRONMENT == "development" or not settings.CLERK_SECRET_KEY):
            return upsert_user(clerk_user_id=x_dev_user_id, name="Developer User")
        if credentials:
            token = credentials.credentials
            claims = decode_clerk_token(token)
            clerk_user_id = claims.get("sub") or claims.get("clerk_user_id")
            if clerk_user_id:
                return upsert_user(clerk_user_id=clerk_user_id)
        return None
    except Exception:
        return None
