#Import dependicies
from collections import defaultdict

#Set the current day and puzzle data
day_no = 4
puzzle_no = 2
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
dataInput = []
wordSearch = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:
            #Clean the line
            dataRow = line.strip()

            #Split the characters
            wordSearchLineCharacters = list(dataRow)

            #Add line to the data input array
            dataInput.append(wordSearchLineCharacters)    

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Create a location guide for each character with the datainput
for inputSingleLine in dataInput:
    #Create defaultdict for this single line
    wordSearchLine = defaultdict(list)

    #Loop through all characters in this line and put them in the dict
    for location, letter in enumerate(inputSingleLine):
        wordSearchLine[letter].append(location)

    wordSearch.append(wordSearchLine)

#Set the horizontal and vertical lengths
horLength = len(dataInput[0]) - 1
verLength = len(wordSearch) - 1

#Collection of functions to find horizontal, vertical and diagonal letters
def findLetter(letter, line, location):
    searchInLine = wordSearch[line]

    if( location in searchInLine[letter] ):
        return True
    return False

def findMasMas(line, location):
    if line >= 1 and line < verLength:
        if location >= 1 and location < horLength:
            mOne = findLetter("M", (line - 1), (location - 1))
            mTwo = findLetter("M", (line + 1), (location - 1))
            sOne = findLetter("S", (line - 1), (location + 1))
            sTwo = findLetter("S", (line + 1), (location + 1))

            if mOne and mTwo and sOne and sTwo:
                return True
            return False
        return False
    return False

def findSamSam(line, location):
    if line >= 1 and line < verLength:
        if location >= 1 and location < horLength:
            sOne = findLetter("S", (line - 1), (location - 1))
            sTwo = findLetter("S", (line + 1), (location - 1))
            mOne = findLetter("M", (line - 1), (location + 1))
            mTwo = findLetter("M", (line + 1), (location + 1))

            if mOne and mTwo and sOne and sTwo:
                return True
            return False
        return False
    return False

def findSasMam(line, location):
    if line >= 1 and line < verLength:
        if location >= 1 and location < horLength:
            sOne = findLetter("S", (line - 1), (location - 1))
            sTwo = findLetter("S", (line - 1), (location + 1))
            mOne = findLetter("M", (line + 1), (location - 1))
            mTwo = findLetter("M", (line + 1), (location + 1))

            if mOne and mTwo and sOne and sTwo:
                return True
            return False
        return False
    return False

def findMamSas(line, location):
    if line >= 1 and line < verLength:
        if location >= 1 and location < horLength:
            sOne = findLetter("S", (line + 1), (location + 1))
            sTwo = findLetter("S", (line + 1), (location - 1))
            mOne = findLetter("M", (line - 1), (location + 1))
            mTwo = findLetter("M", (line - 1), (location - 1))

            if mOne and mTwo and sOne and sTwo:
                return True
            return False
        return False
    return False

#Loop through the WordSearch
for lineNo, wordSearchLine in enumerate(wordSearch):
    if( wordSearchLine['A'] ):
        for startLocation in wordSearchLine['A']:
            isThisMasMas = findMasMas(lineNo, startLocation)
            isThisSamSam = findSamSam(lineNo, startLocation)
            isThisSaSMaM = findSasMam(lineNo, startLocation)
            isThisMamSaS = findMamSas(lineNo, startLocation)

            #If X-MAS is found add it to the total answer value
            if isThisMasMas:
                answer+=1
            if isThisSamSam:
                answer+=1
            if isThisSaSMaM:
                answer+=1
            if isThisMamSaS:
                answer+=1

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")