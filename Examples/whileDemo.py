#Initialize theSum
theSum = 0.0

#Get data from user
data = input("Enter a numeric grade or just press Enter to quit: ")
count = 0

while data != "":
    number = float(data)
    if number >= 0 and number <= 100:
        count += 1
        theSum += number
        data = input("Enter a numeric grade or just press Enter to quit: ")
    else:
        print("ERROR: Number must be between 0 and 100.")
        data = input("Enter a numeric grade or just press Enter to quit: ")
    
#Calculate average grade and display
theSum /= count
print("The sum of the grades is", theSum)
