from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.auth import get_current_user, get_optional_current_user, CurrentUser, upsert_user
from app.schemas.user import UserResponse, UserSyncRequest
from app.database.mongodb import get_db

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: CurrentUser = Depends(get_current_user)):
    """
    Get the currently authenticated user's profile.
    Auto-syncs Clerk identity with MongoDB user records.
    """
    db = get_db()
    user_doc = db.users.find_one({"clerk_user_id": current_user.clerk_user_id})
    if user_doc:
        return UserResponse(
            _id=str(user_doc["_id"]),
            clerk_user_id=user_doc["clerk_user_id"],
            email=user_doc.get("email"),
            name=user_doc.get("name"),
            profile_image=user_doc.get("profile_image"),
            role=user_doc.get("role", "user"),
            subscription_status=user_doc.get("subscription_status", "free"),
            created_at=user_doc.get("created_at"),
            updated_at=user_doc.get("updated_at"),
            last_login_at=user_doc.get("last_login_at"),
        )
    return UserResponse(
        _id=current_user.id,
        clerk_user_id=current_user.clerk_user_id,
        email=current_user.email,
        name=current_user.name,
        profile_image=current_user.profile_image,
        role=current_user.role,
        subscription_status=current_user.subscription_status,
    )


@router.post("/sync", response_model=UserResponse)
async def sync_user(
    payload: UserSyncRequest,
    current_user: Optional[CurrentUser] = Depends(get_optional_current_user),
):
    """
    Sync Clerk user identity into MongoDB.
    Creates or updates the MongoDB user record with full name, email, and avatar.
    """
    user_id = (current_user.clerk_user_id if current_user else None) or payload.clerk_user_id
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing clerk_user_id for synchronization",
        )

    email = payload.email or (current_user.email if current_user else None)
    name = payload.name or (current_user.name if current_user else None)
    profile_image = payload.profile_image or (current_user.profile_image if current_user else None)

    user = upsert_user(
        clerk_user_id=user_id,
        email=email,
        name=name,
        profile_image=profile_image,
    )

    db = get_db()
    user_doc = db.users.find_one({"clerk_user_id": user.clerk_user_id})
    return UserResponse(
        _id=str(user_doc["_id"]) if user_doc else user.id,
        clerk_user_id=user.clerk_user_id,
        email=user_doc.get("email") if user_doc else user.email,
        name=user_doc.get("name") if user_doc else user.name,
        profile_image=user_doc.get("profile_image") if user_doc else user.profile_image,
        role=user_doc.get("role", "user") if user_doc else user.role,
        subscription_status=user_doc.get("subscription_status", "free") if user_doc else user.subscription_status,
        created_at=user_doc.get("created_at") if user_doc else None,
        updated_at=user_doc.get("updated_at") if user_doc else None,
        last_login_at=user_doc.get("last_login_at") if user_doc else None,
    )

