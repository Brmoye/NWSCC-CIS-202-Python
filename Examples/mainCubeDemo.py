def main():
    """This program is an interface for the cube() function."""
    number = float(input("Enter a number to cube: "))
    result = cube(number) #Call user-defined cube() function
    print("The cube of", number, "is", result)

def cube(num):
    """Returns the cube of a number"""
    return num ** 3

#Entry point for program execution
if __name__ == "__main__":
    main()
