from card import Card
import random


class Deck:
    def __init__(self):
        self.__deck = []
        for suite in Card.possible_suites:
            for i in range(2, 15):
                self.__deck.append(Card(i, suite))
    def shuffle(self):
        random.shuffle(self.__deck)
    
    def draw(self):
        top_card = self.__deck.pop()
        return top_card
