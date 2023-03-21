from django.core.mail import send_mail



def send_order_confirmation_code(email, code , name, price):
    full_link = f'Привет, подверди заказ на продукт {name} на сумму {price} \n\n http://lacolhost:8000/api/v1/confirm/{code}'
    
    send_mail(
        'Order from shop py25',
        full_link,
        'amanturkubatov545@gmail.com',
        [email]
    )