from sqlalchemy.ext.asyncio import AsyncSession

from app.common.dto.hotel_dto import HotelDTO
from app.common.models.hotel import Hotel
from app.common.repository.hotel_repository import HotelRepository
from app.common.service.base_service import BaseService


class HotelService(BaseService):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            session=session,
            repository=HotelRepository,
            model=Hotel,
            model_dto=HotelDTO
        )