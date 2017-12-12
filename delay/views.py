#from django.shortcuts import render
from django.views.generic import ListView
from .models import Train
from .est_time import sbbtrip
from datetime import datetime

class DelayList(ListView):
    template_name = "delay/index.html"

    def get_queryset(self):
        next_trains = sbbtrip()
        next_train = next_trains["trip1"]["dep"]
        return Train.objects.order_by("-betriebstag").filter(abfahrtszeit__contains=next_train.time())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["trips"] = sbbtrip()
        return context
