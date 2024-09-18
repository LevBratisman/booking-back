from app.common.dto.base import IdBase, BaseDTO
from app.common.models.user import RoleEnum


class User(BaseDTO):
    email: str
    hashed_password: str
    role: RoleEnum
    username: str
    age: int


class UserInfoDTO(BaseDTO):
    email: str
    role: RoleEnum
    username: str
    age: int


class UserDTOAdd(User):
    pass


class UserDTOUpdate(User):
    pass


class UserDTO(UserDTOUpdate, IdBase):
    pass
