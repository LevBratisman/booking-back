from datetime import date

from common.dto.base import IdBase, UserDependsBase, BaseDTO


class Booking(UserDependsBase):
    room_id: int
    date_from: date
    date_to: date
    price: int


class BookingDTOAdd(Booking):
    pass


class BookingDTOUpdate(Booking):
    pass


class BookingDTO(BookingDTOUpdate, IdBase):
    pass
