def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1

    return result

def main():
    print("This program sums a range of numbers.")
    lower = int(input("Enter the lower number: "))
    upper = int(input("Enter the upper number: "))
    print("The summation of", lower, "and", upper, "is", \
          summation(lower, upper))

#Entry point for program execution
if __name__ == "__main__":
    main()
