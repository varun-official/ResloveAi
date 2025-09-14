from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import UserModel
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "")
DB_NAME = os.getenv("DB_NAME", "resloveai_db")
async def init_db():
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[DB_NAME]
    await init_beanie(database=db, document_models=[UserModel])
