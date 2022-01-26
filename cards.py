
import random

def main():
    myDeck = Deck()
    myDeck.shuffle()
    myHands = []
    for i in range(10):
        myHands.append(PokerHand())
        myHands[-1].draw(myDeck,5)
    for hand in sorted(myHands,reverse=True):
        print(hand)

class Card:

    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    SUITS = ("Spades","Diamonds","Hearts","Clubs")

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self._rankStr()} of {self.suit}"

    def __repr__(self):
        return f"{self._rankRepr()}{self.suit[0]}"

    def _rankStr(self):
        if self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        elif self.rank == 14:
            return "Ace"
        else:
            return str(self.rank)

    def _rankRepr(self):
        if self.rank == 10:
            return "T"
        elif self.rank == 11:
            return "J"
        elif self.rank == 12:
            return "Q"
        elif self.rank == 13:
            return "K"
        elif self.rank == 14:
            return "A"
        else:
            return str(self.rank)

    def __lt__(self,other):
        return self.rank < other.rank

    def __ge__(self,other):
        return self.rank >= other.rank

    def __eq__(self,other):
        if type(self) != type(other):
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
        output = "Deck["
        output += ",".join(self.cards)
        output += "]"
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

    def __init__(self):
        self.cards = []

    def draw(self,drawDeck,numCards=1):
        while numCards > 0 and len(drawDeck) > 0:
            self.cards.append(drawDeck.draw())
            numCards -= 1
        self.cards.sort(reverse=True)

    def _isFlush(self):
        if len(self.cards) < 5:
            return False
        firstSuit = self.cards[0].getSuit()
        for card in self.cards[1:]:
            if card.getSuit() != firstSuit:
                return False
        return True

    def _isStraight(self):
        # look specifically for an ace-high straight
        if self.cards[0].getRank() == 14 \
                and self.cards[1].getRank() == 2 \
                and self.cards[2].getRank() == 3 \
                and self.cards[3].getRank() == 4 \
                and self.cards[4].getRank() == 5:
            return True
        # now use a loop to look for every other type of straight
        for startRank in range(13,5):
            straightFound = True
            i = 0
            while straightFound and i < 5:
                if self.cards[i].getRank() != startRank-i:
                    straightFound = False
                i += 1
            if straightFound:
                return True
        # if we've reached this point, we have check for and failed to find every specific straight that exists
        return False

    def _ranksWithCount(self,count):
        cardRanks = [card.getRank() for card in self.cards]
        ranksFound = []
        for i in Card.RANKS:
            if cardRanks.count(i) == count:
                ranksFound.append(i)
        return ranksFound

    def _gradeHand(self,returnString=False):
        # 8 Straight Flush
        if self._isStraight() and self._isFlush():
            return (8,)
        # 7 Four-of-a-kind
        elif len(self._ranksWithCount(4)) == 1:
            return (7,self._ranksWithCount(4)[0])
        # 6 Full House
        elif len(self._ranksWithCount(3)) == 1 and len(self._ranksWithCount(2)) == 1:
            return (6,self._ranksWithCount(3)[0],self._ranksWithCount(2)[0])
        # 5 Flush
        elif self._isFlush():
            return (5,)
        # 4 Straight
        elif self._isStraight():
            return (4,)
        # 3 Three-of-a-kind
        elif len(self._ranksWithCount(3)) == 1:
            return (3,self._ranksWithCount(3)[0])
        # 2 Two pair
        elif len(self._ranksWithCount(2)) == 2:
            return (2,self._ranksWithCount(2)[1],self._ranksWithCount(2)[0])
        # 1 Pair
        elif len(self._ranksWithCount(2)) == 1:
            return (1,self._ranksWithCount(2)[0])
        else:
            return (0,)

    def __str__(self):
        return f"Hand[{','.join([x.__repr__() for x in sorted(self.cards,reverse=True)])}] {self._gradeHand()}"

    def __lt__(self,other):
        return [self._gradeHand()] + sorted(self.cards,reverse=True) < [other._gradeHand()] + sorted(other.cards,reverse=True)
    
if __name__ == "__main__":
    main()
