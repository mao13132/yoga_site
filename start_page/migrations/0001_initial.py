# Generated by Django 4.2.2 on 2023-07-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbonimentsCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=120, verbose_name='Главный заголовок')),
                ('title2', models.CharField(max_length=120, verbose_name='Второй заголовок')),
                ('dlina', models.IntegerField(verbose_name='Дней подписки')),
                ('id_chat', models.CharField(blank=True, max_length=120, null=True, verbose_name='ID чата')),
                ('birka', models.CharField(max_length=120, verbose_name='Бирка')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('bonus', models.TextField(verbose_name='Бонус')),
                ('price', models.IntegerField()),
                ('old_price', models.IntegerField()),
                ('button', models.CharField(max_length=120, verbose_name='Надпись кнопки')),
            ],
            options={
                'verbose_name': 'абонемент',
                'verbose_name_plural': 'Абонементы. Редактировать',
            },
        ),
        migrations.CreateModel(
            name='AbonimentsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Главный заголовок')),
                ('title2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Второй заголовок')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'Абонементы. Заголовки',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Описание преимущества')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='ButtonsHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button1', models.CharField(max_length=128, verbose_name='Первая кнопка')),
                ('button2', models.CharField(max_length=128, verbose_name='Вторая кнопка')),
                ('button3', models.CharField(max_length=128, verbose_name='Третья кнопка')),
                ('button4', models.CharField(max_length=128, verbose_name='Четвертая кнопка')),
                ('button5', models.CharField(max_length=128, verbose_name='Пятая кнопка')),
                ('button6', models.CharField(max_length=128, verbose_name='Шестая кнопка')),
            ],
            options={
                'verbose_name': 'Верхние кнопки',
                'verbose_name_plural': 'Верхние кнопки',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.TextField(blank=True, null=True, verbose_name='Контакты')),
                ('telegram', models.CharField(blank=True, max_length=150, null=True, verbose_name='Логин телеграм без @')),
            ],
            options={
                'verbose_name': 'контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='FreeFormTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=150, verbose_name='Верхний заголовок')),
                ('title2', models.CharField(max_length=150, verbose_name='Нижний заголов')),
                ('desc', models.TextField(verbose_name='Описание предложения')),
                ('button', models.CharField(max_length=120, verbose_name='Надпись кнопки')),
            ],
            options={
                'verbose_name': 'бесплатную форму',
                'verbose_name_plural': 'Бесплатная форма',
            },
        ),
        migrations.CreateModel(
            name='LeadFormTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=150, verbose_name='Верхний заголовок')),
                ('title2', models.CharField(max_length=150, verbose_name='Нижний заголов')),
                ('desc', models.TextField(verbose_name='Описание предложения')),
                ('button', models.CharField(max_length=120, verbose_name='Надпись кнопки')),
            ],
            options={
                'verbose_name': 'форму заявки',
                'verbose_name_plural': 'Формы заявок. Тарифы',
            },
        ),
        migrations.CreateModel(
            name='LeadPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=120, verbose_name='Главный заголовок')),
                ('title2', models.CharField(max_length=120, verbose_name='Второй заголовок')),
                ('button', models.CharField(max_length=120, verbose_name='Надпись кнопки')),
                ('image', models.ImageField(upload_to='lead', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'оффер',
                'verbose_name_plural': 'Бесплатный оффер',
            },
        ),
        migrations.CreateModel(
            name='Page2Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider', verbose_name='Изображение')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Заполнение карточки',
                'verbose_name_plural': 'Второй экран 3 КАРТОЧКИ',
            },
        ),
        migrations.CreateModel(
            name='Page2Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('disc1', models.TextField(verbose_name='Первое описание')),
                ('disc2', models.TextField(verbose_name='Второе описание')),
            ],
            options={
                'verbose_name': 'Второй экран',
                'verbose_name_plural': 'Второй экран',
            },
        ),
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
        migrations.CreateModel(
            name='Page4Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50, verbose_name='Заголовок 1')),
                ('title2', models.CharField(max_length=50, verbose_name='Заголовок 2')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '4 экран',
                'verbose_name_plural': '4 экран',
            },
        ),
        migrations.CreateModel(
            name='Page5Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Главный заголовок')),
                ('title2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Нижний заголовок')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '5 экран карта',
                'verbose_name_plural': '5 экран карта',
            },
        ),
        migrations.CreateModel(
            name='Page5Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Главный заголовок')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('title2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Нижний заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='page5', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': '5 экран',
                'verbose_name_plural': '5 экран',
            },
        ),
        migrations.CreateModel(
            name='Page6Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Дни недели')),
                ('title2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Время')),
                ('title3', models.CharField(blank=True, max_length=120, null=True, verbose_name='Заголовок')),
                ('title4', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='sessions', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'расписание',
                'verbose_name_plural': 'Расписание. Редактировать',
            },
        ),
        migrations.CreateModel(
            name='Page6Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Главный заголовок')),
                ('title2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Второй заголовок')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'Раписание. Заголовки',
            },
        ),
        migrations.CreateModel(
            name='Quests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(max_length=120, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'Вопросы. Редактировать',
            },
        ),
        migrations.CreateModel(
            name='QuestsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Главный заголовок')),
                ('title2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Второй заголовок')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'Вопросы. Заголовки',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='reviews', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
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
                ('image', models.ImageField(blank=True, null=True, upload_to='settings', verbose_name='Главная картинка сайта')),
                ('image_mob', models.ImageField(blank=True, null=True, upload_to='settings', verbose_name='Моб картинка сайта')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Имя преподавателя')),
                ('desc', models.TextField(verbose_name='Имя преподавателя')),
                ('image', models.ImageField(upload_to='teachers', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'преподавателя',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
    ]
