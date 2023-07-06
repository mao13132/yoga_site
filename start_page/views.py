from datetime import timedelta, timezone

from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.views.decorators.http import require_GET

from .forms import OneFormOrders
from .func.page3_advantages import page3_advantages
from .models import *
from .tekegram_sendler import TelegramSendler


from start_page.func.page2_slider import insert_id_animated
from start_page.func.page4_cards import page4_cards
from start_page.func.page5_green import page5_green
from start_page.func.page5_cards import func_page5_cards
from start_page.func.page6_session import page6_sessions_func
from start_page.func.page7_teacher import page7_teacher_func
from start_page.func.page8_cards import page8_cars_func
from start_page.func.page9_reviews import page9_reviews_func
from start_page.func.lead_page import lead_page_func
from start_page.func.quests_page import quest_func
from start_page.func.contacts_func import contacts_func
from start_page.func.lead_form_func import lead_form_func

from orders.models import Orders

from telegram.models import Links

from .ukassa import Ukassa


# Create your views here.

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def index(request):
    buttons = ButtonsHead.objects.first()

    settings = Settings.objects.first()

    page2 = Page2Title.objects.first()

    page2slider = Page2Slider.objects.all().order_by('id')
    page2slider = insert_id_animated(page2slider)

    advantage_list = Advantages.objects.all().order_by('id')
    advantage_list = page3_advantages(advantage_list)

    page4 = Page4Title.objects.first()

    page4_cars = Page4Cards.objects.all().order_by('id')
    page4_cars = page4_cards(page4_cars)

    page5 = Page5Title.objects.first()
    page5 = page5_green(page5)

    page5_cards = Page5Cards.objects.all().order_by('id')
    page5_cards = func_page5_cards(page5_cards)

    page6 = Page6Title.objects.first()

    sessions = Page6Session.objects.all().order_by('id')
    sessions = page6_sessions_func(sessions)

    teachers = Teachers.objects.all()
    teachers = page7_teacher_func(teachers)

    aboniment = AbonimentsTitle.objects.first()

    aboniment_list = AbonimentsCards.objects.all().order_by('id')

    aboniment_list = page8_cars_func(aboniment_list)

    reviews = Reviews.objects.all().order_by('id')
    reviews = page9_reviews_func(reviews)

    leads = LeadPage.objects.first()
    leads = lead_page_func(leads)

    quest = QuestsTitle.objects.first()

    quests_list = Quests.objects.all().order_by('id')
    quests_list = quest_func(quests_list)

    contacts = Contacts.objects.first()
    contacts = contacts_func(contacts)

    form_title = LeadFormTitle.objects.all()
    form_title = lead_form_func(form_title)

    free_form_title = FreeFormTitle.objects.first()

    context = {'settings': settings, 'buttons': buttons, 'page2': page2, 'slider': page2slider,
               'advantages': advantage_list, 'page4': page4, "page4_cars": page4_cars,
               'page5': page5, "page5_cards": page5_cards, "page6": page6, 'sessions': sessions,
               'teachers': teachers, 'aboniment': aboniment, 'aboniment_list': aboniment_list,
               'reviews': reviews, 'leads': leads, 'quest': quest, 'quests_list': quests_list,
               'contacts': contacts, 'form_title': form_title, 'form': OneFormOrders(),
               'free_form_title': free_form_title}

    response = render(request, 'start_page/index.html', context=context)

    return response


def thanks(request):
    # def thanks(request, name='', phone='', text=''):
    if request.method == "POST":
        form = OneFormOrders(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            telegram = form.cleaned_data['telegram']
            price = form.cleaned_data['price']
            source = form.cleaned_data['source']
            ip = request.META['REMOTE_ADDR']
            offer = form.cleaned_data['offer']
            buy_chat = form.cleaned_data['buy_chat']
            form_date = int(form.cleaned_data['dlina']) if form.cleaned_data['dlina'] else 1

            ###############Дата окончания действия ссылки############
            expire_date_orig = datetime.now() + timedelta(days=form_date)
            link = TelegramSendler().test_create(buy_chat, expire_date_orig)

            if not link:
                print(f'Не смог сформировать ссылку в телеграм')

            if price != '0':
                payment_link = Ukassa().create_payment(price, offer, link)
            else:
                payment_link = ''

            links_model = Links()
            links_model.link = link
            links_model.payment_link = payment_link
            links_model.buy_chat = buy_chat
            links_model.ower_license = expire_date_orig
            links_model.source = 'Сайт'
            links_model.save()

            orders_model = Orders()
            orders_model.offer = offer
            orders_model.link = link
            orders_model.name = name
            orders_model.phone = phone
            orders_model.telegram = telegram
            orders_model.price = price
            orders_model.source = source
            orders_model.ip = ip
            orders_model.buy_chat = buy_chat
            orders_model.save()

            TelegramSendler().new_orders(form.cleaned_data)

    context = {
        'name': name,
        'phone': phone,
        'link': link
    }

    if price == '0':
        return render(request, 'start_page/thanks.html', context=context)

    return redirect(payment_link)
    # return render(request, 'start_page/thanks.html', context=context)
