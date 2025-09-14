from beanie import Document, before_event, Insert, Update, Save, Replace
from pydantic import Field, EmailStr, BaseModel
from datetime import datetime, timezone
from typing import Optional


class UserModel(Document):
    email: EmailStr
    full_name: str
    user_type: str = "user"  # Default type is "user"
    skills: list[str] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @before_event([Insert, Save, Replace, Update])
    def update_timestamp(self):
        self.updated_at = datetime.now(timezone.utc)

    class Settings:
        name = "users"  # Collection name in MongoDB

class CreateUserModel(BaseModel):
    email: EmailStr
    full_name: str
    user_type: str = "user"  # Can be "user" or "admin"
    skills: list[str] = []

class UpdateUserModel(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    user_type: Optional[str] = None
    skills: Optional[list[str]] = None
