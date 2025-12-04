from player import *
import uuid

class PokerGame:
    def __init__(self):
        self.__gameID = str(uuid.uuid4())
        self.__river = []
        self.__players = []
        self.__pot = 0
        self.__deck = Deck()
        self.__deck.shuffle()
        self.__playerQueue = []
    
    def startGame(self):
        for player in self.__playerQueue:
            self.__players.append(player)
        self.__playerQueue = []
        for player in self.__players:
            player.draw(self.__deck,2)

    def riverDraw(self):
        self.__river.append(self.__deck.draw())

    def endRound(self):
        for player in self.__players:
            player.clearHand()
        self.__river = []
        self.__deck = Deck()
        self.__deck.shuffle()

    def addPlayer(self, player):
        self.__playerQueue.append(player)
    @property
    def gameID(self):
        return self.__gameID
    
    @property
    def pot(self):
        return self.__pot
    
    def changePot(self, n):
        self.__pot += n


if __name__ == '__main__':
    #Create 2 players


    #Have them play a game of poker while printing everything
    
    pass