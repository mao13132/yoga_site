# Generated by Django 4.2.2 on 2023-06-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_page', '0010_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='title1',
            field=models.TextField(blank=True, null=True, verbose_name='Контакты'),
        ),
    ]
