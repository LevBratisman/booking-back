from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import declarative_mixin
from datetime import datetime
from typing import TypeVar


@as_declarative()
class Base:
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    

@declarative_mixin
class TimeStampedModel:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())



ModelType = TypeVar("ModelType", bound=Base)