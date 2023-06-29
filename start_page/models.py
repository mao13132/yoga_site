from django.core.exceptions import ValidationError
from django.db import models

from django.contrib import messages


# Create your models here.

class Settings(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название сайта')
    description = models.TextField(null=False, blank=True, verbose_name='Описание сайта')
    h1_1 = models.CharField(max_length=128, verbose_name='Заголовок 1')
    h1_2 = models.CharField(max_length=128, verbose_name='Заголовок 2')
    button1 = models.CharField(max_length=128, verbose_name='Текст кнопки 1')
    button2 = models.CharField(max_length=128, verbose_name='Текст кнопки 2')

    # def save_model(self, request, obj, form, change):
    #     if 'owner' in form.changed_data:
    #         messages.add_message(request, messages.INFO, 'Car has been sold')
    #     super(Settings, self).save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        if not self.pk and Settings.objects.exists():
            Settings.objects.filter(pk=Settings.objects.first().pk).update(title=self.title,
                                                                           description=self.description, h1_1=self.h1_1,
                                                                           h1_2=self.h1_2, button1=self.button1,
                                                                           button2=self.button2)
        else:
            return super(Settings, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки сайта'
