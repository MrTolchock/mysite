from django.shortcuts import render
from .est_time_dj3 import sbbtrip

def index(request):
    return render(request, "sbbdelay3/index.html", {"trips":sbbtrip()})
