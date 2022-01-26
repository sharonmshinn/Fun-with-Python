import random


def main():
    myDeck = Deck()
    myDeck.shuffle()
    myHands = []
    for i in range(10):
        myHands.append(PokerHand())
        myHands[-1].draw(myDeck,5)
    for hand in sorted(myHands, reverse=True):
        print(hand)
    
class Card:

    RANKS = (1,2,3,4,5,6,7,8,9,10,11,12,13)
    SUITS = ("Spades","Diamonds","Hearts","Clubs")

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self._rankStr()} of {self.suit}"

    def __repr__(self):
        return f"{self._rankRepr()} {self.suit[0]}"

    def _rankStr(self):
        if self.rank == 1:
            return "Ace"
        elif self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        else:
            return str(self.rank)
    def _rankRepr(self):
        if self.rank == 1:
            return "A"
        elif self.rank == 10:
            return "T"
        elif self.rank == 11:
            return "J"
        elif self.rank == 12:
            return "Q"
        elif self.rank == 13:
            return "K"
        else:
            return str(self.rank)

    def __lt__(self,other):
        return self.rank < other.rank

    def __ge__(self,other):
        return self.rank >= other.rank

    def __eq__(self,other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.rank == other.rank

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

class Deck:

    def __init__(self):
        self.cards = list()
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.cards.append(Card(rank,suit))

    def __str__(self):
        output = ""
        for card in self.cards:
            output += str(card)
            output += "\n"
        return output

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
        

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

class PokerHand:

    def __init__(self,deck):
        self.cards = []

    def draw(self,drawDeck,numCards=1):
        #for i in range(5):
            #theCard - drawDeck.draw()
            #if type(theCard) != type(None):
                #self.cards.append(theCard)
        while numCards > 0 and len(drawDeck) > 0:
            self.cards.append(drawDeck.draw())
            numCards -= 1

    def _isFlush(self):
        if len(int(self.cards) < 5):
            return False
        firstSuit = self.cards[0].getSuit()
        for card in self.cards[1:]:
            if card.getSuit() != firstSuit:
                return False
        return True

    def _isStraight(self):
        sortedHand = sorted(self.cards)
        for startRank in range(1, 9+1):
            straightFound = True
            i = 0
            while straightFound and i < 5:
                if sortedHand[i].getRank() != startRank + i:
                    straightFound = False
                i += 1
            if straightFound:
                return True
        if sortedHand[0].getRank() == 1:
            straightFound = True
            i = 0
            while straightFound and i < 4:
                sortedHand[i].getRank() != 9 + i:
                    straightFound = False
                i += 1
            if straightFound:
                return True
        return False

    def _ranksWithCount(self,count):
        cardRanks = [card.getRank() for card in self.cards]
        ranksFound = []
        for i in Card.RANKS:
            if cardRanks.count(i) == count:
                ranksFound.append(i)
        return ranksFound
                

    def _gradeHand(self):
        #8 Straight Flush
        if self._isStraight() and self._isFlush():
            return (8,)
        #7 Four-of-a-kind
        elif len(self._ranksWithCount(4)) == 1:
            return (7, self._ranksWithCount(4)[0])
        #6 Full House
        elif len(self._ranksWithCount(3)) == 1 and len(self._ranksWithCount(2)) == 1:
            return (6, self._ranksWithCount(3)[0], self.ranksWithCount(2)[0])
        #5 Flush
        elif self._isFlush():
            return (5,)
        #4 Straight
        elif self._isStraight():
            return (4,)
        #3 Three-of-a-kind
        elif len(self._ranksWithCount(3)) == 1:
            return (3, self._ranksWithCount(3)[0])
        #2 Two Pair
        elif len(self._ranksWithCount(2)) == 2:
            return (2, self._ranksWithCount(2)[1], self._ranksWithCount(2)[0])
        #1 Pair
        elif len(self._ranksWithCount(2)) == 1:
            return (1, self._ranksWithCount(2)[0])
        else:
            return (0,)

    def __str__(self):
        


    def __lt__(self,other):
        if self._gradeHand() < other.gradeHand():
            return True
        else:
            return sorted(self.cards, reverse=True) < sorted(other.cards, reverse=True)
        

if __name__ == "__main__":
    main()
        
