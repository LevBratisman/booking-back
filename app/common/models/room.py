from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, ForeignKey

from app.db.base_class import Base

class Room(Base):
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    services: Mapped[list[str] | None] = mapped_column(JSON)
    image_id: Mapped[int | None] = mapped_column()
