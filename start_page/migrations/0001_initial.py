# Generated by Django 4.2.2 on 2023-06-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название сайта')),
                ('description', models.TextField(blank=True, verbose_name='Описание сайта')),
                ('h1_1', models.CharField(max_length=128, verbose_name='Заголовок 1')),
                ('h1_2', models.CharField(max_length=128, verbose_name='Заголовок 2')),
                ('button1', models.CharField(max_length=128, verbose_name='Текст кнопки 1')),
                ('button2', models.CharField(max_length=128, verbose_name='Текст кнопки 2')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
