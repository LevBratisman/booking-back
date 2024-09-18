from pydantic import BaseModel, ConfigDict
from typing import TypeVar
from datetime import datetime, date

from app.db.base_class import ModelType

from app.utils.string_utils import to_camel


class BaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)

    def to_dict(self):
        return dict(self)
    

class IdBase(BaseDTO):
    id: int


class UserDependsBase(BaseDTO):
    user_id: int


class TimeStampedBase(BaseDTO):
    created_at: datetime


class TermDTO(BaseDTO):
    date_from: date | None
    date_to: date | None


CreateDTOType = TypeVar('CreateDTOType', bound=BaseDTO)
UpdateDTOType = TypeVar('UpdateDTOType', bound=IdBase)
ModelDTOType = TypeVar('ModelDTOType', bound=BaseDTO)


def model_to_dto(*, model_db: ModelType | None, model_dto: ModelDTOType) -> ModelDTOType | None:
    if model_db is None:
        return None
    return model_dto.model_validate(model_db, from_attributes=True)


