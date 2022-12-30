"""
This demo demonstrates the use of a for loop and formatting strings in a print statement
"""

#Get data from user
startBal = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the whole number interest rate as a percantage: "))

#Convert interest rate percentage to a decimal
rate /= 100

#Initialize the accumulator for interest
totalInt = 0.0

#Display header for table output
print("%4s%18s%10s%16s" % \
      ("Year", "Starting Balance", "Interest", "Ending Balance"))

#Calculate and display results for each year
for year in range(1, years + 1):
    interest = startBal * rate
    endBal = startBal + interest
    print("%4d%18.2f%10.2f%16.2f" % \
          (year, startBal, interest, endBal))
    startBal = endBal
    totalInt += interest

#Display the totals
print("Ending Balance: $%0.2f" % endBal)
print("Total interest earned: $%0.2f" % totalInt)
