"""
Program: mathDemo.py
Author: Stephen Chandler
Purpose: This program uses math to calculate income tax.
"""

#Initialize constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 3000.00

#Get data from user
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

#Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

#Display the income tax
print("The calculated income tax is $" + str(incomeTax))
