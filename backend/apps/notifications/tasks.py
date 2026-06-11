# pyrefly: ignore [missing-import]
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_notification_task(email, title, message):
    """
    Asynchronously dispatch standard system email notification.
    """
    send_mail(
        subject=title,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
    return f"Email sent to {email}"

@shared_task
def send_whatsapp_notification_task(phone, message):
    """
    Future-ready task structure for dispatching WhatsApp notifications.
    Currently acts as a mock logger.
    """
    # Placeholder for integration with services like Twilio or WhatsApp Business API
    print(f"[WHATSAPP MOCK] Sending WhatsApp to {phone}: {message}")
    return f"Mock WhatsApp message queued for {phone}"
