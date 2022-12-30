"""
Program:    Chap04Tidbit.py
Author:     Brian Moye
Date:       June 11, 2020
Purpose:    Display a payment schedule table
"""

#Declare interest rate constants
ANNUAL_RATE = .12
MONTHLY_RATE = ANNUAL_RATE / 12

#Get purchase price from user
purchasePrice = float(input("Enter purchase price: "))

#Get down payment from user
downPayment = float(input("Enter down payment or 0 for none: "))

#Calculate monthly payment and setup loop calculation
monthlyPayment = 0.05 * purchasePrice - downPayment
month = 1
balance = purchasePrice - downPayment

#Print table heading
print("Month  Starting Balance  Interest to Pay \
        Principal to Pay  Payment  Ending Balance")

#Calculate all info and display
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * MONTHLY_RATE

    principal = monthlyPayment - interest
    remaining = balance - monthlyPayment

    print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % \
           (month, balance, interest, principal, monthlyPayment, remaining))
    balance = remaining
    month += 1
