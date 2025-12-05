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
        return self.__value
    

    @property
    def suite(self):
        if self.__covered:
            return Card.__covered_suit
        
        return self.__suite
    
    def reveal(self):
        self.__covered = False

    def isCovered(self):
        return self.__covered
    

    def __str__(self):
        if self.__covered:
            return "Covered"
        name = Card.reference.get(self.__value, str(self.__value))
        return f"{name} of {self.__suite}"

    def __repr__(self):
        return self.__str__()