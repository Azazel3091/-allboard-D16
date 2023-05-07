from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Post(models.Model):
    CAT = (('TANKS', 'Танки'),
        ('HEALERS', 'Хилы'),
        ('DAMAGE DILERS', 'ДД'),
        ('MERCHANTS', 'Торговцы'),
        ('GUILDMASTER', 'Гилдмастеры'),
        ('QUESTGIVERS', 'Квестгиверы'),
        ('BLACKSMITH', 'Кузнецы'),
        ('LEATHER_WORKER', 'Кожевники'),
        ('POTION MAKERS', 'Зельевары'),
        ('SPELL MASTER', 'Мастера заклинаний '))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=CAT, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = RichTextField()

    def __str__(self):
        return f'{self.CAT}'


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
