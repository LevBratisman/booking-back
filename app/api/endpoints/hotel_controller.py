from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from common.repository.hotel_repository import HotelRepository
from common.dto.hotel_dto import HotelDTO, HotelDTOAdd, HotelDTOUpdate

router = APIRouter()

@cbv(router)
class HotelAPI:

    @router.get("/list")
    async def get_all(self) -> list[HotelDTO]:
        result = await HotelRepository.get_all()
        return result


    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> HotelDTO:
        result = await HotelRepository.get_by_id(instance_id=instance_id)
        return result
    

    @router.post("/")
    async def add_hotel(self, data: HotelDTOAdd) -> HotelDTO:
        converted_data = data.to_dict()
        result = await HotelRepository.add(**converted_data)
        return result
    

    @router.patch("/{instance_id}")
    async def update_hotel(self, data: HotelDTOUpdate, instance_id: int):
        converted_data = data.to_dict()
        await HotelRepository.update(instance_id=instance_id, **converted_data)
        return 'UPDATED'
    

    @router.delete("/{instance_id}")
    async def delete_hotel(seld, instance_id: int):
        await HotelRepository.delete(instance_id=instance_id)
        return 'DELETED'