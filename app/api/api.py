from fastapi import APIRouter

from api.endpoints.hotel_controller import router as hotel_router

main_router = APIRouter()

main_router.include_router(hotel_router, prefix="/hotels", tags=['Hotels'])