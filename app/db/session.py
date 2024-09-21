from sqlalchemy.ext.asyncio import create_async_engine, create_async_engine, async_sessionmaker
import asyncio
from sqlalchemy import NullPool


from app.core.config import settings

DATABASE_PARAMS = {"poolclass": NullPool}
engine_nullpool = create_async_engine(settings.POSTGRES_DATABASE_URI, **DATABASE_PARAMS)
async_session_maker_nullpool = async_sessionmaker(engine_nullpool, expire_on_commit=False)


async_engine = create_async_engine(
    settings.POSTGRES_DATABASE_URI, pool_pre_ping=True
)

async_session_maker = async_sessionmaker(
        bind=async_engine, 
        expire_on_commit=False, 
        autoflush=False,
    )