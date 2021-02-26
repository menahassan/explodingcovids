from django.http import HttpResponse
from django.shortcuts import render
from board.models import Deck
from board.models import Hand
from board.models import Player
from board.models import DiscardPile
from django.views.generic import View

class CreateGameView(View):
    #template_name = 'board/index.html'
    def get(self,request,*args, **kwargs):
        players = []
        deck = Deck()
        discardPile = DiscardPile()
        names = request.session.get('names')
        count = 0
        for name in names:
            if(count == 0):
                turn = True
            else:
                turn = False
            hand = Hand()
            for i in range(7):
                hand.add_card(deck.remove_card())
            player = Player(turn,name,hand)
            #for now, just send data as a list
            players.append([turn,name,hand.getCards()])
        
        deckLen = deck.getDeckLength()
        deckList = deck.listDeck()
        return render(request,'board/index.html',{
            "deckLen":deckLen,
            "deckList":deckList,
            "players":players
        })
