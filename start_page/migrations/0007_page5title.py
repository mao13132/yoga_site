# Generated by Django 4.2.2 on 2023-06-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0006_page4cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page5Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=120, verbose_name='Главный заголовок')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('title2', models.CharField(max_length=120, verbose_name='Нижний заголовок')),
            ],
            options={
                'verbose_name': '5 экран',
                'verbose_name_plural': '5 экран',
            },
        ),
    ]
