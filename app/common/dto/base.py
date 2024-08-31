from pydantic import BaseModel, ConfigDict
from typing import TypeVar
from datetime import datetime

from db.base_class import ModelType


class BaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    def to_dict(self):
        return dict(self)
    

class IdBase(BaseDTO):
    id: int


class UserDependsBase(BaseDTO):
    user_id: int


class TimeStampedBase(BaseDTO):
    created_at: datetime


CreateDTOType = TypeVar('CreateDTOType', bound=BaseDTO)
UpdateDTOType = TypeVar('UpdateDTOType', bound=IdBase)
ModelDTOType = TypeVar('ModelDTOType', bound=BaseDTO)


def model_to_dto(*, model_db: ModelType | None, model_dto: ModelDTOType) -> ModelDTOType | None:
    if model_db is None:
        return None
    return model_dto.model_validate(model_db, from_attributes=True)


