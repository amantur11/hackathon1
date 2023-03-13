from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Xacaton shop project', # title
        f'http://localhost:8000/api/v1/account/activate/{code}/', # body
        'amanturkubatov545@gmail.com', # from
        [email] # to
    )   

def send_reset_password_code(email, code):
    send_mail(
        'Xacaton shop project', # title
        f'привет чтобы бросить пароль тебе нужно знать этот код = {code}', # body
        'amanturkubatov545@gmail.com', # from
        [email] # to
    )