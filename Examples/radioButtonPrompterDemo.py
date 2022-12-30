"""
This program uses radio buttons to populate a prompter popup window.
"""

from breezypythongui import EasyFrame

class radioButtonPromptDemo(EasyFrame):
    #__init__ method definition
    def __init__(self):
        EasyFrame.__init__(self, "Joe's Restaurant Menu")

        #Label, group, and radio buttons for meats
        self.addLabel(text = "Meat", row = 0, column = 0)
        self.meatGroup = self.addRadiobuttonGroup(row = 1, column = 0,
                                                  rowspan = 2)
        defaultRB = self.meatGroup.addRadiobutton(text = "Chicken")
        self.meatGroup.setSelectedButton(defaultRB)
        self.meatGroup.addRadiobutton(text = "Beef")

        #Label, group, and radio buttons for potatoes
        self.addLabel(text = "Potato", row = 0, column = 1)
        self.taterGroup = self.addRadiobuttonGroup(row = 1, column = 1,
                                                  rowspan = 2)
        defaultRB2 = self.taterGroup.addRadiobutton(text = "French fries")
        self.taterGroup.setSelectedButton(defaultRB2)
        self.taterGroup.addRadiobutton(text = "Baked potato")

        #Label, group, and radio buttons for vegetables
        self.addLabel(text = "Vegetables", row = 0, column = 2)
        self.vegGroup = self.addRadiobuttonGroup(row = 1, column = 2,
                                                  rowspan = 2)
        defaultRB3 = self.vegGroup.addRadiobutton(text = "Carrots")
        self.vegGroup.setSelectedButton(defaultRB3)
        self.vegGroup.addRadiobutton(text = "Green beans")

        self.addButton(text = "Place order", row = 3, column = 0,
                       columnspan = 3, command = self.placeOrder)

    #Definitions of event handlers
    def placeOrder(self):
        message = ""

        message += self.meatGroup.getSelectedButton()["text"] + "\n"
        message += self.taterGroup.getSelectedButton()["text"] + "\n"
        message += self.vegGroup.getSelectedButton()["text"] + "\n"

        self.messageBox(title = "Customer Order", message = message)

def main():
    radioButtonPromptDemo().mainloop()

if __name__ == "__main__":
    main()
