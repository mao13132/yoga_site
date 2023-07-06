from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

from django.contrib import messages


class FreeFormTitle(models.Model):
    title1 = models.CharField(max_length=150, null=False, blank=False, verbose_name='Верхний заголовок')
    title2 = models.CharField(max_length=150, null=False, blank=False, verbose_name='Нижний заголов')
    desc = models.TextField(null=False, blank=False, verbose_name='Описание предложения')
    button = models.CharField(null=False, blank=False, max_length=120, verbose_name='Надпись кнопки')

    class Meta:
        verbose_name = 'бесплатную форму'
        verbose_name_plural = 'Бесплатная форма'

    def save(self, *args, **kwargs):
        count = FreeFormTitle.objects.count()
        if count >= 1:
            if not self.pk and FreeFormTitle.objects.exists():
                return False
            else:
                FreeFormTitle.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2,
                                                                desc=self.desc, button=self.button)
        else:
            return super(FreeFormTitle, self).save(*args, **kwargs)




class LeadFormTitle(models.Model):
    title1 = models.CharField(max_length=150, null=False, blank=False, verbose_name='Верхний заголовок')
    title2 = models.CharField(max_length=150, null=False, blank=False, verbose_name='Нижний заголов')
    desc = models.TextField(null=False, blank=False, verbose_name='Описание предложения')
    button = models.CharField(null=False, blank=False, max_length=120, verbose_name='Надпись кнопки')

    class Meta:
        verbose_name = 'форму заявки'
        verbose_name_plural = 'Формы заявок. Тарифы'

    def save(self, *args, **kwargs):
        count = LeadFormTitle.objects.count()
        if count >= 3:
            if not self.pk and LeadFormTitle.objects.exists():
                return False
            else:
                LeadFormTitle.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2,
                                                                desc=self.desc, button=self.button)
        else:
            return super(LeadFormTitle, self).save(*args, **kwargs)

class Contacts(models.Model):
    title1 = models.TextField(null=True, blank=True, verbose_name='Контакты')
    telegram = models.CharField(max_length=150, null=True, blank=True, verbose_name='Логин телеграм без @')

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'Контакты'

    def save(self, *args, **kwargs):
        count = Contacts.objects.count()
        if count >= 1:
            if not self.pk and Contacts.objects.exists():
                return False
            else:
                Contacts.objects.filter(pk=self.pk).update(title1=self.title1, telegram=self.telegram)
        else:
            return super(Contacts, self).save(*args, **kwargs)


class Quests(models.Model):
    quest = models.CharField(null=False, blank=False, max_length=120, verbose_name='Вопрос')
    answer = models.TextField(null=False, blank=False, verbose_name='Ответ')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы. Редактировать'

    def save(self, *args, **kwargs):
        count = Quests.objects.count()
        if count >= 9:
            if not self.pk and Quests.objects.exists():
                return False
            else:
                Quests.objects.filter(pk=self.pk).update(quest=self.quest, answer=self.answer)
        else:
            return super(Quests, self).save(*args, **kwargs)


class QuestsTitle(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Главный заголовок')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Второй заголовок')

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'Вопросы. Заголовки'

    def save(self, *args, **kwargs):
        count = QuestsTitle.objects.count()
        if count >= 1:
            if not self.pk and QuestsTitle.objects.exists():
                return False
            else:
                QuestsTitle.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2)
        else:
            return super(QuestsTitle, self).save(*args, **kwargs)


class LeadPage(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Главный заголовок')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Второй заголовок')
    buy_chat = models.CharField(null=False, blank=False, max_length=120, verbose_name='Доступ к чату')
    button = models.CharField(null=True, blank=True, max_length=120, verbose_name='Надпись кнопки')
    image = models.ImageField(null=True, blank=True, upload_to='lead', verbose_name='Изображение')

    class Meta:
        verbose_name = 'оффер'
        verbose_name_plural = 'Бесплатный оффер'

    def save(self, *args, **kwargs):
        count = LeadPage.objects.count()
        if count >= 1:
            if not self.pk and LeadPage.objects.exists():
                return False
            else:
                LeadPage.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2,
                                                           button=self.button, image=self.image)
        else:
            return super(LeadPage, self).save(*args, **kwargs)


class Reviews(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='reviews', verbose_name='Отзыв')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def save(self, *args, **kwargs):
        count = Reviews.objects.count()
        if count >= 8:
            if not self.pk and Reviews.objects.exists():
                return False
            else:
                Reviews.objects.filter(pk=self.pk).update(image=self.image)
        else:
            return super(Reviews, self).save(*args, **kwargs)


class AbonimentsCards(models.Model):
    """Офферы offer"""
    title1 = models.CharField(null=False, blank=False, max_length=120, verbose_name='Главный заголовок')
    title2 = models.CharField(null=False, blank=False, max_length=120, verbose_name='Второй заголовок')
    dlina = models.IntegerField(null=False, blank=False, verbose_name='Дней подписки')
    id_chat = models.CharField(null=True, blank=True, max_length=120, verbose_name='ID чата на который подписываем')
    birka = models.CharField(null=False, blank=False, max_length=120, verbose_name='Бирка')
    desc = models.TextField(null=False, blank=False, verbose_name='Описание')
    bonus = models.TextField(null=False, blank=False, verbose_name='Бонус')
    price = models.IntegerField(null=False, blank=False)
    old_price = models.IntegerField(null=False, blank=False)
    button = models.CharField(null=False, blank=False, max_length=120, verbose_name='Надпись кнопки')

    class Meta:
        verbose_name = 'абонемент'
        verbose_name_plural = 'Абонементы. Редактировать'

    def save(self, *args, **kwargs):
        count = AbonimentsCards.objects.count()
        if count >= 9:
            if not self.pk and AbonimentsCards.objects.exists():
                return False
            else:
                AbonimentsCards.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2,
                                                                  birka=self.birka, desc=self.desc,
                                                                  bonus=self.bonus, price=self.price,
                                                                  button=self.button, old_price=self.old_price,
                                                                  dlina=self.dlina)
        else:
            return super(AbonimentsCards, self).save(*args, **kwargs)


class AbonimentsTitle(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Главный заголовок')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Второй заголовок')

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'Абонементы. Заголовки'

    def save(self, *args, **kwargs):
        count = AbonimentsTitle.objects.count()
        if count >= 1:
            if not self.pk and AbonimentsTitle.objects.exists():
                return False
            else:
                AbonimentsTitle.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2)
        else:
            return super(AbonimentsTitle, self).save(*args, **kwargs)


class Teachers(models.Model):
    name = models.CharField(max_length=130, null=False, blank=False, verbose_name='Имя преподавателя')
    desc = models.TextField(null=False, blank=False, verbose_name='Имя преподавателя')
    image = models.ImageField(null=False, blank=False, upload_to='teachers', verbose_name='Изображение')

    class Meta:
        verbose_name = 'преподавателя'
        verbose_name_plural = 'Преподаватели'

    def save(self, *args, **kwargs):
        count = Teachers.objects.count()
        if count >= 6:
            if not self.pk and Teachers.objects.exists():
                return False
            else:
                Teachers.objects.filter(pk=self.pk).update(name=self.name, desc=self.desc,
                                                           image=self.image)
        else:
            return super(Teachers, self).save(*args, **kwargs)


class Page6Session(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Дни недели')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Время')
    title3 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Заголовок')
    title4 = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=False, blank=False, upload_to='sessions', verbose_name='Изображение')

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'Расписание. Редактировать'

    def save(self, *args, **kwargs):
        count = Page6Session.objects.count()
        if count >= 3:
            if not self.pk and Page6Session.objects.exists():
                return False
            else:
                Page6Session.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2,
                                                               title3=self.title3, title4=self.title4,
                                                               image=self.image)
        else:
            return super(Page6Session, self).save(*args, **kwargs)


class Page6Title(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Главный заголовок')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Второй заголовок')

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'Раписание. Заголовки'

    def save(self, *args, **kwargs):
        count = Page6Title.objects.count()
        if count >= 1:
            if not self.pk and Page6Title.objects.exists():
                return False
            else:
                Page6Title.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2)
        else:
            return super(Page6Title, self).save(*args, **kwargs)


class Page5Cards(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Главный заголовок')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Нижний заголовок')
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = '5 экран карта'
        verbose_name_plural = '5 экран карта'

    def save(self, *args, **kwargs):
        count = Page5Cards.objects.count()
        if count >= 4:
            if not self.pk and Page5Cards.objects.exists():
                return False
            else:
                Page5Cards.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2, desc=self.desc)
        else:
            return super(Page5Cards, self).save(*args, **kwargs)


class Page5Title(models.Model):
    title1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Главный заголовок')
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')
    title2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Нижний заголовок')
    image = models.ImageField(null=True, blank=True, upload_to='page5', verbose_name='Изображение')

    class Meta:
        verbose_name = '5 экран'
        verbose_name_plural = '5 экран'

    def save(self, *args, **kwargs):
        count = Page5Title.objects.count()
        if count >= 1:
            if not self.pk and Page5Title.objects.exists():
                return False
            else:
                Page5Title.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2, desc=self.desc,
                                                             image=self.image)
        else:
            return super(Page5Title, self).save(*args, **kwargs)


class Page4Cards(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок карточки')
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = '4 экран карточка'
        verbose_name_plural = '4 экран карточки'

    def save(self, *args, **kwargs):
        count = Page4Cards.objects.count()
        if count >= 6:
            if not self.pk and Page4Cards.objects.exists():
                return False
            else:
                Page4Cards.objects.filter(pk=self.pk).update(title=self.title, desc=self.desc)
        else:
            return super(Page4Cards, self).save(*args, **kwargs)


class Page4Title(models.Model):
    title1 = models.CharField(max_length=50, verbose_name='Заголовок 1')
    title2 = models.CharField(max_length=50, verbose_name='Заголовок 2')
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = '4 экран'
        verbose_name_plural = '4 экран'

    def save(self, *args, **kwargs):
        count = Page4Title.objects.count()
        if count >= 1:
            if not self.pk and Page4Title.objects.exists():
                return False
            else:
                Page4Title.objects.filter(pk=self.pk).update(title1=self.title1, title2=self.title2, desc=self.desc)
        else:
            return super(Page4Title, self).save(*args, **kwargs)


class Advantages(models.Model):
    title = models.CharField(max_length=250, verbose_name='Описание преимущества')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def save(self, *args, **kwargs):
        count = Advantages.objects.count()
        if count >= 6:
            if not self.pk and Advantages.objects.exists():
                return False
            else:
                Advantages.objects.filter(pk=self.pk).update(title=self.title)
        else:
            return super(Advantages, self).save(*args, **kwargs)


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
