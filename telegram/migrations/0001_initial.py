# Generated by Django 4.2.2 on 2023-07-06 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300, verbose_name='Приглашение')),
                ('payment_link', models.CharField(max_length=200, verbose_name='Платёжка')),
                ('id_tg', models.CharField(blank=True, max_length=120, null=True, verbose_name='ID клиента')),
                ('date_connect', models.DateTimeField(blank=True, null=True, verbose_name='Подписался')),
                ('buy_chat', models.CharField(max_length=120, verbose_name='Доступ к чату')),
                ('start_license', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Начало лицензии')),
                ('ower_license', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Окончание')),
                ('activ', models.BooleanField(default=True, verbose_name='Активна')),
                ('kick', models.BooleanField(default=False, verbose_name='Удален')),
                ('free', models.BooleanField(default=False, verbose_name='free')),
                ('source', models.CharField(blank=True, max_length=120, null=True, verbose_name='Источник')),
            ],
            options={
                'verbose_name': 'ссылку',
                'verbose_name_plural': 'ссылки',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tg', models.CharField(blank=True, max_length=120, null=True, verbose_name='ID телеграма')),
                ('name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Имя')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Полное имя')),
                ('login', models.CharField(blank=True, max_length=120, null=True, verbose_name='Логин')),
                ('email', models.CharField(blank=True, max_length=120, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=120, null=True, verbose_name='Телефон')),
                ('join_date', models.DateField(default=datetime.datetime.now, verbose_name='Первый контакт')),
                ('last_time', models.DateTimeField(blank=True, null=True, verbose_name='Последний')),
                ('push1', models.BooleanField(default=True)),
                ('push2', models.BooleanField(default=True)),
                ('rang', models.CharField(blank=True, max_length=120, null=True, verbose_name='Статус')),
                ('buy_chat', models.CharField(blank=True, max_length=120, null=True, verbose_name='Купленный чат')),
                ('license', models.BooleanField(default=False, verbose_name='Лицензия')),
                ('start_license', models.DateTimeField(blank=True, null=True, verbose_name='Начало лицензии')),
                ('ower_license', models.DateTimeField(blank=True, null=True, verbose_name='Окончание')),
                ('other', models.CharField(blank=True, max_length=120, null=True, verbose_name='Другое')),
                ('demo', models.BooleanField(default=False, verbose_name='Free оффер')),
            ],
            options={
                'verbose_name': 'пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
