from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.crud_base_repository import CRUDBaseRepository
from common.models.room import Room


class RoomRepository(CRUDBaseRepository):
    model = Room