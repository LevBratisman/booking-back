from pydantic import EmailStr
from app.tasks.celery_app import celery_worker
import smtplib

from app.tasks.email_template import create_booking_confirmation_template
from app.core.config import settings


@celery_worker.task
def send_booking_information_email(
    booking: dict,
    email_to: EmailStr
):
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg_content)