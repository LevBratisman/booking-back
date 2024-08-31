from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from api.deps import get_hotel_service
from common.service.hotel_service import HotelService

router = APIRouter

@cbv(router)
class BookingAPI:

    @router.get("/list")
    async def get_all():
        pass


    @router.get("/{instance_id}/")
    async def get_by_id():
        pass