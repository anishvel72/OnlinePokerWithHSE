from serverClasses.card import Card
from serverClasses.deck import Deck
import uuid

class PokerPlayer:
    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__money = 1000
        self.__id = str(uuid.uuid4())
    
    @property
    def id(self):
        return self.__id

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