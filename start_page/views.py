from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.http import require_GET

from .func.page3_advantages import page3_advantages
from .models import Settings, ButtonsHead, Page2Title, Page2Slider, Advantages

from start_page.func.page2_slider import insert_id_animated

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

    context = {'settings': settings, 'buttons': buttons, 'page2': page2, 'slider': page2slider,
               'advantages': advantage_list}

    response = render(request, 'start_page/index.html', context=context)

    return response


