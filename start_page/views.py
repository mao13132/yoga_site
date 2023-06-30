from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.http import require_GET

from .func.page3_advantages import page3_advantages
from .models import Settings, ButtonsHead, Page2Title, Page2Slider, Advantages, Page4Title, Page4Cards, \
    Page5Title, Page5Cards

from start_page.func.page2_slider import insert_id_animated
from start_page.func.page4_cards import page4_cards
from start_page.func.page5_green import page5_green
from start_page.func.page5_cards import func_page5_cards

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

    context = {'settings': settings, 'buttons': buttons, 'page2': page2, 'slider': page2slider,
               'advantages': advantage_list, 'page4': page4, "page4_cars": page4_cars,
               'page5': page5, "page5_cards": page5_cards}

    response = render(request, 'start_page/index.html', context=context)

    return response


