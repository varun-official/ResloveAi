
from fastapi import FastAPI
from app.routers import user
from app.config.database import init_db
import asyncio

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI app!"}
