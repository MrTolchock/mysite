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

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         prog_first = Exercise.objects.filter(in_prog=True).first()
         context['first'] = {"prog_first": prog_first.order}
         return context
