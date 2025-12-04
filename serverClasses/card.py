class Card:
    possible_suites = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
    reference = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    
    __covered_value = 14
    __covered_suit = "Covered"


    def __init__(self, value, suite, covered=True):
        self.__value = value
        self.__suite = suite
        self.__covered = covered
    

    @property
    def value(self):
        if self.__covered:
            return Card.__covered_value
        return self.__value
    

    @property
    def suite(self):
        if self.__covered:
            return Card.__covered_suit
        
        return self.__suite