from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.crud_base_repository import CRUDBaseRepository
from common.models.hotel import Hotel


class HotelRepository(CRUDBaseRepository):
    model = Hotel
