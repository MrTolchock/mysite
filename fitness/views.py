from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Exercise


class ExerciseDetail(DetailView):
    queryset=Exercise.objects.all()

class ProgDetail(DetailView):
    queryset=Exercise.objects.all()

    # def get_object(self):
    #     return get_object_or_404(User, pk=request.session['user_id'])


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) #Call base implementation first to get a context
    #
    #     # Define next exercise
    #     context["order"] = {"next": 2, "previous": 3}
    #
    #     return context

class ExerciseList(ListView):
    queryset=Exercise.objects.all()
