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


        #Scoring Mechanism (A base10 number representation using Base15 math. If the number was Base15, the first number is rank, 2nd number is rank within rank, and 3rd card is high card overall)
        # 9 for Straight-Flush, 8 for 4 of a kind, 7 for Full House, 6 for plain Flush, 5 for plain straight, 4 for 3 of a kind, 3 for 2 pair, 2 for single pair, 1 for if the player could only win by high card 
        playerScores = {}
        
        def getVal(card):
            return card.value
        

        def dictionaries(cards):
            suites = {'Diamonds' : 0, 'Clubs': 0, 'Spades':0, 'Hearts':0}
            values = {2: 0, 3: 0, 4: 0, 5: 0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
            for card in cards:
                values[card.value] += 1
                suites[card.suite] += 1
            return values, suites
        

        
        for player in self.__players:
            cards = player.hand.copy()
            cards.append(self.__river[0])
            cards.append(self.__river[1])
            
            cards.sort(key = getVal, reverse=True)

            suites, values = dictionaries(cards)


            


            score = 0

            def isStraight(cards):
                #We can assume the cards are sorted because we did that earlier

                #Make new list without duplicates
                checkerList = []

                for i in range(len(cards)):
                    if cards[i] != cards[i-1]:
                        checkerList.append(cards[i])
                

                streak = 1
                for i in range(1, len(checkerList)):
                    if checkerList[i % len(checkerList)] == checkerList[(i -1)% len(checkerList)] -1:
                        streak +=1
                        if streak == 5:
                            return True
                    else:
                        #reset streak back to 1
                        streak = 1
                return False


                

            #Check for Flush (check for straight within it as well)


            if (suites['Diamonds'] == 5 or suites['Clubs'] == 5 or suites['Spades'] == 5 or suites['Hearts'] == 5):
                potential_straight = []
                for key, value in cards.items():
                    if value ==5:
                        x = key
                for card in cards:
                    if card.suite == x:
                        potential_straight.append(card)

                if isStraight(cards):
                    #striaght flush
                    score = 9 * (15 ** 3)
                else:
                    score = 6 * (15 ** 3)
            
                
            #Check for 4 of a kind using values dictionary
                


        pass


    #Helper Functions that I Will use in checkWinner():


    def get_ranks(cards):
        pass

    def get_suits(cards):
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
    for i in range(3):
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
