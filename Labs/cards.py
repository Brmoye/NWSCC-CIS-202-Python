"""
File: cards.py
Project 9.8
Module for playing cards, with classes Card and Deck.
Adds a faceup attribute and a turn method.
"""

import random

class Card(object):
    """ A card object with a suit and rank."""
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    
    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        self.faceup = False

    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

    def turn(self):
        """Turns the card over."""
        self.faceup = not self.faceup

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        #Remove and return top card on deck or none if empty
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        result = ""
        for c in self.cards:
            result = self.result + str(c) + "\n"

        return result



    
