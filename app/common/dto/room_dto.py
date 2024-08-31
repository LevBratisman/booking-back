from common.dto.base import IdBase, BaseDTO


class Room(BaseDTO):
    hotel_id: int
    name: str
    price: int
    quantity: int
    description: str | None = None
    services: list[str] | None = None
    image_id: int | None = None



class RoomDTOAdd(Room):
    pass


class RoomDTOUpdate(Room, IdBase):
    pass


class RoomDTO(RoomDTOUpdate):
    pass
