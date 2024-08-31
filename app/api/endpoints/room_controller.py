from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from common.repository.room_repository import RoomRepository
from common.dto.room_dto import RoomDTO, RoomDTOAdd, RoomDTOUpdate

router = APIRouter()

@cbv(router)
class RoomAPI:

    @router.get("/list")
    async def get_all(self) -> list[RoomDTO]:
        result = await RoomRepository.get_all()
        return result


    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> RoomDTO:
        result = await RoomRepository.get_by_id(instance_id=instance_id)
        return result
    

    @router.post("/")
    async def add_room(self, data: RoomDTOAdd) -> RoomDTO:
        converted_data = data.to_dict()
        result = await RoomRepository.add(**converted_data)
        return result
    

    @router.patch("/{instance_id}")
    async def update_room(self, data: RoomDTOUpdate, instance_id: int):
        converted_data = data.to_dict()
        await RoomRepository.update(instance_id=instance_id, **converted_data)
        return 'UPDATED'
    

    @router.delete("/{instance_id}")
    async def delete_room(seld, instance_id: int):
        await RoomRepository.delete(instance_id=instance_id)
        return 'DELETED'