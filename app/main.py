#khởi động FastAPI.
from fastapi import FastAPI
from app.routers import items
from app.dependencies import init_db

app = FastAPI()

app.include_router(items.router)

# @app.on_event("startup")
# async def startup_event():
#     await init_db()