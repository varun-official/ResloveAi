from app.models.user_model import UserModel, UpdateUserModel
from typing import Optional, List,Dict,Any
from beanie.operators import Set
from pydantic import EmailStr

async def create_user(user_data: Dict[str, Any]) -> UserModel:
    if not isinstance(user_data, dict):
        user_data = user_data.dict()
    user = UserModel(**user_data)
    await user.insert()
    return user

async def get_user_by_email(email: str) -> Optional[UserModel]:
    user = await UserModel.find_one(UserModel.email == email)
    return user

async def update_user(email: EmailStr, update_data: UpdateUserModel) -> Optional[UserModel]:
    try:
        update_dict = update_data.dict(exclude_unset=True, exclude_none=True)
        if not update_dict:
            return None  # nothing to update

        user = await UserModel.find_one(UserModel.email == email)
        if not user:
            return None

        await user.update(Set(update_dict))

        # return the fresh updated document
        return await UserModel.get(user.id)
    except Exception as e:
        print(f"Error updating user: {e}")
        return None

async def list_users(page:int,page_size:int,filter:dict) -> List[UserModel]:
    page = max(page, 1)
    page_size = min(max(page_size, 1), 100)
    skip = (page - 1) * page_size
    query = get_user_filter_query(filter)
    users = await UserModel.find(query).skip(skip).limit(page_size).to_list()
    return users

async def delete_user(email: str) -> bool:
    user = await get_user_by_email(email)
    if user:
        await user.delete()
        return True
    return False

def get_user_filter_query(filter: Dict[str, Any]) -> Dict[str, Any]:
    array_fields = ['skills']
    or_clauses = []
    for field in array_fields:
        if field in filter and isinstance(filter[field], str):
            for item in filter[field].split(','):
                item = item.strip()
                if item:
                    or_clauses.append({field: {"$regex": item, "$options": "i"}})
    if or_clauses:
        return {"$or": or_clauses}
    return {}