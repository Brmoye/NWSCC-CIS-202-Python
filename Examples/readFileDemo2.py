tempFile = open("temperatures.txt", 'r')

print("Weekly Temperatures")
print("-------------------")
for line in tempFile:
    tempsList = line.split()
    for temp in tempsList:
        temperature = int(temp)
        print(temperature, end = " ")
    print()
