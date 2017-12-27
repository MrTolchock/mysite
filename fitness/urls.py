from django.conf.urls import url
from django.urls import path
from django.views.generic import DetailView, ListView, RedirectView
from .views import ExerciseDetail, ExerciseList, ProgDetail

urlpatterns = [
    # Index
    url(r'^$', ExerciseList.as_view(template_name = "fitness/index.html"), name="index"),

    # Excercises
    url(r'^(?P<slug>\d+)$', ExerciseDetail.as_view(template_name = "fitness/exercise.html")),

    # Programmes
    url(r'^prog/$', RedirectView.as_view(pattern_name="index", permanent=False)),
    url(r'^prog/(?P<slug>\d+)$', ProgDetail.as_view(template_name = "fitness/programme.html")),
]
