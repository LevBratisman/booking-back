from email.message import EmailMessage
from app.core.config import settings

from pydantic import EmailStr


def create_booking_confirmation_template(
    booking: dict,
    email_to: EmailStr
):
    email = EmailMessage()

    email['Subject'] = 'Подтверждение бронирования'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>Информация о бронировании</h1>
            Вы забронировали отель с {booking['date_from']} по {booking['date_to']}
        """,
        subtype='html'
    )

    return email


def create_booking_remind_day_template(
    booking: dict,
    email_to: EmailStr
):
    email = EmailMessage()

    email['Subject'] = 'Завтра заселение'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>Информация о бронировании</h1>
            Вы забронировали отель с {booking['date_from']} по {booking['date_to']}
        """,
        subtype='html'
    )

    return email


def create_booking_remind_three_days_template(
    booking: dict,
    email_to: EmailStr
):
    email = EmailMessage()

    email['Subject'] = '3 дня до заселения'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>Информация о бронировании</h1>
            Вы забронировали отель с {booking['date_from']} по {booking['date_to']}
        """,
        subtype='html'
    )

    return email