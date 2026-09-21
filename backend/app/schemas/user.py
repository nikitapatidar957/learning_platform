from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    clerk_user_id: str
    email: Optional[str] = None
    name: Optional[str] = None
    profile_image: Optional[str] = None
    role: str = "user"
    subscription_status: str = "free"


class UserResponse(UserBase):
    id: str = Field(alias="_id", default="")
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    last_login_at: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class UserSyncRequest(BaseModel):
    clerk_user_id: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    profile_image: Optional[str] = None

