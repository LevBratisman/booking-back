import datetime
from pydantic import EmailStr
from sqlalchemy import select
from app.tasks.celery_app import celery_worker
import smtplib
import asyncio

from app.common.repository.booking_repository import BookingRepository
from app.common.repository.user_repository import UserRepository
from app.common.models import Booking
from app.common.dto.booking_dto import BookingDTO

from app.tasks.email_template import (
    create_booking_remind_day_template,
    create_booking_remind_three_days_template
)
from app.core.config import settings



@celery_worker.task(name='remind_for_check_in_booking')
def send_remind_for_check_in():

    bookings = asyncio.run(BookingRepository.get_all())

    if not bookings:
        return
    
    for booking in bookings:
        date_from_obj = datetime.datetime.strptime(str(booking.date_from), "%Y-%m-%d")
        time_delta = date_from_obj - datetime.datetime.today()

        if time_delta.days == 3:
            user = asyncio.run(UserRepository.get_by_id(instance_id=booking.user_id))
            booking_dict = BookingDTO.model_validate(booking).model_dump()
            msg_content = create_booking_remind_three_days_template(booking_dict, user.email)

            with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.send_message(msg_content)

        elif time_delta.days == 1:
            user = asyncio.run(UserRepository.get_by_id(instance_id=booking.user_id))
            booking_dict = BookingDTO.model_validate(booking).model_dump()
            msg_content = create_booking_remind_day_template(booking_dict, user.email)

            with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.send_message(msg_content)