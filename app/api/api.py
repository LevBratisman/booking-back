from fastapi import APIRouter

from api.endpoints.login_controller import router as login_router
from api.endpoints.hotel_controller import router as hotel_router
from api.endpoints.booking_controller import router as booking_router
from api.endpoints.room_controller import router as room_router
from api.endpoints.user_controller import router as user_router

main_router = APIRouter()

main_router.include_router(login_router, tags=['Auth'])
main_router.include_router(user_router, prefix="/users", tags=['Users'])
main_router.include_router(hotel_router, prefix="/hotels", tags=['Hotels'])
main_router.include_router(booking_router, prefix="/bookings", tags=['Booking'])
main_router.include_router(room_router, prefix="/rooms", tags=['Rooms'])