from django.http import HttpResponse
from django.shortcuts import render
#from board.models import Deck
#from board.models import Hand
from board.models import Player
#from board.models import DiscardPile
from django.views.generic import View
from .forms import NameForm

class LoadGameView(View):
    #template_name = 'board/index.html'
    def get(self,request,*args, **kwargs):
        player1 = Player(True,"Bob")
        player1Name = player1.getName()
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('board/index')

            # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()
        return render(request,'loading/index.html',{
            "player1Name":player1Name,
            "form": form
        })

