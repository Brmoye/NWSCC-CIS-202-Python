"""
Program:    Chap06Lab-Sort
Author:     Brian Moye
Date:       July 2, 2020
Purpose:    This pgram contains a function that sorts a list.
"""

def isSorted(lyst):
    #Returns true if sorted, else false
    if len(lyst) <= 1:
        return True
    else:
        for index in range(len(lyst) - 1):
            if lyst[index] > lyst[index + 1]:
                return False
    return True

def main():
    #Test an empty list
    lyst = []
    print("List: ", lyst)
    print("Was list sorted?", isSorted(lyst))

    #Test list with one item
    lyst = [1]
    print("List: ", lyst)
    print("Was list sorted?", isSorted(lyst))

    #Test list with 10 sorted items
    lyst = list(range(10))
    print("List: ", lyst)
    print("Was list sorted?", isSorted(lyst))
    
    #Test list with 10 items, one not sorted
    lyst[9] = 3
    print("List: ", lyst)
    print("Was list sorted?", isSorted(lyst))

#Entry point for program execution
if __name__ == "__main__":
    main()
