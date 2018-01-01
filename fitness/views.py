from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Exercise
from django.db.models import Sum


class ExerciseDetail(DetailView):
    slug_field = "order"
    queryset=Exercise.objects.all()


class ProgDetail(DetailView):
    slug_field = "order"
    queryset=Exercise.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Count exercises in programme
        prog_count = Exercise.objects.filter(in_prog=True).count()
        prog_all = Exercise.objects.filter(in_prog=True).aggregate(Sum('repetitions'))

        # Save context dictionary
        context['context'] = {"prog_all": prog_all["repetitions__sum"]}
        return context


class ExerciseList(ListView):
    queryset=Exercise.objects.all()

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)

         # Get first exercise of programme
         prog_first = Exercise.objects.filter(in_prog=True).first()

         # Save context dictionary
         context['context'] = {"prog_first": prog_first.order}
         return context
