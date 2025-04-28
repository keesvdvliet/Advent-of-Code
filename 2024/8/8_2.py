#Import dependicies
from collections import defaultdict

#Set the current day and puzzle data
day_no = 8
puzzle_no = 2
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
rawMapLines = []
coordMap = defaultdict(list)
registeredAntinodes = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:
            #Clean the line
            dataRow = line.strip()

            #Split the characters
            mappingLine = list(dataRow)

            #Add line to the data input array
            rawMapLines.append(mappingLine)    

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Set the height and the width of the map we are using
mapWidth = len(rawMapLines[0]) - 1
mapHeight = len(rawMapLines) - 1

#Create a coordinate map of all characters
for yLocation, mapLine in enumerate(rawMapLines):

    #Loop through all characters in this line and put them in the dict if needed
    for xLocation, char in enumerate(mapLine):
        if( char != "." ):
            charCoords = {"x": xLocation, "y": yLocation}
            coordMap[char].append(charCoords)

#Function that creates the antinode locations and checks them against the map
def createAntinode(xLocationA, xLocationB, yLocationA, yLocationB):
    #Determine the first coordinate
    if( yLocationA != yLocationB ):
        firstValue = "A" if yLocationB > yLocationA else "B"
    else:
        firstValue = "A" if xLocationB > xLocationA else "B"

    #Set the X-direction
    if firstValue == "A":
        xDirection = "L" if xLocationB < xLocationA else "R"
    elif firstValue == "B":
        xDirection = "L" if xLocationA < xLocationB else "R"

    #Calculate the distance between
    xDistance = abs(xLocationA - xLocationB)
    yDistance = abs(yLocationA - yLocationB)

    #Set the starting coords
    xStart = xLocationA if firstValue == "A" else xLocationB
    yStart = yLocationA if firstValue == "A" else yLocationB

    #Register the starting coords as an antinode
    if xStart >= 0 and xStart <= mapWidth and yStart >= 0 and yStart <= mapHeight:
        #Antinode fits, if it is not already in the list. Add it.
        antinodeF = {"x": xStart, "y": yStart}
        if antinodeF not in registeredAntinodes:
            registeredAntinodes.append( antinodeF )

    #Forwards while loop, as long as we are in bounds continue
    forwardsInBound = True
    currentForwards = int(1)

    while forwardsInBound:
        #Set the antinode coords
        xAntinode = xStart - (xDistance * currentForwards) if xDirection == "L" else  xStart + (xDistance * currentForwards)
        yAntiNode = yStart + (yDistance * currentForwards)

        #Update the current forwards counter
        currentForwards+=1

        #Check if the antinodes fit on the map
        if xAntinode >= 0 and xAntinode <= mapWidth and yAntiNode >= 0 and yAntiNode <= mapHeight:
            #Antinode fits, if it is not already in the list. Add it.
            antinodeE = {"x": xAntinode, "y": yAntiNode}
            if antinodeE not in registeredAntinodes:
                registeredAntinodes.append( antinodeE )
        else:
            #Antinode does not fit, stop the forwards loop
            forwardsInBound = False

    #Backwards while loop, as long as we are in bounds continue
    backwardsInBound = True
    currentBackwards = int(1)

    while backwardsInBound:
        #Set the antinode coords
        xAntinode = xStart + (xDistance * currentBackwards) if xDirection == "L" else  xStart - (xDistance * currentBackwards)
        yAntiNode = yStart - (yDistance * currentBackwards)

        #Update the current backwards counter
        currentBackwards+=1

        #Check if the antinodes fit on the map
        if xAntinode >= 0 and xAntinode <= mapWidth and yAntiNode >= 0 and yAntiNode <= mapHeight:
            #Antinode fits, if it is not already in the list. Add it.
            antinodeF = {"x": xAntinode, "y": yAntiNode}
            if antinodeF not in registeredAntinodes:
                registeredAntinodes.append( antinodeF )
        else:
            #Antinode does not fit, stop the backwards loop
            backwardsInBound = False

#Check all frequencies on the coord map
for frequency in coordMap:
    #Count how many times this char occurs
    charCount = len(coordMap[frequency])

    #Only continue if the character occures more than once in the mapping
    if( charCount > 1 ):
        #Set index compare
        charMaxIndex = charCount - 1

        #Loop through the coords
        for index, coords in enumerate(coordMap[frequency]):
            #Set the location
            xLocationCheck = coords['x']
            yLocationCheck = coords['y']

            #We loop through all coords, and check them against all availble characters again in the loop below
            for i in range(len(coordMap[frequency])):
                #Only check if this is not the current index
                if( index != i ):
                    #Set the distance
                    xLocationCompare = coordMap[frequency][i]['x']
                    yLocationCompare = coordMap[frequency][i]['y']

                    #Check if a antinode can be place on the map for this line
                    createAntinode(xLocationCheck, xLocationCompare, yLocationCheck, yLocationCompare)

#Count the registered antinodes to get the answer
answer = len(registeredAntinodes)

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")