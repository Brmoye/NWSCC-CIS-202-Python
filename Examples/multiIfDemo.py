#Get input from user
number = int(input("Enter a numeric grade: "))

if number >= 0 and number <= 100:
    #Calculate letter grade based on numeric grade
    if number > 89:
        letter = 'A'
    elif number > 79:
        letter = 'B'
    elif number > 69:
        letter = 'C'
    elif number > 59:
        letter = 'D'
    else:
        letter = 'F'
    print("The letter grade is", letter)
else:
    print("ERROR: Grade must be between 0 and 100")
    


