#Quản lý các dependencies của ứng dụng
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

DATABASE_URL = "postgresql+asyncpg://postgres:manhlan@127.0.0.1:5432/secondCRUD"
# DATABASE_URL = "postgresql+asyncpg://postgres:manhlan@db:5432/secondCRUD"
# DATABASE_URL = "postgresql+asyncpg://postgres:manhlan@localhost:5432/secondCRUD"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    from app.models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)