import random

myfile = open("randomIntegers.txt", 'r')

for line in myfile:             #Read each line in myfile
    line = line.strip()         #Strip off whitespace
    number = int(line)          #Convert line to int
    print(number, end=", ")

myfile.close()
print("Done")
