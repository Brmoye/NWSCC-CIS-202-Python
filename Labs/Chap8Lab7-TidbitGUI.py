"""
Program:    Chap8Lab7-TidbitGUI.py
Author:     Brian Moye
Date:       July 16, 2020
Purpose:    This program displays a payment plan given an annual interest
            rate and a purchase price.
"""

from breezypythongui import EasyFrame

class TidbitGUI(EasyFrame):

    def __init__(self):
        #Set up window and widgets
        EasyFrame.__init__(self, title = "Tidbit Payment Schedule")

        #Add input fields
        self.addLabel(text = "Purchase Price:", row = 0, column = 0)
        self.priceField = self.addFloatField(value = 0.0, row = 0, column = 1)
        self.addLabel(text = "Annual Interest Rate:", row = 1, column = 0)
        self.rateField = self.addFloatField(value = 0.0, row = 1, column = 1)

        #Add command button
        self.button = self.addButton(text = "Compute", row = 2, column = 0,
                                        columnspan = 2,
                                        command = self.computeSchedule)

        #Add output textbox
        self.outputArea = self.addTextArea(text = "", row = 3, column = 0,
                                           columnspan = 2, width = 85,
                                           height = 20)

    def computeSchedule(self):
        #Event handler for Compute button
        purchasePrice = self.priceField.getNumber()
        monthlyPayment = 0.05 * purchasePrice
        annualRate = self.rateField.getNumber()
        monthlyRate = annualRate / 12
        month = 1
        balance = purchasePrice
        schedule = "Month  Starting Balance  Interest to Pay  "
        schedule += "Principal to Pay  Payment  Ending Balance\n"

        #Loop to calculate individual payments
        while balance > 0:
            if monthlyPayment > balance:
                monthlyPayment = balance
                interest = 0
            else:
                interest = balance * monthlyRate

            principal = monthlyPayment - interest
            remaining = balance - monthlyPayment
            schedule += "%2d%15.2f%17.2f%17.2f%17.2f%17.2f\n" % \
                        (month, balance, interest, principal,
                         monthlyPayment, remaining)
            balance = remaining
            month += 1
            self.outputArea.setText(schedule)
            
def main():
    TidbitGUI().mainloop()

if __name__ == "__main__":
    main()
