#from django.shortcuts import render
from django.views.generic import ListView
from .models import Train
from .est_time import sbbtrip
from datetime import datetime, timedelta
from django.db.models import Avg

class DelayList(ListView):

    def get_queryset(self):
        next_trains = sbbtrip()
        next_train = next_trains["trip1"]["dep"]
        prev_trains = Train.objects.order_by("-betriebstag").filter(abfahrtszeit__contains=next_train.time())
        return prev_trains


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Call base implementation first to get a context

        # Load next trains
        context["trips"] = sbbtrip()
        next_train = context["trips"]["trip1"]["dep"]

        # Load history of relevant trains
        relevant_trains = Train.objects.all().filter(abfahrtszeit__contains=next_train.time())

        # Compute average delay
        avg_all = relevant_trains.aggregate(Avg('ab_delay'))
        try:
            avg_all = datetime.fromtimestamp(avg_all["ab_delay__avg"])
        except:
            avg_all = 0

        # Compute average delay for same day of the week
        avg_day = relevant_trains.filter(betriebstag__week_day=(next_train.weekday()+1) % 7 + 1).aggregate(Avg('ab_delay'))
        try:
            avg_day = datetime.fromtimestamp(avg_day["ab_delay__avg"])
        except:
            avg_day = 0

        # Prepare chart data
        # chart_day = next_train
        # i = 1
        #
        # while i < 7:
        #     chart_day = chart_day - timedelta(days=i)
        #     chart = relevant_trains.get(betriebstag=chart_day)
        #     i = i + 1

        # Save dictionary
        context["average"] = {"avg_day": avg_day, "avg_all": avg_all}
        # context["chart"] = {"chart": chart}

        return context
