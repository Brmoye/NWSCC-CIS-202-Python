"""
Program:    Chap4Lab-payroll.py
Author:     Brian Moye
Date:       June 18, 2020
Purpose:    Reads a data file containing names, hours and total pay,
            and then displays the information in table form.
"""

import os

#Get the file name from user and store it in a variable called fileName
fileName = input("Enter payroll filename (include file extension): ")
fileName = "payroll/" + fileName

#check if file and/or directory exists
if os.path.exists(fileName):
    #Open the input file for reading using the name stored in fileName
    inputFile = open(fileName, 'r')

    #Print table heading
    print("\n*** ABC Company Payroll Report***")
    print("%-15s%6s%15s" % ("---------------", "------", "---------------"))
    print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))

    #Read data, calculate total pay, and display data
    for line in inputFile:
        
        #Use split()function to split data in line variable and store in dataList
        dataList = line.split()
        
        #Store the first element of the dataList array and store in name variable
        name = dataList[0]
        
        #Store the second element of the dataList array and store in hours variable
        hours = int(dataList[1])
        
        #Store the third element of the dataList array and store in payRate variable
        payRate = float(dataList[2])

        #Calculate the total pay
        totalPay = hours * payRate

        #Display data
        print("%-15s%6d%15.2f" % (name, hours, totalPay))
else:
    print("Error: Payroll file does not exist. See administrator.")
