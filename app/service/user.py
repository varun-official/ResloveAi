from app.models.user_model import UserModel
from typing import Optional, List,Dict,Any

async def create_user(user_data: Dict[str, Any]) -> UserModel:
    if not isinstance(user_data, dict):
        user_data = user_data.dict()
    user = UserModel(**user_data)
    await user.insert()
    return user

async def get_user_by_email(email: str) -> Optional[UserModel]:
    user = await UserModel.find_one(UserModel.email == email)
    return user

async def update_user(email: str, update_data: Dict[str, Any]) -> Optional[UserModel]:
    user = await get_user_by_email(email)
    if user:
        for key, value in update_data.items():
            setattr(user, key, value)
        await user.save()
        return user
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