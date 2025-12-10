class Card:
    possible_suites = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
    reference = {14: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    #change
    __covered_value = 15
    __covered_suit = "Covered"

    @classmethod
    def coveredValue(self):
        return self.__covered_value
    
    @classmethod
    def coveredSuit(self):
        return self.__covered_suit
    

    def __init__(self, value, suite, covered=True):
        self.__value = value
        self.__suite = suite
        self.__covered = covered
    

    @property
    def value(self):
        return self.__value
    

    @property
    def suite(self):
        return self.__suite
    
    def reveal(self):
        self.__covered = False

    def isCovered(self):
        return self.__covered
    

    def __str__(self):
        
        representation = ''
        if self.__covered:
            representation =  "Covered"
        name = Card.reference.get(self.__value, str(self.__value))
        representation += f"{name} of {self.__suite}"
        return representation

    def __repr__(self):
        return self.__str__()