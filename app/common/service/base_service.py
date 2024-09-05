from sqlalchemy.ext.asyncio import AsyncSession

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.db.base_class import ModelType
from app.common.dto.base import ModelDTOType
from app.common.dto.base import model_to_dto

class BaseService:
    def __init__(
            self,
            *,
            session: AsyncSession,
            repository: CRUDBaseRepository,
            model: ModelType,
            model_dto: ModelDTOType
        ) -> None:
        self.session = session
        self.repository = repository(session=session)
        self.model = model
        self.model_dto = model_dto

    
    async def to_dto(
        self, model_dto: ModelDTOType, model_db: ModelType | None
    ) -> ModelDTOType | None:
        return model_to_dto(model_db=model_db, model_dto=model_dto)


    async def get_by_id(self, *, instance_id: int) -> ModelDTOType:
        result = await self.repository.get_by_id(instance_id=instance_id)
        return await self.to_dto(model_dto=self.model_dto, model_db=self.model)
    

    async def get_all(self) -> list[ModelDTOType]:
        result = await self.repository.get_all()
        return [await self.to_dto(model_dto=self.model_dto, model_db=self.model) for model in result]
    

    async def get_by_user(self):
        pass