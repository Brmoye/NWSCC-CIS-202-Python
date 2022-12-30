"""
Program: medianListDemo.py
Purpose: This program finds the median in a list of numbers in a file.
"""

#Get filename from user and open for reading
fileName = input("Enter the filename: ")
fileptr = open(fileName, 'r')

#Convert file text to numbers and add to a list
numbers = [] #Create empy list
for line in fileptr:
    words = line.split()
    for word in words:
        numbers.append(float(word))

#Sort the numbers list and display the midpoint number
numbers.sort()
print("The list for median calculation is", numbers)
midpoint = len(numbers) // 2

print("The median is", end = " ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

