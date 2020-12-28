from django.http import HttpResponse
from django.shortcuts import render
from board.models import Deck
from django.views.generic import View

class CreateGameView(View):
    #template_name = 'board/index.html'
    def get(self,request,*args, **kwargs):
        deck = Deck()
        deckLen = deck.getDeckLength()
        deckList = deck.listDeck()
        return render(request,'board/index.html',{
            "deckLen":deckLen,
            "deckList":deckList
        })
