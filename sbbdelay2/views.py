from django.shortcuts import render
from .est_time_dj2 import sbbtrip

def index(request):
    return render(request, "sbbdelay2/index.html", {"trips":sbbtrip()})
