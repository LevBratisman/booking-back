from pydantic import EmailStr

from common.dto.base import BaseDTO


class RegisterUserDTO(BaseDTO):
    email: EmailStr
    password: str


class LoginUserDTO(BaseDTO):
    email: EmailStr
    password: str