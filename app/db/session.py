from sqlalchemy.ext.asyncio import create_async_engine, create_async_engine, async_sessionmaker, AsyncSession
import asyncio

from core.config import settings

engine = create_async_engine(
    settings.POSTGRES_DATABASE_URI, pool_pre_ping=True
)

async_session_maker = async_sessionmaker(
        bind=engine, 
        expire_on_commit=False, 
        autoflush=False,
        pool_pre_ping=True
    )

class DataBaseSession:
    def __init__(self) -> None:
        self.db = None

    async def __aenter__(self) -> AsyncSession:
        self.db = async_session_maker()
        return self.db

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.db.close()

async def get_session():
    async with DataBaseSession() as session:
        return session