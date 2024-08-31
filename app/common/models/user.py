from sqlalchemy.orm import Mapped, mapped_column

from db.base_class import Base

class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()