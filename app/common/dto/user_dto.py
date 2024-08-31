from common.dto.base import IdBase, BaseDTO


class User(BaseDTO):
    email: str
    hashed_password: str


class UserDTOAdd(User):
    pass


class UserDTOUpdate(User):
    pass


class UserDTO(UserDTOUpdate, IdBase):
    pass
