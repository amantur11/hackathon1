from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, code):
    import time
    time.sleep(10)
    send_mail(
        'Xacaton shop project', # title
        f'http://localhost:8000/api/v1/account/activate/{code}/', # body
        'amanturkubatov545@gmail.com', # from
        [email] # to
    )
