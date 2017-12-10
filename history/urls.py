from django.conf.urls import url
from django.urls import path
from django.views.generic import ListView
from history.views import HistoryList


urlpatterns = [
    path("", HistoryList.as_view()),
]
