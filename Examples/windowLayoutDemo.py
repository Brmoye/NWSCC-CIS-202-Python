"""
This program demonstrates a window layout.
"""

from breezypythongui import EasyFrame

class windowLayout(EasyFrame):
    #__init__ method definition
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
        self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky = "NSEW")
        self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky = "NSEW")

def main():
    windowLayout().mainloop()

if __name__ == "__main__":
    main()
