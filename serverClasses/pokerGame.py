from player import *
import uuid

class PokerGame:
    def __init__(self):
        self._gameID = str(uuid.uuid4())
        self._river = []
        self._players = []
        self._pot = 0
        self._deck = Deck()
        self._deck.shuffle()
    
    def initialDeal(self):
        for player in self._players:
            player.draw(self._deck,2)

    def endRound(self):
        for player in self._players:
            player.clearHand()
        self._river = []
        self._deck = Deck()
        self._deck.shuffle()

    @property
    def gameID(self):
        return self._gameID


if __name__ == '__main__':
    #Create 2 players


    #Have them play a game of poker while printing everything
    
    pass