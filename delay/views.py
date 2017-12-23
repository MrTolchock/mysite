#from django.shortcuts import render
from django.views.generic import ListView
from .models import Train
from .est_time import sbbtrip
from datetime import datetime
from django.db.models import Avg

class DelayList(ListView):
    template_name = "delay/index.html"

    def get_queryset(self):
        next_trains = sbbtrip()
        next_train = next_trains["trip1"]["dep"]
        prev_trains = Train.objects.order_by("-betriebstag").filter(abfahrtszeit__contains=next_train.time())
        return prev_trains


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Call base implementation first to get a context
        context["trips"] = sbbtrip()
        next_train = context["trips"]["trip1"]["dep"]

        # Average delay
        avg_all = Train.objects.all().filter(abfahrtszeit__contains=next_train.time()).aggregate(Avg('ab_delay'))
        try:
            avg_all = datetime.fromtimestamp(avg_all["ab_delay__avg"])
        except:
            avg_all = 0

        # Average delay for same day of the week
        avg_day = Train.objects.all().filter(abfahrtszeit__contains=next_train.time()).filter(betriebstag__week_day=next_train.weekday()+2).aggregate(Avg('ab_delay'))
        try:
            avg_day = datetime.fromtimestamp(avg_day["ab_delay__avg"])
        except:
            avg_day = 0

        # Save dictionary
        context["average"] = {"avg_day": avg_day, "avg_all": avg_all}

        return context
