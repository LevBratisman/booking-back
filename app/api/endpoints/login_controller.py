from fastapi import APIRouter, Depends, Response

from app.common.dto.user_dto import UserDTO
from app.core.security import get_password_hash, authenticate_user, create_access_token
from app.common.dto.auth_dto import RegisterUserDTO, LoginUserDTO
from app.common.repository.user_repository import UserRepository

from app.core.exceptions import (
    UserAlreadyExistsException,
    IncorrectPasswordOrEmailException
)

router = APIRouter()


@router.post('/register')
async def register_user(data: RegisterUserDTO) -> UserDTO:
    existing_user = await UserRepository.get_one(email=data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(password=data.password)

    result = await UserRepository.add(
        email=data.email,
        hashed_password=hashed_password
    )
    return result


@router.post('/login')
async def login_user(response: Response, data: LoginUserDTO) -> dict:
    user = await authenticate_user(email=data.email, password=data.password)
    if not user:
        raise IncorrectPasswordOrEmailException
    
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)

    return {"access_token": access_token}


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')
    return 'Logged out'