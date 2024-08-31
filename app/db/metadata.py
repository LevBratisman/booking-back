# Import all the models, so that Base has them before being
# imported by Alembic

from common import models  # noqa
from db.base_class import Base  # noqa