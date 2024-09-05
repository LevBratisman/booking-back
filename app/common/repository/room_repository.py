from sqlalchemy.ext.asyncio import AsyncSession

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.models.room import Room


class RoomRepository(CRUDBaseRepository):
    model = Room

    @classmethod
    async def get_rooms_left():
        pass