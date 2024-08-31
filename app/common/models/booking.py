from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Date, Computed
from datetime import date

from db.base_class import Base, TimeStampedModel

class Booking(Base):
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int] = mapped_column()
    total_cost: Mapped[int] = mapped_column(Computed('(date_to - date_from) * price'))
    total_days: Mapped[int] = mapped_column(Computed('date_to - date_from'))
