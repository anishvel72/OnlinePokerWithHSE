class Card:
    possible_suites = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
    def __init__(self, value, suite, covered=True):
        self.__value == value
        self.__suite == suite
        self.__covered == covered
    
    reference = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}