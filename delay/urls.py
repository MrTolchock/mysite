from django.conf.urls import url
from django.urls import path
from django.views.generic import ListView
from .views import DelayList


urlpatterns = [
    path("", DelayList.as_view()),
]
