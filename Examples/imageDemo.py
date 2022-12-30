"""
This program displays a photo in a window
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class imageDemo(EasyFrame):
    #__init__ method definition
    def __init__(self):
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "Smokey the cat",
                                   row = 1, column = 0,
                                   sticky = "NSEW")

        #Definitions of event handlers
        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"

def main():
    imageDemo().mainloop()

if __name__ == "__main__":
    main()
