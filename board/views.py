from django.http import HttpResponse
from django.shortcuts import render
from board.models import Deck
from board.models import Hand
from board.models import Player
from board.models import DiscardDeck
from django.views.generic import View

class CreateGameView(View):
    #template_name = 'board/index.html'
    def get(self,request,*args, **kwargs):
        deck = Deck()
        discardDeck = DiscardDeck()
        player1 = Player("Bob",True)
        hand1 = player1.getHand()
        player1Name = player1.getName()

        for i in range(7):
            hand1.add_card(deck.remove_card())
        handCards = hand1.getCards()

        deckLen = deck.getDeckLength()
        deckList = deck.listDeck()
        return render(request,'board/index.html',{
            "deckLen":deckLen,
            "deckList":deckList,
            "handCards":handCards,
            "player1Name":player1Name
        })
