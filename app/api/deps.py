from datetime import datetime, UTC
from fastapi import Depends, Request, HTTPException, status
from jose import jwt, JWTError
from pydantic import ValidationError

from app.common.models.user import User
from app.core.config import settings
from app.common.repository.user_repository import UserRepository
from app.common.models.user import RoleEnum
from app.core.exceptions import (
    TokenDoesNotExistException,
    InvalidOrExpiredTokenException
)


def get_access_token(request: Request) -> str | None:
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenDoesNotExistException
    return token


async def get_current_user(*, token: str = Depends(get_access_token)) -> User :
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM
        )
    except (JWTError, ValidationError):
        raise InvalidOrExpiredTokenException
        
    user = await UserRepository.get_by_id(instance_id=int(payload.get('sub')))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return user


async def get_admin(user: User = Depends(get_current_user)):
    if user.role == RoleEnum.ADMIN:
        return user