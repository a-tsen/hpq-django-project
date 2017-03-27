from django.http import HttpResponse
from django.template import loader

from .models import Item


def collection_index(request):  # displays all items
    item_list = Item.objects.order_by('-pk')  # first page of items
    template = loader.get_template('collection/collection.html')
    context = {
        'item_list': item_list,
        'item_type': "All"
    }
    return HttpResponse(template.render(context, request))


def item_category(request, item_type):  # displays items for a given item class
    item_list = Item.objects.filter(item_type=item_type).order_by('-pk')
    template = loader.get_template('collection/collection.html')
    context = {
        'item_list': item_list,
        'item_type': item_type
    }
    return HttpResponse(template.render(context, request))

