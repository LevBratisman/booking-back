from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, or_

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.models.hotel import Hotel
from app.common.models.booking import Booking
from app.common.models.room import Room
from app.common.dto.room_dto import RoomWithLeftRoomsDTO

from app.common.dto.base import TermDTO
from app.common.dto.hotel_dto import HotelDTO, HotelWithLeftRoomsDTO

from app.db.session import async_session_maker


class HotelRepository(CRUDBaseRepository):
    model = Hotel
    
    @classmethod
    async def get_by_location(cls, location: str, term_data: TermDTO) -> list[HotelWithLeftRoomsDTO]:
        async with async_session_maker() as session:
            get_rooms_left = select(Hotel.__table__.columns, (Hotel.rooms_quantity - func.count(Booking.id)).label('rooms_left')
                ).select_from(Hotel
                ).outerjoin(Room, Hotel.id == Room.hotel_id
                ).outerjoin(
                    Booking,
                    and_(
                        Booking.room_id == Room.id,
                        or_(
                            and_(
                                Booking.date_to >= term_data.date_from,
                                Booking.date_to <= term_data.date_to
                            ),
                            and_(
                                Booking.date_from >= term_data.date_from,
                                Booking.date_from <= term_data.date_to
                            ),
                            and_(
                                Booking.date_from <= term_data.date_from,
                                Booking.date_to >= term_data.date_to
                            )
                        )
                    )
                ).where(
                    Hotel.location.like(f"%{location}%")
                ).group_by(Hotel.id)

            result = await session.execute(get_rooms_left)

            return result.mappings().all()
            


    @classmethod
    async def get_rooms_by_hotel(cls, instance_id: int, term_data: TermDTO) -> list[RoomWithLeftRoomsDTO]:
        async with async_session_maker() as session:
            get_rooms_left = select(Room.__table__.columns, (Room.quantity - func.count(Booking.id)).label('rooms_left')
                ).select_from(Room
                ).outerjoin(
                Booking,
                and_(
                    Booking.room_id == Room.id,
                    or_(
                        and_(
                            Booking.date_to >= term_data.date_from,
                            Booking.date_to <= term_data.date_to
                        ),
                        and_(
                            Booking.date_from >= term_data.date_from,
                            Booking.date_from <= term_data.date_to
                        ),
                        and_(
                            Booking.date_from <= term_data.date_from,
                            Booking.date_to >= term_data.date_to
                        )
                    )
                )
            ).where(
                Room.hotel_id == instance_id
            ).group_by(Room.id)

            result = await session.execute(get_rooms_left)

            return result.mappings().all()


