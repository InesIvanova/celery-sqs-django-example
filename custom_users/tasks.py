import time

from celery import shared_task

from services.ses import SESService


@shared_task()
def send_welcome_email(name, email):
    time.sleep(15)
    SESService().send_email(
        f"Welcome, {name}!",
        "Welcome to our website, and thanks for your registration.",
        email,
    )
