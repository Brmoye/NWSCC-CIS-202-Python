import os

currentDirPath = os.getcwd()
print("The current directory is", currentDirPath)
listOfFileNames = os.listdir(currentDirPath)

print("The files in this directory are:")
for name in listOfFileNames:
    if ".py" in name:
        print(name)
