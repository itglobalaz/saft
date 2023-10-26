from django.core.mail import EmailMessage

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@alfagroup.az'
EMAIL_HOST_PASSWORD = 'Alfa-2022'
DEFAULT_FROM_EMAIL = 'info@alfagroup.az'
EMAIL_USE_TLS = True


def send_email_feedback(data):
    name = data['name']
    email = data['email']
    subject = data['subject']
    description = data['description']
    email_body = (f'<strong>Тема</strong>: {subject}<br/>'
                  f'<strong>Имя</strong>: {name}<br/>'
                  f'<strong>Почта:</strong> {email}<br/>'
                  f'<strong>Информация</strong>: {description}<br/>'
                  f'Письмо отправлена из сайта alfagroup.az'
                  )
    email = EmailMessage('Название темы', email_body, 'info@alfagroup.az', to=['info@alfagroup.az'])
    email.content_subtype = "html"
    email.send()
