from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from common.repository.hotel_repository import HotelRepository
from common.dto.hotel_dto import HotelDTO, HotelDTOAdd

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
    async def add_hotel(self, data: HotelDTOAdd):
        await HotelRepository.add(**data.to_dict())
        return 'CREATED'