# Generated by Django 4.2.2 on 2023-06-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0005_page4title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page4Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок карточки')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '4 экран карточка',
                'verbose_name_plural': '4 экран карточки',
            },
        ),
    ]
