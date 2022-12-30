import random

myFile = open("randomIntegers.txt", 'w')

for count in range(100):
    number = random.randint(1,500)
    myFile.write(str(number) + '\n')

myFile.close()
print("Random integers have been written to randomIntegers.txt")
