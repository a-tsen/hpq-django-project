from django.http import HttpResponse
from django.template import loader

from .models import About


def index(request):
    about_paragraph = About.objects.all()[0].paragraph
    template = loader.get_template('about/about.html')
    context = {
        'about_paragraph': about_paragraph
    }
    return HttpResponse(template.render(context, request))
