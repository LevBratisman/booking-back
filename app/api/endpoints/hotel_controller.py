import asyncio
from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from fastapi_cache.decorator import cache
from datetime import date


from app.common.repository.hotel_repository import HotelRepository
from app.common.dto.hotel_dto import HotelDTO, HotelDTOAdd, HotelDTOUpdate, HotelWithLeftRoomsDTO, HotelFiltersDTO
from app.common.dto.base import TermDTO

from app.common.dto.room_dto import RoomWithLeftRoomsDTO

router = APIRouter()

@cbv(router)
class HotelAPI:
    
    @router.get("/{location}")
    @cache(expire=20)
    async def get_hotels_by_location(
        self, 
        location: str,
        date_from: date, 
        date_to: date
    ) -> list[HotelWithLeftRoomsDTO]:
        hotels = await HotelRepository.get_by_location(location=location, date_from=date_from, date_to=date_to)
        return hotels


    @router.post("/{instance_id}/rooms")
    async def get_rooms_by_hotel(self, term_data: TermDTO, instance_id: int) -> list[RoomWithLeftRoomsDTO]:
        rooms = await HotelRepository.get_rooms_by_hotel(instance_id=instance_id, term_data=term_data)
        return rooms


    @router.get("/all")
    @cache(expire=20)
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