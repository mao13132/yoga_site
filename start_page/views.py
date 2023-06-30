from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.http import require_GET

from .func.page3_advantages import page3_advantages
from .models import *

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

    page2slider = Page2Slider.objects.all()
    page2slider = insert_id_animated(page2slider)

    advantage_list = Advantages.objects.all()
    advantage_list = page3_advantages(advantage_list)

    page4 = Page4Title.objects.first()

    page4_cars = Page4Cards.objects.all()
    page4_cars = page4_cards(page4_cars)

    page5 = Page5Title.objects.first()
    page5 = page5_green(page5)

    page5_cards = Page5Cards.objects.all()
    page5_cards = func_page5_cards(page5_cards)

    page6 = Page6Title.objects.first()

    sessions = Page6Session.objects.all()
    sessions = page6_sessions_func(sessions)

    teachers = Teachers.objects.all()
    teachers = page7_teacher_func(teachers)

    aboniment = AbonimentsTitle.objects.first()

    aboniment_list = AbonimentsCards.objects.all()
    aboniment_list = page8_cars_func(aboniment_list)

    reviews = Reviews.objects.all()
    reviews = page9_reviews_func(reviews)

    leads = LeadPage.objects.first()
    leads = lead_page_func(leads)

    quest = QuestsTitle.objects.first()

    quests_list = Quests.objects.all()
    quests_list = quest_func(quests_list)


    contacts = Contacts.objects.first()
    contacts = contacts_func(contacts)


    context = {'settings': settings, 'buttons': buttons, 'page2': page2, 'slider': page2slider,
               'advantages': advantage_list, 'page4': page4, "page4_cars": page4_cars,
               'page5': page5, "page5_cards": page5_cards, "page6": page6, 'sessions': sessions,
               'teachers': teachers, 'aboniment': aboniment, 'aboniment_list': aboniment_list,
               'reviews': reviews, 'leads': leads, 'quest': quest, 'quests_list': quests_list,
               'contacts': contacts}

    response = render(request, 'start_page/index.html', context=context)

    return response


