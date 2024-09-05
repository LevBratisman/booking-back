from datetime import date

from app.common.dto.base import IdBase, UserDependsBase, BaseDTO


class Booking(UserDependsBase):
    room_id: int
    date_from: date
    date_to: date
    price: int


class BookingDTOAdd(BaseDTO):
    date_from: date
    date_to: date


class BookingDTOUpdate(Booking):
    pass


class BookingDTO(BookingDTOUpdate, IdBase):
    pass
