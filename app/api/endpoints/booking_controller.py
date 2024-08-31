from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from common.models.user import User
from common.repository.booking_repository import BookingRepository
from common.dto.booking_dto import BookingDTO, BookingDTOAdd, BookingDTOUpdate
from api.deps import get_current_user

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
    

    @router.post("/")
    async def add_booking(self, data: BookingDTOAdd) -> BookingDTO:
        converted_data = data.to_dict()
        result = await BookingRepository.add(**converted_data)
        return result
    

    @router.patch("/{instance_id}")
    async def update_booking(self, data: BookingDTOUpdate, instance_id: int):
        converted_data = data.to_dict()
        await BookingRepository.update(instance_id=instance_id, **converted_data)
        return 'UPDATED'
    

    @router.delete("/{instance_id}")
    async def delete_booking(seld, instance_id: int):
        await BookingRepository.delete(instance_id=instance_id)
        return 'DELETED'