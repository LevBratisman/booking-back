from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv

from app.api.deps import get_current_user
from app.common.models.user import User
from app.common.repository.user_repository import UserRepository
from app.common.dto.user_dto import UserDTO, UserDTOAdd, UserDTOUpdate, UserInfoDTO

router = APIRouter()

@cbv(router)
class UserAPI:

    @router.get("/list")
    async def get_all(self) -> list[UserDTO]:
        result = await UserRepository.get_all()
        return result


    @router.get("/me")
    async def read_user_me(self, user: User = Depends(get_current_user)) -> UserInfoDTO:
        return user


    @router.get("/{instance_id}")
    async def get_by_id(self, instance_id: int) -> UserDTO:
        result = await UserRepository.get_by_id(instance_id=instance_id)
        return result
    

    @router.patch("/{instance_id}")
    async def update_user(self, data: UserDTOUpdate, instance_id: int):
        converted_data = data.to_dict()
        await UserRepository.update(instance_id=instance_id, **converted_data)
        return 'UPDATED'
    

    @router.delete("/{instance_id}")
    async def delete_user(self, instance_id: int):
        await UserRepository.delete(instance_id=instance_id)
        return 'DELETED'
    

    