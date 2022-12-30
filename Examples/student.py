#student.py class file

class Student(object):
    def __init__(self, name, number):
        #Constructor to create Student objects
        self.name = name
        
        #Create empy array of scores
        self.scores = []
        
        #Append number of 0 to scores array
        for count in range(number):
            self.scores.append(0)

    #Mutator methods
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def addScore(self, score):
        self.scores.append(int(score))

    #Accessor methods
    def getName(self):
        return self.name

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        return max(self.scores)

    def getNumScore(self):
        return len(self.scores)

    def __str__(self):
        #Returns string representation of object contents
        return "Name: " + self.name + "\nScores: " \
               + " ".join(map(str, self.scores))
