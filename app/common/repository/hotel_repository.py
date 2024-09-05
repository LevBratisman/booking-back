from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, join, and_, or_

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.models.hotel import Hotel
from app.common.models.booking import Booking
from app.common.models.room import Room

from app.common.dto.base import TermDTO
from app.common.dto.hotel_dto import HotelWithLeftRoomsDTO

from app.db.session import async_session_maker


class HotelRepository(CRUDBaseRepository):
    model = Hotel
    
    @classmethod
    async def get_by_location(cls, location: str, term_data: TermDTO) -> list[HotelWithLeftRoomsDTO]:
        async with async_session_maker() as session:
            get_count_free_rooms = select(Hotel, func.count().label('count_of_rooms')
                ).join(Room).join(Booking).where(
                and_(
                    Booking.room_id==Room.id,
                    # or_(
                    #     and_(
                    #         Booking.date_to >= term_data.date_from,
                    #         Booking.date_to <= term_data.date_to
                    #     ),
                    #     and_(
                    #         Booking.date_from >= term_data.date_from,
                    #         Booking.date_from <= term_data.date_to
                    #     ),
                    #     and_(
                    #         Booking.date_from <= term_data.date_from,
                    #         Booking.date_to >= term_data.date_to
                    #     )
                    # )
                )
            )

            result = await session.execute(get_count_free_rooms)
            print(result.mappings().all())
            


    @classmethod
    async def get_rooms_by_hotel(cls, instance_id: int, term_data: TermDTO):
        async with async_session_maker() as session:
            pass


