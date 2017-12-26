from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Exercise


class ExerciseDetail(DetailView):
    slug_field = "order"
    queryset=Exercise.objects.all()

class ProgDetail(DetailView):
    slug_field = "order"
    queryset=Exercise.objects.all()

class ExerciseList(ListView):
    queryset=Exercise.objects.all()
