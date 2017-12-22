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
        return Train.objects.order_by("-betriebstag").filter(abfahrtszeit__contains=next_train.time())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Call base implementation first to get a context
        context["trips"] = sbbtrip()
        next_train = context["trips"]["trip1"]["dep"]
        avg_all = Train.objects.all().filter(abfahrtszeit__contains=next_train.time()).aggregate(Avg('ab_delay'))
        context["average"] = avg_all

        avg_day = Train.objects.all().filter(abfahrtszeit__contains=next_train.time()).filter(betriebstag__week_day=5).aggregate(Avg('ab_delay'))
        avg_day = datetime.fromtimestamp(avg_day['ab_delay__avg'])#.strftime('%M:%S')
        context["aver"] = {"avg_day": avg_day}

        return context
