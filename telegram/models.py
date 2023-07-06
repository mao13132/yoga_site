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
    last_time = models.DateTimeField(null=True, blank=True, verbose_name='Последний')
    push1 = models.BooleanField(default=True)
    push2 = models.BooleanField(default=True)
    rang = models.CharField(null=True, blank=True, max_length=120, verbose_name='Статус')
    buy_chat = models.CharField(null=True, blank=True, max_length=120, verbose_name='Купленный чат')
    license = models.BooleanField(default=False, verbose_name='Лицензия')
    start_license = models.DateTimeField(null=True, blank=True, verbose_name='Начало лицензии')
    ower_license = models.DateTimeField(null=True, blank=True, verbose_name='Окончание')
    other = models.CharField(null=True, blank=True, max_length=120, verbose_name='Другое')
    demo = models.BooleanField(default=False, verbose_name='Free оффер')

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'


class Links(models.Model):
    link = models.CharField(max_length=300, null=False, blank=False, verbose_name='Приглашение')
    payment_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='Платёжка')
    id_tg = models.CharField(null=True, blank=True, max_length=120, verbose_name='ID клиента')
    date_connect = models.DateTimeField(null=True, blank=True, verbose_name='Подписался')
    buy_chat = models.CharField(null=False, blank=False, max_length=120, verbose_name='Доступ к чату')
    start_license = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Начало лицензии')
    ower_license = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Окончание')
    activ = models.BooleanField(default=True, verbose_name='Активна')
    kick = models.BooleanField(default=False, verbose_name='Удален')
    free = models.BooleanField(default=False, verbose_name='free')
    push = models.BooleanField(default=False, verbose_name='Оплачен')
    source = models.CharField(null=True, blank=True, max_length=120, verbose_name='Источник')

    class Meta:
        verbose_name = 'ссылку'
        verbose_name_plural = 'ссылки'
