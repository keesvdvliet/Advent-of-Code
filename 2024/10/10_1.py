#Import dependicies
from datetime import datetime

#Set the current day and puzzle data
day_no = 10
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
topoGraphicMap = {}

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for yCoord, row in enumerate(dataset):
            #Clean the line
            dataRow = row.strip()

            #Split the characters
            allCharacters = list(dataRow)

            #Loop through the characters and create a topographic map
            for xCoord, char in enumerate(allCharacters):
                coordinate = { "x": xCoord, "y": yCoord }

                #Create a height key if it does not exists yet
                if char not in topoGraphicMap:
                    topoGraphicMap[char] = []

                #Put the coordinate in the topographic map
                topoGraphicMap[char].append(coordinate)


#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Function that takes a step in a specific direction and checks if it is possible
def takeStep(direction, elevation, x, y):
    #Set the next steps
    if direction == "up":
        nextX = int(x)
        nextY = int(y) - 1
    if direction == "down":
        nextX = int(x)
        nextY = int(y) + 1
    if direction == "left":
        nextX = int(x) - 1
        nextY = int(y)
    if direction == "right":
        nextX = int(x) + 1
        nextY = int(y)

    #Create a new coord object
    nextCoord = { "x": nextX, "y": nextY }

    #Check if this coord exists at the elevation level
    if nextCoord in topoGraphicMap[str(elevation)]:
        return nextCoord
    else:
        return False

#Loop through all starting points
for startingCoord in topoGraphicMap[str(0)]: #The keys are save as a string so we use this little workaround :)
    #Set some values we will use to walk the walk
    nextElev = 1
    checkCoords = []

    #Append the starting coords to the check coords as this is the first we will test
    checkCoords.append(startingCoord)

    #We can only walk to a height of 9, so this loop stops once we reach the top
    while nextElev <= 9:
        #Set an empty list where we will store the next coords
        nextCoords = []
        canContinue = False

        for checkSteps in checkCoords:
            checkX = checkSteps['x']
                       
            checkUp = takeStep('up', nextElev, checkSteps['x'], checkSteps['y'])
            checkDown = takeStep('down', nextElev, checkSteps['x'], checkSteps['y'])
            checkLeft = takeStep('left', nextElev, checkSteps['x'], checkSteps['y'])
            checkRight = takeStep('right', nextElev, checkSteps['x'], checkSteps['y'])

            #Append the found coordinate to the nextCoords
            if checkUp != False:
                nextCoords.append(checkUp)
                canContinue = True
            if checkDown != False:
                nextCoords.append(checkDown)
                canContinue = True
            if checkLeft != False:
                nextCoords.append(checkLeft)
                canContinue = True
            if checkRight != False:
                nextCoords.append(checkRight)
                canContinue = True

         #Update the elevation count if can continue, and update the coords
        if canContinue:
            checkCoords = nextCoords
            nextElev+=1
        else:
            checkCoords = []
            break   

    #Once we are done, count all options found for this value
    hikeUniqueEndsPath = list({frozenset(d.items()): d for d in checkCoords}.values())
    hikePath = len(hikeUniqueEndsPath)

    #Add the hike path count to the answer
    answer = answer + int(hikePath)

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")