from django.core.exceptions import ValidationError
from django.db import models

from django.contrib import messages

class Advantages(models.Model):
    title = models.CharField(max_length=250, verbose_name='Описание преимущества')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def save(self, *args, **kwargs):
        count = Advantages.objects.count()
        if count >= 6:
            if not self.pk and Page2Title.objects.exists():
                return False
            else:
                Advantages.objects.filter(pk=self.pk).update(title=self.title)
        else:
            return super(Advantages, self).save(*args, **kwargs)

    def refresh(self, *args, **kwargs):
        # Do something
        super(Advantages, self).update(*args, **kwargs)
        # Do something else


class Page2Slider(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='slider', verbose_name='Изображение')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Заполнение карточки'
        verbose_name_plural = 'Второй экран 3 КАРТОЧКИ'

    def save(self, *args, **kwargs):
        count = Page2Slider.objects.count()
        if count >= 3:

            if not self.pk and Page2Slider.objects.exists():
                return False
            else:
                Page2Slider.objects.filter(pk=Page2Slider.objects.first().pk).update(image=self.image,
                                                                                     title=self.title,
                                                                                     desc=self.desc)
        else:
            return super(Page2Slider, self).save(*args, **kwargs)



# Create your models here.


class Page2Title(models.Model):
    h1 = models.CharField(max_length=128, verbose_name='Заголовок')
    disc1 = models.TextField(null=False, verbose_name='Первое описание')
    disc2 = models.TextField(null=False, verbose_name='Второе описание')

    def save(self, *args, **kwargs):
        if not self.pk and Page2Title.objects.exists():
            Page2Title.objects.filter(pk=Page2Title.objects.first().pk).update(h1=self.h1,
                                                                               disc1=self.disc1, disc2=self.disc2)
        else:
            return super(Page2Title, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Второй экран'
        verbose_name_plural = 'Второй экран'


class ButtonsHead(models.Model):
    button1 = models.CharField(max_length=128, verbose_name='Первая кнопка')
    button2 = models.CharField(max_length=128, verbose_name='Вторая кнопка')
    button3 = models.CharField(max_length=128, verbose_name='Третья кнопка')
    button4 = models.CharField(max_length=128, verbose_name='Четвертая кнопка')
    button5 = models.CharField(max_length=128, verbose_name='Пятая кнопка')
    button6 = models.CharField(max_length=128, verbose_name='Шестая кнопка')

    def save(self, *args, **kwargs):
        if not self.pk and ButtonsHead.objects.exists():
            ButtonsHead.objects.filter(pk=ButtonsHead.objects.first().pk).update(button1=self.button1,
                                                                                 button2=self.button2,
                                                                                 button3=self.button3,
                                                                                 button4=self.button4,
                                                                                 button5=self.button5,
                                                                                 button6=self.button6)
        else:
            return super(ButtonsHead, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Верхние кнопки'
        verbose_name_plural = 'Верхние кнопки'


class Settings(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название сайта')
    description = models.TextField(null=False, blank=True, verbose_name='Описание сайта')
    h1_1 = models.CharField(max_length=128, verbose_name='Заголовок 1')
    h1_2 = models.CharField(max_length=128, verbose_name='Заголовок 2')
    button1 = models.CharField(max_length=128, verbose_name='Текст кнопки 1')
    button2 = models.CharField(max_length=128, verbose_name='Текст кнопки 2')
    image = models.ImageField(null=True, blank=True, upload_to='settings', verbose_name='Главная картинка сайта')
    image_mob = models.ImageField(null=True, blank=True, upload_to='settings', verbose_name='Моб картинка сайта')

    # def save_model(self, request, obj, form, change):
    #     if 'owner' in form.changed_data:
    #         messages.add_message(request, messages.INFO, 'Car has been sold')
    #     super(Settings, self).save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        if not self.pk and Settings.objects.exists():
            Settings.objects.filter(pk=Settings.objects.first().pk).update(title=self.title,
                                                                           description=self.description, h1_1=self.h1_1,
                                                                           h1_2=self.h1_2, button1=self.button1,
                                                                           button2=self.button2, image=self.image)
        else:
            return super(Settings, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки сайта'
