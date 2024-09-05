# Import all the models, so that Base has them before being
# imported by Alembic

from app.common import models  # noqa
from app.db.base_class import Base  # noqa