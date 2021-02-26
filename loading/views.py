from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms
from board.models import Player
from django.views.generic import View

class NewTaskForm(forms.Form):
    name = forms.CharField(label = "Player Name")

class LoadGameView(View):
    def get(self,request,*args, **kwargs):
        if "names" not in request.session:
            request.session["names"] = []
        return render(request,'loading/index.html',{
            "names":request.session["names"],
            "form": NewTaskForm()
        })

    def post(self,request,*args, **kwargs):
        if request.method == "POST":
            form = NewTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            request.session["names"] += [name]
        else:
            return render(request, 'loading/index.html',{
                "form": form,
                "names":request.session["names"]
            })
        return render(request,'loading/start.html',{
            "form": NewTaskForm(),
            "names":request.session["names"]
        })
            

