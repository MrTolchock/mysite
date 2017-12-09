from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from history.models import Train

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', ListView.as_view(queryset=Train.objects.all().order_by("ankunftszeit"), template_name="history/index.html")),
]
