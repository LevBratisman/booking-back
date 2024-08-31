from sqlalchemy.ext.asyncio import AsyncSession
from common.dto.hotel_dto import HotelDTO
from common.models.hotel import Hotel
from common.repository.hotel_repository import HotelRepository
from common.service.base_service import BaseService


class HotelService(BaseService):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            session=session,
            repository=HotelRepository,
            model=Hotel,
            model_dto=HotelDTO
        )