import time
from django.core.mail import send_mail
from .celery import app


@app.task
def send_email_message(code, email, status):
    time.sleep(5)
    link = f'http://localhost:8000/account/activate/{code}'


    if status == 'register':

        send_mail(
            'from django project',
            link,
            'testweb23062000@gmail.com',
            [email]
        )

    elif status == 'reset_password':
        send_mail(
            'Reset your password',
            f'Code activations: {code}',
            'mrnaamatov79@gmail.com',
            [email]
        )

    elif status == 'reserv':
        send_mail(
            'from django project',
            link,
            'mrnaamatov79@gmail.com',
            [email]

        )
