from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from app.common.models.user import User
from app.common.repository.booking_repository import BookingRepository
from app.common.dto.booking_dto import BookingDTO, BookingDTOAdd, BookingDTOUpdate
from app.api.deps import get_current_user

from app.core.exceptions import RoomCannotBeBookedException, BookingDeleteException

router = APIRouter()

@cbv(router)
class BookingAPI:

    @router.get("/all")
    async def get_all(self) -> list[BookingDTO]:
        result = await BookingRepository.get_all()
        return result
    

    @router.get("/list")
    async def get_all_by_user(self, user: User = Depends(get_current_user)) -> list[BookingDTO]:
        result = await BookingRepository.get_by_user(user_id=user.id)
        return result


    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> BookingDTO:
        result = await BookingRepository.get_by_id(instance_id=instance_id)
        return result
    

    @router.post("/{room_id}")
    async def add_booking(self, data: BookingDTOAdd, room_id: int, user: User = Depends(get_current_user)) -> BookingDTO | dict:
        booking = await BookingRepository.add(room_id=room_id, user_id=user.id, data=data)
        if not booking:
            raise RoomCannotBeBookedException
        else:
            return booking
    

    @router.delete("/{instance_id}")
    async def delete_booking(seld, instance_id: int, user: User = Depends(get_current_user)) -> BookingDTO | None:
        booking = await BookingRepository.delete(instance_id=instance_id, user_id=user.id)
        if not booking:
            raise BookingDeleteException
        else:
            return booking