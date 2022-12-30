"""
Program:    doctor.py
Author:     Brian Moye
Purpose:    Conducts an interactive session of
            nondirective psychotherapy.
"""

import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.",
          "Please, continue.")
qualifiers = ("Why do you say that ", "You seem to think that ",
              "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your", "we":"you",
                "us":"you", "mine":"yours"}

def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1,4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
     """Replaces first person pronoun with second person pronoun."""
     words = sentence.split()
     replyWords = []
     for word in words:
         replyWords.append(replacements.get(word, word))
     return " ".join(replyWords)

def main():
    """Handles interaction between doctor and patient."""
    print("Good morning, I hope you're well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("I hope this session was helpful")
            print("Have a nice day!")
            break
        print(reply(sentence))

#Entry point for program execution
if __name__ == "__main__":
    main()
        
