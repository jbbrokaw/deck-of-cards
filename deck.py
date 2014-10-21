from __future__ import unicode_literals
import random

SUIT_NAMES = {0: "Hearts",
              1: "Diamonds",
              2: "Clubs",
              3: "Spades"}

VALUE_NAMES = {0: "Ace",
               1: "Two",
               2: "Three",
               3: "Four",
               4: "Five",
               5: "Six",
               6: "Seven",
               7: "Eight",
               8: "Nine",
               9: "Ten",
               10: "Jack",
               11: "Queen",
               12: "King"}  # Might make human-readable eventually


class Card(object):
    def __init__(self, suit, value):
        if suit < 0 or suit > 3:
            raise ValueError("Invalid suit")
        if value < 0 or value > 12:
            raise ValueError("Invalid value")
        self.suit = suit
        self.value = value

    def __eq__(self, othercard):
        return self.value == othercard.value and self.suit == othercard.suit

    def __cmp__(self, othercard):
        if self.value == 0:  # An ace
            if othercard.value == 0:
                return 0
            else:
                return 1

        if othercard.value == 0:
            return -1

        return cmp(self.value, othercard.value)


class Deck(list):
    def __init__(self):
        for suit in xrange(4):
            for value in xrange(13):
                self.append(Card(suit, value))
        self.top_index = 0  # Keep track of which card to deal

    def deal(self):
        topcard = self[self.top_index]
        self.top_index = (self.top_index + 1) % len(self)
        # keep cycling through, we probably want to shuffle when this is zero
        return topcard

    def shuffle(self):
        self.top_index = 0
        random.shuffle(self)
