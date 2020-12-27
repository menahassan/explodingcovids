from django.http import HttpResponse
from django.shortcuts import render

cards = ["covid exposure","mask/ppe","stay at home","superspreader",
"quarantine", "stimulus check","event cancellation","covid forecast",
"trump","fauci","NFL","pfizer","zoom"]

# Create your views here.
def index(request):
    return render(request, "board/index.html",{
        "cards": cards
    })
