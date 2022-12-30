"""
This program uses checkboxes to populate a prompter popup window.
"""

from breezypythongui import EasyFrame

class checkboxPrompterDemo(EasyFrame):
    #__init__ method definition
    def __init__(self):
        EasyFrame.__init__(self, "Joe's Restaurant Menu")
        
        self.chickCB = self.addCheckbutton(text = "Chicken",
                                           row = 0, column = 0)
        self.taterCB = self.addCheckbutton(text = "French fries",
                                           row = 0, column = 1)
        self.beansCB = self.addCheckbutton(text = "Green beans",
                                           row = 1, column = 0)
        self.sauceCB = self.addCheckbutton(text = "Applesauce",
                                           row = 1, column = 1)

        self.addButton(text = "Place order", row = 2, column = 0,
                       columnspan = 2, command = self.placeOrder)

    #Definitions of event handlers
    def placeOrder(self):
        message = ""

        if self.chickCB.isChecked():
            message += "Chicken\n"
        if self.taterCB.isChecked():
            message += "French fries\n"
        if self.beansCB.isChecked():
            message += "Green beans\n"
        if self.sauceCB.isChecked():
            message += "Applesauce\n"
        if message == "":
            message = "No food ordered."

        self.messageBox(title = "Customer Order", message = message)

def main():
    checkboxPrompterDemo().mainloop()

if __name__ == "__main__":
    main()
