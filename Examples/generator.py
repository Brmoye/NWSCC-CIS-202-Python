"""
This program generates sentences using simple grammar and vocabulary.
Words are chosen at random.
"""

import random

#Vocabulary: words in 4 different parts of speech
articles     = ("A", "THE")
nouns        = ("BOY", "GIRL", "BAT", "BALL")
verbs        = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def main():
    """Let user choose number of sentences to generate."""
    number = int(input("Enter the number of sentences to generate: "))
    for count in range(number):
        print(sentence())

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

#Entry point for program execution
if __name__ == "__main__":
    main()
