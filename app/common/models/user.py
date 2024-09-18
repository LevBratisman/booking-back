from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as EnumType
from enum import Enum

from app.db.base_class import Base


class RoleEnum(str, Enum):
    CLIENT = "CLIENT"
    ADMIN = "ADMIN"


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(EnumType(RoleEnum, name="role_enum"), default=RoleEnum.CLIENT)
    username: Mapped[str | None] = mapped_column()
    age: Mapped[int | None] = mapped_column()