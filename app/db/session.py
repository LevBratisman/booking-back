from sqlalchemy.ext.asyncio import create_async_engine, create_async_engine, async_sessionmaker

from core.config import settings

engine = create_async_engine(
    settings.POSTGRES_DATABASE_URI, pool_pre_ping=True
)

async def get_session():
    async_session_maker = async_sessionmaker(
        bind=engine, 
        expire_on_commit=False, 
        autoflush=False
    )

    async with async_session_maker() as session:
        return session