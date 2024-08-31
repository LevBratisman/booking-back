from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.crud_base_repository import CRUDBaseRepository
from common.models.booking import Booking


class BookingRepository(CRUDBaseRepository):
    model = Booking