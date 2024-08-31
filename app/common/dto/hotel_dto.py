from common.dto.base import IdBase, BaseDTO


class Hotel(BaseDTO):
    name: str
    location: str
    rooms_quantity: int
    services: list[str] | None = None
    image_id: int | None = None



class HotelDTOAdd(Hotel):
    pass


class HotelDTOUpdate(Hotel):
    pass


class HotelDTO(HotelDTOUpdate, IdBase):
    pass

