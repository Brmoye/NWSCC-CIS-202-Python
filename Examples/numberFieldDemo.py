"""
This program uses a button to populate a textbox
"""

from breezypythongui import EasyFrame
import math

class numberFieldDemo(EasyFrame):
    #__init__ method definition
    def __init__(self):
        EasyFrame.__init__(self, title = "Number Field Demo")
        
        self.addLabel(text = "Enter an integer:", row = 0, column = 0)
        self.inputField = self.addIntegerField(value = 0, row = 0,
                                               column = 1, width = 10)

        self.addLabel(text = "Square root:", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0,
                                              row = 1, column = 1,
                                              width = 8, precision = 2,
                                             state = "readonly")
        self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2,
                       command = self.computeSqrt)
        
    #Definitions of event handlers
    def computeSqrt(self):
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)

def main():
    numberFieldDemo().mainloop()

if __name__ == "__main__":
    main()
