from serverClasses.player import *
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
        self.__started = False
    
    def startGame(self):
        for player in self.__playerQueue:
            self.__players.append(player)
        self.__playerQueue = []
        for player in self.__players:
            player.draw(self.__deck,2)
        self.__started = True

    def fold(self, player):
        self.__players.remove(player)
        self.__playerQueue.append(player)
    
    @property
    def started(self):
        return self.__started
    
    def riverDraw(self):
        self.__river.append(self.__deck.draw())

    def endRound(self):
        for player in self.__players:
            player.clearHand()
        self.__river = []
        self.__deck = Deck()
        self.__deck.shuffle()
        self.__started = False
    
    @property
    def players(self):
        return self.__players

    def checkWinner(self):


        #Scoring Mechanism (A base10 number representation using Base15 math. If the number was Base15, the first number is rank, 2nd number is rank within rank, and 3rd card is high card overall)
        # 9 for Straight-Flush, 8 for 4 of a kind, 7 for Full House, 6 for plain Flush, 5 for plain straight, 4 for 3 of a kind, 3 for 2 pair, 2 for single pair, 1 for if the player could only win by high card 
        playerScores = {}
        scoreValues = []
        
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
            player.hand.sort(key = getVal, reverse=True)
            cards.append(self.__river[0])
            cards.append(self.__river[1])
            
            cards.sort(key = getVal, reverse=True)

            values, suites = dictionaries(cards)


            


            score = 0

            def isStraight(cards):
                #We can assume the cards are sorted because we did that earlier

                #Make new list without duplicates
                checkerList = []

                for i in range(len(cards)):
                    if cards[i].value != cards[i-1].value:
                        checkerList.append(cards[i])
                

                #Check Streak

                streak = 1
                for i in range(1, len(checkerList)):
                    if checkerList[i % len(checkerList)].value == checkerList[(i -1)% len(checkerList)].value -1:
                        streak +=1
                        if streak == 5:
                            return True
                    else:
                        #reset streak back to 1
                        streak = 1
                return False


            def hasValue(dictionary, target):
                for key, value in dictionary.items():
                    if value == target:
                        return True
                return False
            
            #Check for Flush (check for straight within it as well)
            if (hasValue(suites, 5)):
                potential_straight = []
                for key, value in suites.items():
                    if value ==5:
                        flushSuite = key
                for card in cards:
                    if card.suite == flushSuite:
                        potential_straight.append(card)

                if isStraight(cards):
                    #straight flush
                    score = 9 * (15 ** 3)                    
                else:
                    score = 6 * (15 ** 3)
                score += (potential_straight[0].value * (15 ** 2))
                score += player.hand[0].value

                playerScores[player.id] = score
                scoreValues.append(score)
                continue
                
            
                
            #Check for 4 of a kind using values dictionary
            if hasValue(values, 4):
                for key, value in values.items():
                    if value == 4:
                        fourKind = key
                score = 8 * (15 ** 3)
                score += fourKind * (15 ** 2)
                score += player.hand[0].value
                playerScores[player.id] = score
                scoreValues.append(score)
                continue
            

            
                    

                        


            #Check for Full House and 3 of a Kind using values dictionary
            if hasValue(values, 3):
                cpValues = values.copy()
                for key, value in cpValues.items():
                    if value == 3:
                        threeKind = key
                
                del cpValues[threeKind]

                if hasValue(cpValues, 3) or hasValue(cpValues, 2):
                    for key, value in cpValues.items():
                        if value > 2:
                            s2ndValue = key
                    score = 7 * (15 ** 3)
                    print(threeKind)
                    score += max(threeKind, s2ndValue) * (15 ** 2)
                    score += player.hand[0].value
                    
                else:
                    score = 4 * (15 ** 3)
                    score += threeKind * (15 ** 2)
                    score += player.hand[0].value
                playerScores[player.id] = score
                scoreValues.append(score)
                continue
            


            #Pure straight
            if isStraight(cards):
                
                checkerList = []

                for i in range(len(cards)):
                    if cards[i].value != cards[i-1].value:
                        checkerList.append(cards[i])
                


                streak = 1
                startCard = checkerList[0]
                for i in range(1, len(checkerList)):
                    if checkerList[i % len(checkerList)].value == checkerList[(i -1)% len(checkerList)].value -1:
                        streak +=1
                        if streak == 5:
                            break
                    else:
                        streak = 1
                        startCard = checkerList[i]
                
                score = 5 * (15 ** 3)
                score += startCard * (15 ** 2)
                score += player.hand[0].value
                playerScores[player.id] = score
                scoreValues.append(score)
                continue

            #1 and 2 pair (slightly fails when there are more than two pairs)
            if hasValue(values, 2):
                cpValues = values.copy()
                
                for key, value in values.items():
                    if value == 2:
                        pairValue = key
                
                del cpValues[pairValue]

                if hasValue(cpValues, 2):
                    for key, value in cpValues.items():
                        if value == 2:
                            pair2ndValue = key
                    

                    score = 3 * (15 ** 3)
                    score += max(pairValue, pair2ndValue) * (15 ** 2)
                    score += player.hand[0].value
                else:
                    score = 2 * (15 ** 3)
                    score += pairValue * (15 ** 2)
                    score += player.hand[0].value
                playerScores[player.id] = score
                scoreValues.append(score)
                continue

            score = 15 ** 3
            score += player.hand[0].value * (15 ** 2)
            score += player.hand[0].value

        maxScore = max(scoreValues)
        winners = []
        
        for id, score in playerScores.items():
            if playerScores[id] == maxScore:
                winners.append(id)
        return winners



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




if __name__ == "__main__":
    game = PokerGame()

    # Create players
    p1 = PokerPlayer("Player 1")
    p2 = PokerPlayer("Player 2")
    p3 = PokerPlayer("Player 3")

    # Add players to queue
    game.addPlayer(p1)
    game.addPlayer(p2)
    game.addPlayer(p3)

    print("Starting game", game.gameID)
    game.startGame()

    print("\nPlayer hands after deal:")
    for player in game._PokerGame__players:
        for card in player.hand:
            card.reveal()
        print(player.name, [str(card) for card in player.hand])

    print("\nDrawing first three river cards")
    for _ in range(3):
        game.riverDraw()
    for card in game._PokerGame__river:
        card.reveal()
    print("River:", [str(c) for c in game._PokerGame__river])

    print("\nDrawing turn card")
    game.riverDraw()
    game._PokerGame__river[-1].reveal()
    print("River:", [str(c) for c in game._PokerGame__river])

    print("\nDrawing final river card")
    game.riverDraw()
    game._PokerGame__river[-1].reveal()
    print("River:", [str(c) for c in game._PokerGame__river])

    print("\nEvaluating winner")
    winners = game.checkWinner()

    def getPlayerbyId(id):
        for player in game.players:
            if player.id == id:
                return player
    
    if not winners:
        print("No winner returned. Check the scoring dictionary assignments.")
    else:
        print("Winner list:")
        for winner in winners:
            print(getPlayerbyId(winner).name)

    print("\nPot demo")
    game.changePot(50)
    print("Pot:", game.pot)

    print("\nEnding round")
    game.endRound()
    print("Hands after clearing:", [player.hand for player in game._PokerGame__players])
    print("River after clearing:", game._PokerGame__river)
    print("Pot:", game.pot)
