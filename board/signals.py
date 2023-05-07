from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Reply


@receiver(post_save, sender=Reply)
def my_handler(sender, instance, created, **kwargs):
    if instance.status:  # Если автор обьявления принял отклик - автору отклика приходит сообщение
        mail = instance.author.email
        send_mail(
            'Subject',
            'message',
            'DruidTrad@yandex.ru',
            [mail],
            fail_silently=False
        )
    mail = instance.article.author.email
    send_mail(
        'Subject',
        'message',
        'DruidTrad@yandex.ru',
        [mail],
        fail_silently=False
    )
