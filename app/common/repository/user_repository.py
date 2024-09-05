from sqlalchemy.ext.asyncio import AsyncSession

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.models.user import User


class UserRepository(CRUDBaseRepository):
    model = User