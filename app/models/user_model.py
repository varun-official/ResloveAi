from beanie import Document, before_event, Insert, Update, Save, Replace
from pydantic import Field, EmailStr, BaseModel
from datetime import datetime, timezone


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
    full_name: str | None = None
    user_type: str | None = None  # Can be "user" or "admin"
    skills: list[str] | None = None