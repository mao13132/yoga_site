# Generated by Django 4.2.2 on 2023-07-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_alter_links_payment_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='push',
            field=models.BooleanField(default=False),
        ),
    ]
