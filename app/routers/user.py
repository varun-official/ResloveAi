from fastapi import APIRouter
from app.models.user_model import UserModel, UpdateUserModel, CreateUserModel
from app.service.user import create_user, get_user_by_email, update_user, list_users, delete_user
from typing import Optional
from pydantic import EmailStr
router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/")
async def get_all_user(page: int = 1, page_size: int = 100, tag_filter: Optional[str] = None):
    all_user = await list_users(page, page_size, filter={"skills": tag_filter} if tag_filter else {})
    return all_user

@router.post("/")
async def add_user(user_data: CreateUserModel):
    user = await create_user(user_data)
    return user

@router.get("/{email}")
async def get_user(email: str):
    user = await get_user_by_email(email)
    if user:
        return user
    return {"error": "User not found"}

@router.put("/")
async def modify_user(update_data: UpdateUserModel):
    user = await update_user(update_data.email, update_data)
    if user:
        return user
    return {"error": "User not found"}

@router.delete("/{email}")
async def remove_user(email: str):
    success = await delete_user(email)
    if success:
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}


    
