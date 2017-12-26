from django.conf.urls import url
from django.urls import path
from django.views.generic import DetailView, ListView, RedirectView
from .views import ExerciseDetail, ExerciseList, ProgDetail

urlpatterns = [
    url(r'^$', ExerciseList.as_view(template_name = "fitness/index.html"), name="index"),
    url(r'^prog/$', RedirectView.as_view(pattern_name="index", permanent=False)),

    url(r'^(?P<pk>\d+)$', ExerciseDetail.as_view(template_name = "fitness/exercise.html")),
    url(r'^prog/(?P<pk>\d+)$', ProgDetail.as_view(template_name = "fitness/programme.html")),
]
