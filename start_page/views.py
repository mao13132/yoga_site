from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.http import require_GET

from .models import Settings, ButtonsHead, Page2Title

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

    context = {'settings': settings, 'buttons': buttons, 'page2': page2}

    response = render(request, 'start_page/index.html', context=context)

    return response


