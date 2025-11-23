from card import Card
from deck import Deck

class PokerPlayer:
    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__money = 0
    
    @property
    def name(self):
        return self.__name
    
    def addMoney(self, n):
        self.__money += n


    @property
    def hand(self):
        return self.__hand
    
    def addToHand(self, deck):
        newCard = deck.draw()
        self.__hand.append(newCard)

    def clearHand(self):
        self.__hand = []