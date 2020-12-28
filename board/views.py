from django.http import HttpResponse
from django.shortcuts import render
from board.models import Deck
from board.models import Hand
from django.views.generic import View

class CreateGameView(View):
    #template_name = 'board/index.html'
    def get(self,request,*args, **kwargs):
        deck = Deck()
        hand = Hand()
        for i in range(7):
            hand.add_card(deck.remove_card())
        handCards = hand.getCards()

        deckLen = deck.getDeckLength()
        deckList = deck.listDeck()
        return render(request,'board/index.html',{
            "deckLen":deckLen,
            "deckList":deckList,
            "handCards":handCards
        })
