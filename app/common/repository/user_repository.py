from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.crud_base_repository import CRUDBaseRepository
from common.models.user import User


class UserRepository(CRUDBaseRepository):
    model = User