#Import dependicies
from collections import defaultdict

#Set the current day and puzzle data
day_no = 4
puzzle_no = 1
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

def findHorizontal(line, location, direction):   
    #Set the search values
    keyModifier = 1 if direction == "POS" else -1

    #Search for the M
    searchHorizontal_M = location + keyModifier if location + keyModifier <= horLength and location + keyModifier >= 0 else "N"
    M_found = findLetter("M", line, searchHorizontal_M) if searchHorizontal_M != "N" else False

    #Search for the A
    searchHorizontal_A = location + (keyModifier * 2) if location + (keyModifier * 2) <= horLength and location + (keyModifier * 2) >= 0 else "N"
    A_found = findLetter("A", line, searchHorizontal_A) if searchHorizontal_A != "N" else False

    #Search for the S
    searchHorizontal_S = location + (keyModifier * 3) if location + (keyModifier * 3) <= horLength and location + (keyModifier * 3) >= 0 else "N"
    S_found = findLetter("S", line, searchHorizontal_S) if searchHorizontal_S != "N" else False

    #Return
    if M_found and A_found and S_found:
        return True
    return False

def findVertical(line, location, direction):   
    #Set the search values
    keyModifier = 1 if direction == "POS" else -1

    #Search for the M
    searchVertical_M = line + keyModifier if line + keyModifier <= verLength and line + keyModifier >= 0 else "N"
    M_found = findLetter("M", searchVertical_M, location) if searchVertical_M != "N" else False

    #Search for the A
    searchVertical_A = line + (keyModifier * 2) if line + (keyModifier * 2) <= verLength and line + (keyModifier * 2) >= 0 else "N"
    A_found = findLetter("A", searchVertical_A, location) if searchVertical_A != "N" else False

    #Search for the S
    searchVertical_S = line + (keyModifier * 3) if line + (keyModifier * 3) <= verLength and line + (keyModifier * 3) >= 0 else "N"
    S_found = findLetter("S", searchVertical_S, location) if searchVertical_S != "N" else False

    #Return
    if M_found and A_found and S_found:
        return True
    return False

def findDiagonal(line, location, directionH, directionV):
    #Set the search values
    keyModifierH = 1 if directionH == "POS" else -1
    keyModifierV = 1 if directionV == "POS" else -1
    
    #Search for the M
    searchHorizontal_M = location + keyModifierH if location + keyModifierH <= horLength and location + keyModifierH >= 0 else "N"
    searchVertical_M = line + keyModifierV if line + keyModifierV <= verLength and line + keyModifierV >= 0 else "N"
    M_found = findLetter("M", searchVertical_M, searchHorizontal_M) if searchVertical_M != "N" and searchHorizontal_M != "N" else False

    #Search for the A
    searchHorizontal_A = location + (keyModifierH * 2) if location + (keyModifierH * 2) <= horLength and location + (keyModifierH * 2) >= 0 else "N"
    searchVertical_A = line + (keyModifierV * 2) if line + (keyModifierV * 2) <= verLength and line + (keyModifierV * 2) >= 0 else "N"
    A_found = findLetter("A", searchVertical_A, searchHorizontal_A) if searchVertical_A != "N" and searchHorizontal_A != "N" else False

    #Search for the S
    searchHorizontal_S = location + (keyModifierH * 3) if location + (keyModifierH * 3) <= horLength and location + (keyModifierH * 3) >= 0 else "N"
    searchVertical_S = line + (keyModifierV * 3) if line + (keyModifierV * 3) <= verLength and line + (keyModifierV * 3) >= 0 else "N"
    S_found = findLetter("S", searchVertical_S, searchHorizontal_S) if searchVertical_S != "N" and searchHorizontal_S != "N" else False

    #Return
    if M_found and A_found and S_found:
        return True
    return False

#Loop through the WordSearch
for lineNo, wordSearchLine in enumerate(wordSearch):
    if( wordSearchLine['X'] ):
        for startLocation in wordSearchLine['X']:
            #Find horizontal matches
            horizontalP = findHorizontal(lineNo, startLocation, "POS")
            horizontalN = findHorizontal(lineNo, startLocation, "NEG")

            #Find vertical matches
            verticalP = findVertical(lineNo, startLocation, "POS")
            verticalN = findVertical(lineNo, startLocation, "NEG")

            #Find diagonal matches
            diagPP = findDiagonal(lineNo, startLocation, "POS", "POS")
            diagPN = findDiagonal(lineNo, startLocation, "POS", "NEG")
            diagNN = findDiagonal(lineNo, startLocation, "NEG", "NEG")
            diagNP = findDiagonal(lineNo, startLocation, "NEG", "POS")

            #If XMAS is found add it to the total answer value
            if horizontalP:
                answer+=1
            if horizontalN:
                answer+=1
            if verticalP:
                answer+=1
            if verticalN:
                answer+=1
            if diagPP:
                answer+=1
            if diagPN:
                answer+=1
            if diagNN:
                answer+=1
            if diagNP:
                answer+=1

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")