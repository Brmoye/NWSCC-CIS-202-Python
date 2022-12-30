"""
Program:    Chap5Lab1-Stats.py
Author:     Brian Moye
Purpose:    This program uses functions to calculate the mean,
            median, and mode of a set of numbers.
"""

def mean(lyst):
    #Returns the mean of a list of numbers
    sum = 0
    for number in lyst:
        sum += number
    if len(lyst) == 0:
        return 0
    else:
        return sum / len(lyst)

def mode(lyst):
    #Returns the mode of a list of numbers by
    #obtaining a set of unique numbers from the list
    #and their frequencies, saving these associations
    #in a dictionary
    theDictionary = {}

    for number in lyst:
        freq = theDictionary.get(number, None)
        if freq == None:
            #Number seen for first time
            theDictionary[number] = 1
        else:
            #Number already seen, increment count
            theDictionary[number] = freq + 1
    #Find the mode by obtaining the maximum frequency and
    #determining its key
    if len(theDictionary) == 0:
        return 0
    else:
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key

def median(lyst):
    #Returns the median of a list of numbers
    #Create a copy of the lyst called numbers and then sort
    numbers = []
    for number in lyst:
        numbers.append(number)
    numbers.sort()

    #Find the midpoint and return the value
    if len(numbers) == 0:
        return 0

    else:
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1]) / 2
        
def main():
    lyst = [3, 1, 7, 1, 4, 10]
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))

#Entry point for program execution
if __name__ == "__main__":
    main()



    


    
