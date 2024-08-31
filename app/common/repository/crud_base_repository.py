from abc import ABC, abstractmethod
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from db.base_class import ModelType
from db.session import get_session


class AbstractRepository(ABC):
    """
    Interface for all repositories
    """
    @abstractmethod
    async def add():
        raise NotImplementedError

    @abstractmethod
    async def get_one():
        raise NotImplementedError

    @abstractmethod
    async def get_by_id():
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_user():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError

    @abstractmethod
    async def delete():
        raise NotImplementedError



class CRUDBaseRepository(AbstractRepository):
    model: ModelType = None


    @classmethod
    async def get_one(cls, **filters) -> ModelType:
        session: AsyncSession = await get_session()
        query = select(cls.model).filter_by(**filters)
        result = await session.execute(query)

        return result.scalar_one_or_none()


    @classmethod
    async def get_by_id(cls, *, instance_id: int) -> ModelType:
        session: AsyncSession = await get_session()
        query = select(cls.model).where(cls.model.id == instance_id)
        result = await session.execute(query)

        return result.scalar_one_or_none()
    

    @classmethod
    async def get_by_user(cls, **filters) -> list[ModelType]:
        pass


    @classmethod
    async def get_all(cls, **filters) -> list[ModelType]:
        session: AsyncSession = await get_session()
        query = select(cls.model).filter_by(**filters)
        result = await session.execute(query)

        return result.scalars().all()
    

    @classmethod
    async def add(cls, **data):
        session: AsyncSession = await get_session()
        query = insert(cls.model).values(**data)
        await session.execute(query)
        await session.commit()
        

    @classmethod
    async def update(cls):
        pass


    @classmethod
    async def delete(cls):
        pass