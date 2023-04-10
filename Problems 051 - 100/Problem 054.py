#-------------------------------------------------------------------------------
# Name:        Problem 054 - Poker Hands
#
# Links:       http://projecteuler.net/problem=54
#              http://www.wheelingisland.com/Compare-Poker-Hands.aspx
#              http://www.pokerhands.com/poker_hand_tie_rules.html
#
# Notes:       Doesn't support wheel straights (A, 2, 3, 4, 5)
#
# TODO:
#-------------------------------------------------------------------------------

from collections import Counter

RankValue = { '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
              '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14 }

RankName = { '2' : "Two", '3' : "Three", '4' : "Four", '5' : "Five", '6' : "Six",
             '7' : "Seven", '8' : "Eight", '9' : "Nine", 'T' : "Ten", 'J' : "Jack",
             'Q' : "Queen", 'K' : "King", 'A' : "Ace"  }

Suit = { 'H' : "Hearts", 'D' : "Diamonds", 'C' : "Clubs", 'S' : "Spades" }

class HandRanking:
    HighCard = 0
    OnePair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    Straight = 4
    Flush = 5
    FullHouse = 6
    FourOfAKind = 7
    StraightFlush = 8
    RoyalFlush = 9

class Card:
    """ A class containg a rank and a suit for a playing card """
    def __init__(self, cardStr):
        l = list(cardStr)
        self.rank = l[0]
        self.suit = l[1]

    def Fullname(self):
        return "%s of %s" % (RankName[self.rank], Suit[self.suit ])

    def __repr__(self):
        return "Card(%s%s)" % (self.rank, self.suit )

    def __str__(self):
        return "%s%s" % (self.rank, self.suit )

class Hand:
    """ A poker hand consists of 5 cards """
    def __init__(self, handStr):
        l = handStr.split()
        self.cards = [Card(x) for x in l]
        self.scoreRanking, self.orderedValues = self.Score()

    def __repr__(self):
        return "Hand(%s %s %s %s %s)" % (tuple(self.cards))

    def __str__(self):
        return "%s %s %s %s %s" % (tuple(self.cards))

    # For ease of use
    def __iter__(self):
        for card in self.cards:
            yield card

    def Score(self):
        ranks = sorted([RankValue[card.rank] for card in self.cards], reverse=True)

        # Search for same suits first
        sameSuit = True
        firstSuit = self.cards[0].suit
        for card in self.cards[1:]:
            if firstSuit != card.suit:
                sameSuit = False
                break

        # Check for the 3 flushes
        if sameSuit:
            # Royal flush
            royalFlush = [14, 13, 12, 11, 10]
            if ranks == royalFlush:
                return HandRanking.RoyalFlush, royalFlush

            # Straight flush
            highest = ranks[0]
            if highest - 4 >= RankValue['2']:
                straight = [highest, highest-1, highest-2, highest-3, highest-4]
                if ranks == straight:
                    return HandRanking.StraightFlush, straight

            # Flush
            return HandRanking.Flush, ranks

        # Check for the other hands
        c = Counter(ranks)
        topTwo = c.most_common(2) # Maximum of same cards for winning hands

        # l[0][0] is the most common value, l[0][1] is it's count

        # Four of a kind
        if topTwo[0][1] == 4:
            foak = [topTwo[0][0] for i in range(4)]
            kicker = [x for x in ranks if x != topTwo[0][0]]
            return HandRanking.FourOfAKind, foak + kicker

        # Full house
        if topTwo[0][1] == 3 and topTwo[1][1] == 2:
            part1 = [topTwo[0][0] for i in range(3)]
            part2 = [topTwo[1][0] for i in range(2)]
            return HandRanking.FullHouse, part1 + part2

        # Straight
        highest = ranks[0]
        if highest - 4 >= RankValue['2']:
            straight = [highest, highest-1, highest-2, highest-3, highest-4]
            if ranks == straight:
                return HandRanking.Straight, straight

        # Three of a kind
        if topTwo[0][1] == 3:
            toak = [topTwo[0][0] for i in range(3)]
            kickers = [x for x in ranks if x != topTwo[0][0]]
            return HandRanking.ThreeOfAKind, toak + kickers

        # Two pair
        if topTwo[0][1] == 2 and topTwo[1][1] == 2:
            pair1 = [topTwo[0][0] for i in range(2)]
            pair2 = [topTwo[1][0] for i in range(2)]
            kicker = [x for x in ranks if x != topTwo[0][0] and x != topTwo[1][0]]
            return HandRanking.TwoPair, pair1 + pair2 + kicker

        # One pair
        if topTwo[0][1] == 2:
            pair = [topTwo[0][0] for i in range(2)]
            kickers = [x for x in ranks if x != topTwo[0][0]]
            return HandRanking.OnePair, pair + kickers

        # Always have a high card
        return HandRanking.HighCard, ranks

def Tiebreaker(hand1, hand2):
    for i in range(5):
        a, b = hand1.orderedValues[i], hand2.orderedValues[i]
        if a == b:
            # Look for next kicker
            continue
        if a > b:
            return 1
        else:
            return 2
    # Draw
    return 0

def CompareHands(hand1, hand2):
    if hand1.scoreRanking == hand2.scoreRanking:
        return Tiebreaker(hand1, hand2)
    if hand1.scoreRanking > hand2.scoreRanking:
        return 1
    else:
        return 2

def main():
    player1Wins, player2Wins, draws = 0, 0, 0

    with open("./Problems 051 - 100/poker.txt") as f:
        for i, line in enumerate(f):
            hand1 = Hand(line[:14])
            hand2 = Hand(line[15:])

            result = CompareHands(hand1, hand2)
            if result == 0:
                draws += 1
            elif result == 1:
                player1Wins += 1
            elif result == 2:
                player2Wins += 1

    print("Player one wins: ", player1Wins)
    print("Player two wins: ", player2Wins)
    print("Number of draws: ", draws)

if __name__ == '__main__':
    main()
