from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact


@shared_task
def send_spam():
    emails = [i.email for i in Contact.objects.all()]
    send_mail(
        'Xacaton shop project',# title
        f'Привет загляни на наш сайт у нас новый товар', # body
        'amanturkubatov545@gmail.com', # from
        emails # to
    )                                                                                                                                                                                                                                                                                                                                                                               