from sqlalchemy.ext.asyncio import create_async_engine, create_async_engine, async_sessionmaker, AsyncSession
import asyncio

from app.core.config import settings

engine = create_async_engine(
    settings.POSTGRES_DATABASE_URI, pool_pre_ping=True
)

async_session_maker = async_sessionmaker(
        bind=engine, 
        expire_on_commit=False, 
        autoflush=False,
    )