#Initialize variables
theSum = 0.0
count = 0


done = False
while not done:
    data = input("Enter a numeric grade or just press Enter to quit: ")
    if data == "":
        done = True
    else:
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
