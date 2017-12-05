from django.shortcuts import render
from .est_time_dj import sbbtrip

def index(request):
    return render(request, "sbbdelay/index.html", {"trips":sbbtrip()})
