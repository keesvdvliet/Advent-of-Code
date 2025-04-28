#Import dependicies
from datetime import datetime

#Set the current day and puzzle data
day_no = 11
puzzle_no = 2
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
stones = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for row in dataset:
            #Clean the line
            dataRow = row.strip()

            #Split the characters
            stones = dataRow.split(" ")

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Check all stone rules
maxBlinks = 25
curBlinks = 0
newStones = []

#Loop until we've reached the maxBlinks
while curBlinks < maxBlinks:
    #Loop through all stones
    for stone in stones:
        #If a rule is not yet applied we can append otherwise not
        ruleApplied = False

        #Rule 1
        if int(stone) == int(0):
            if ruleApplied == False:
                newStones.append(int(1))
                ruleApplied = True

        #Rule 2
        stoneString = str(stone)
        stoneSize = len(stoneString)
        
        if stoneSize % 2 == 0:
            stoneSplit = int(stoneSize / 2)
            stoneOne = int(stoneString[0:stoneSplit])
            stoneTwo = int(stoneString[stoneSplit:])

            if ruleApplied == False:
                newStones.append(stoneOne)
                newStones.append(stoneTwo)
                ruleApplied = True

        #Rule 3
        stoneValue = 2024 * int(stone)
        if ruleApplied == False:
            newStones.append(stoneValue)
            ruleApplied = True

    #Add a blink and update the stone-lists
    stones = newStones
    newStones = []
    curBlinks+=1

#All stones have been processed, the answer is the no. of stones
answer = len(stones)

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")