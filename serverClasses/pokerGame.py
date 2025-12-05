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
    
    def checkWinner(self):
        pass

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
    game = PokerGame()

    # Create players
    p1 = PokerPlayer("Player 1")
    p2 = PokerPlayer("Player 2")

    # Add players to queue
    game.addPlayer(p1)
    game.addPlayer(p2)

    # Start the game
    print("Starting game", game.gameID)
    game.startGame()

    # Show each player's starting hand
    print("Player hands after deal:")
    for player in game._PokerGame__players:
        for card in player.hand:
            card.reveal()
        print(player.name, player.hand)


    print('\n\n')
    # Draw three river cards
    print("Drawing first three river cards")
    for _ in range(3):
        game.riverDraw()
    for card in game._PokerGame__river:
        card.reveal()
    print("River:", game._PokerGame__river)



    print('\n\n')
    # Draw turn card
    print("Drawing turn card")
    game.riverDraw()
    game._PokerGame__river[-1].reveal()
    print("River:", game._PokerGame__river)


    print('\n\n')
    # Draw river card
    print("Drawing final river card")
    game.riverDraw()
    game._PokerGame__river[-1].reveal()
    print("River:", game._PokerGame__river)

    # Change pot for demo
    print("Adding 50 to the pot")
    game.changePot(50)
    print("Pot:", game.pot)

    # End the round
    print("Ending round")
    game.endRound()
    print("Players hands:", [player.hand for player in game._PokerGame__players])
    print("River:", game._PokerGame__river)
    print("Pot:", game.pot)
