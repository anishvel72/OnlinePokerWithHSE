from card import Card
from deck import Deck

class PokerPlayer:
    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__money = 1000
    
    @property
    def name(self):
        return self.__name
    
    def changeMoney(self, n):
        self.__money += n

    @property
    def hand(self):
        return self.__hand
    
    def draw(self, deck, numCards=1):
        
        
        for i in range(numCards):
            newCard = deck.draw()
            self.__hand.append(newCard)

    def clearHand(self):
        self.__hand = []

    def action(self, act, game):
        return act