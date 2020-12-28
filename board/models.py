from django.db import models
import random
import sys

class Card:

    def __init__(self,value=0,played=False):
        #Default constructor
        self.value = value
        self.played = played

    def getValue(self):
        return self.value
    
class Deck:
    cardTypes = {"covid exposure":4,"mask/ppe":6,"stay at home":5,"superspreader":4,
    "quarantine":4, "stimulus check":4,"event cancellation":4,"covid forecast":5,
    "trump":4,"fauci":4,"NFL":4,"pfizer":4,"zoom":4}
    def __init__(self):
        self.cards = []
        for key in self.cardTypes:
            for numCards in range(self.cardTypes[key]):
                card = Card(key,False)
                self.cards.append(card)
        self.shuffle()

    def add_card(self,card):
        self.cards.append(card)

    def remove_card(self,i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)
    
    #get properties of the deck
    def getDeckLength(self):
        return len(self.cards)
    
    def getCard(self,index):
        return self.cards[index]

    def listDeck(self):
        deckList = []
        for card in self.cards:
            deckList.append(card.getValue())
        return(deckList)

#can make this take a parameter of player
class Hand():
    def __init__(self,name=''):
        self.cards = []
        self.name = name

    def add_card(self,card):
        self.cards.append(card)

    def remove_card(self,i=-1):
        return self.cards.pop(i)

    def getCards(self):
        handList = []
        for card in self.cards:
            handList.append(card.getValue())
        return(handList)

    def getlabel(self):
        #when we create a Player, we can make name an attribute of player instead
        return self.name

