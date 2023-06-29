from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.http import require_GET

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
    context = {'test': False}
    response = render(request, 'start_page/index.html', context=context)

    return response


