from django.core.mail import send_mail
from notyourmotleycrew import settings
def run():
    to = "oivvio@polite.se"
    subject = "Radac test " + to
    message = "radac test email body " + to
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to])
