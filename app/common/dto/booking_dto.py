from datetime import date

from common.dto.base import IdBase, UserDependsBase, BaseDTO


class Booking(BaseDTO, UserDependsBase):
    room_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


class BookingDTOAdd(Booking):
    pass


class BookingDTOUpdate(Booking, IdBase):
    pass


class BookingDTO(BookingDTOUpdate):
    pass
