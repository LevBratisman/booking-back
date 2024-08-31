from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

from db.base_class import Base

class Hotel(Base):
    name: Mapped[str] = mapped_column(unique=True)
    location: Mapped[str] = mapped_column()
    rooms_quantity: Mapped[int] = mapped_column()
    services: Mapped[list[str] | None] = mapped_column(JSON)
    image_id: Mapped[int | None] = mapped_column()