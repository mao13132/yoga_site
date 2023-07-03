from datetime import datetime

from django.db import models


# Create your models here.

class Users(models.Model):
    id_tg = models.CharField(null=True, blank=True, max_length=120, verbose_name='ID телеграма')
    name = models.CharField(null=True, blank=True, max_length=120, verbose_name='Имя')
    full_name = models.CharField(null=True, blank=True, max_length=120, verbose_name='Полное имя')
    login = models.CharField(null=True, blank=True, max_length=120, verbose_name='Логин')
    email = models.CharField(null=True, blank=True, max_length=120, verbose_name='Email')
    phone = models.CharField(null=True, blank=True, max_length=120, verbose_name='Телефон')
    join_date = models.DateField(default=datetime.now, verbose_name='Первый контакт')
    last_time = models.DateField(null=True, blank=True, verbose_name='Последний')
    push1 = models.BooleanField(default=True)
    push2 = models.BooleanField(default=True)
    rang = models.CharField(null=True, blank=True, max_length=120, verbose_name='Статус')
    buy_chat = models.CharField(null=True, blank=True, max_length=120, verbose_name='Купленный чат')
    license = models.BooleanField(default=False, verbose_name='Лицензия')
    start_license = models.DateField(null=True, blank=True, verbose_name='Начало лицензии')
    ower_license = models.DateField(null=True, blank=True, verbose_name='Окончание')
    other = models.CharField(null=True, blank=True, max_length=120, verbose_name='Другое')
    demo = models.BooleanField(default=False, verbose_name='Free оффер')

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'
