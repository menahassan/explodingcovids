from django.http import HttpResponse
from django.shortcuts import render
#from board.models import Deck
#from board.models import Hand
from board.models import Player
#from board.models import DiscardPile
from django.views.generic import View

class LoadGameView(View):
    #template_name = 'board/index.html'
    def get(self,request,*args, **kwargs):
        player1 = Player(True,"Bob")
        player1Name = player1.getName()
        return render(request,'loading/index.html',{
            "player1Name":player1Name
        })

