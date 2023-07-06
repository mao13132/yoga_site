from datetime import datetime

from django.db import models


# Create your models here.

class Orders(models.Model):
    offer = models.CharField(max_length=300, null=False, blank=False, verbose_name=f'Оффер')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=f'Имя клиента')
    phone = models.CharField(max_length=30, null=False, blank=False, verbose_name=f'Телефон')
    telegram = models.CharField(max_length=30, null=True, blank=True, verbose_name=f'Телеграм клиента')
    price = models.CharField(max_length=30, null=False, blank=False, verbose_name=f'Стоимость')
    ip = models.CharField(max_length=30, null=True, blank=True, verbose_name=f'IP')
    comments = models.TextField(null=True, blank=True, verbose_name=f'Комментарий')
    source = models.TextField(null=True, blank=True, verbose_name=f'Источник')
    buy_chat = models.CharField(max_length=30, null=True, blank=True, verbose_name=f'Купленный чат')
    link = models.CharField(max_length=200, null=True, blank=True, verbose_name=f'Ссылка')
    date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Время заказа')

    class Meta:
        verbose_name = f'Заявка'
        verbose_name_plural = f'Заявки'

    def __str__(self):
        return f'{self.name} {self.telegram} {self.date}'
