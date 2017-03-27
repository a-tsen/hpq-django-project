from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /collection/
    url(r'^$', views.collection_index, name='index'),
    # ex: /collection/necklaces/
    url(r'^(?P<item_type>[a-z]+)/$', views.item_category, name='item_category'),
]
