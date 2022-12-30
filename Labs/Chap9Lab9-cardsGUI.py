"""
File:    Chap9Lab9-cardsGUI.py
Author:  Brian Moye
Date:    2020/07/23
Purpose: This program creates a deck of cards, then shuffles and deals them.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from cards import Deck

class CardsGUI(EasyFrame):

    def __init__(self):
        #Creates deck and sets up images
        EasyFrame.__init__(self, title = "Card Game")
        self.setSize(240, 180)
        
        #Instantiate the deck of cards
        self.deck = Deck()

        #Add labels and buttons
        self.imageLabel = self.addLabel("", row = 0, column = 0,
                                        sticky = "NSEW", columnspan = 3)
        self.stateLabel = self.addLabel("", row = 1, column = 0,
                                        sticky = "NSEW", columnspan = 3)
        self.dealBtn = self.addButton(row = 2, column = 0, text = "Deal",
                                      command = self.deal)
        self.shuffleBtn = self.addButton(row = 2, column = 1, text = "Shuffle",
                                      command = self.shuffle)
        self.newDeckBtn = self.addButton(row = 2, column = 2, text = "New Deck",
                                      command = self.newDeck)

        #Set image to back of card
        self.refreshImage("DECK/b.gif")

    def deal(self):
        #Deal a card
        card = self.deck.deal()
        self.stateLabel["text"] = str(card)
        fileName = "DECK/" + str(card.rank) + card.suit[0] + ".gif"
        self.refreshImage(fileName)
        if len(self.deck) == 0:
            self.dealBtn["state"] = "disabled"

    def shuffle(self):
        self.deck.shuffle()

    def newDeck(self):
        self.deck = Deck()
        self.stateLabel["text"] = ""
        self.refreshImage("DECK/b.gif")
        self.dealBtn["state"] = "normal"

    def refreshImage(self, fileName):
        self.image = PhotoImage(file = fileName)
        self.imageLabel["image"] = self.image

def main():
    CardsGUI().mainloop()

if __name__ == "__main__":
    main()

