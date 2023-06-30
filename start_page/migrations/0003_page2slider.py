# Generated by Django 4.2.2 on 2023-06-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0002_settings_image_mob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page2Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider', verbose_name='Изображение')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Второй экран - КАРТОЧКИ',
            },
        ),
    ]
