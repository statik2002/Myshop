from smtplib import SMTPDataError, SMTPRecipientsRefused
from django.core.signing import Signer
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from main.models import Customer


def create_sign(payload: dict) -> str:
    sign = Signer()
    signed_object = sign.sign_object(payload)
    return signed_object


def usign_sgn(sign_object: str) -> dict:
    sign = Signer()
    return sign.unsign_object(sign_object)


def send_mail(request, user: Customer) -> dict:
    # Берем текущий сайт
    current_site = get_current_site(request)

    # Создаем токен
    token = create_sign({'user_id': user.pk, 'user_name': user.first_name})

    # Формируем сообщение для письма
    message = render_to_string(
        'main/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'token': token,
            }
        )
    
    # Тема письма
    mail_subject = 'Активируйте свой аккаунт'

    # Берем мыло регистрирующегося пользователя
    to_email = user.email

    # Формируем письмо
    email = EmailMessage(mail_subject, message, to=[to_email])

     # Отсылаем письмо
    try:
        result = email.send()
        if result == 1:
            return {'response': 'ok'}

    except SMTPRecipientsRefused:
        return {'email': 'Указан несуществующий email'}
    
    except SMTPDataError as error:
        return {'email': error.with_traceback}