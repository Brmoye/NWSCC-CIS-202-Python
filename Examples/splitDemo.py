sentence = input("Enter a sentence: ")
listOfWords = sentence.split()

print("The words in that sentence are:")
for word in listOfWords:
    print("\"", word, "\"")
