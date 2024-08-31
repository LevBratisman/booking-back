from jose import jwt
from passlib.context import CryptContext
from datetime import UTC, datetime, timedelta

from pydantic import EmailStr

from common.models.user import User
from core.config import settings
from common.repository.user_repository import UserRepository


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=1)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)

    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def authenticate_user(email: EmailStr, password: str) -> User:
    user = await UserRepository.get_one(email=email)
    if user and verify_password(plain_password=password, hashed_password=user.hashed_password):
        return user