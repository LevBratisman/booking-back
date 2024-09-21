from celery import Celery
from celery.schedules import crontab

from app.core.config import settings

celery_worker = Celery(
    "tasks",
    broker=settings.REDIS_URI,
    include=[
        'app.tasks.tasks',
        'app.tasks.scheduled'
    ]
)

celery_worker.conf.beat_schedule = {
    'booking_reminder': {
        'task': 'remind_for_check_in_booking',
        'schedule': crontab(hour="9")
    }
}