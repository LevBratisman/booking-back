from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_, insert, delete

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.models.booking import Booking
from app.common.dto.booking_dto import BookingDTOAdd, BookingDTO
from app.db.session import async_session_maker

from app.common.repository.room_repository import RoomRepository


class BookingRepository(CRUDBaseRepository):
    model = Booking

    @classmethod
    async def add(cls, room_id: int, user_id: int, data: BookingDTOAdd) -> BookingDTO:
        async with async_session_maker() as session:
            target_room = await RoomRepository.get_by_id(instance_id=room_id)

            get_bookings_query = select(cls.model).where(
                and_ (
                    cls.model.room_id == room_id,
                    or_(
                        and_(
                            cls.model.date_to >= data.date_from,
                            cls.model.date_to <= data.date_to
                        ),
                        and_(
                            cls.model.date_from >= data.date_from,
                            cls.model.date_from <= data.date_to
                        ),
                        and_(
                            cls.model.date_from <= data.date_from,
                            cls.model.date_to >= data.date_to
                        )
                    )
                )
            )

            bookings = await session.execute(get_bookings_query)
            bookings_scalars = bookings.scalars().all()

            free_rooms_count = target_room.quantity - len(bookings_scalars)
            if free_rooms_count > 0:
                result = await session.execute(
                          insert(cls.model).values(
                            room_id=room_id,
                            user_id=user_id, 
                            price=target_room.price, 
                            date_from=data.date_from,
                            date_to=data.date_to
                            ).returning(cls.model)
                        )
                
                await session.commit()

                return result.scalar()
            else:
                return None
            

    @classmethod
    async def delete(cls, instance_id: int, user_id: int) -> BookingDTO:
        async with async_session_maker() as session:
            get_target_booking = select(cls.model).where(cls.model.id==instance_id)
            target_booking = await session.execute(get_target_booking)

            target_booking_scalar = target_booking.scalar_one_or_none()

            if target_booking_scalar:

                if target_booking_scalar.user_id == user_id:
                    await session.execute(
                        delete(cls.model).where(cls.model.id==instance_id).returning(cls.model)
                    )
                    await session.commit()
                    
                    return target_booking_scalar
                else:
                    return None
            else:
                return None

            

            
