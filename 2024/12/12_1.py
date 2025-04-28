#Import dependicies
import asyncio
from collections import deque

#Set the current day and puzzle data
day_no = 12
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
gardenMap = {}
gardenHeightCounter = 0
gardenWidthCounter = 0

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:
        #Loop through all the lines in the data
        for y, row in enumerate(dataset):
            #Add a row to the garden height
            gardenHeightCounter+=1

            #Clean the line
            dataRow = row.strip()

            #Split the characters
            plotTypes = list(dataRow)

            #Set width of the garden
            gardenWidthCounter = len(plotTypes)

            #Loop through all coordinates
            for x, plotName in enumerate(plotTypes):
                #Put plot coordinates in the garden map
                if plotName not in gardenMap:
                    gardenMap[plotName] = {}

                if y not in gardenMap[plotName]:
                    gardenMap[plotName][y] = {}
                
                if x not in gardenMap[plotName][y]:
                    gardenMap[plotName][y][x] = None

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Fix numeric values (we are starting at 0 coints)
gardenHeight = gardenHeightCounter - 1
gardenWidth = gardenWidthCounter - 1

async def defineArea(plotName):
    returnMap = {}

    #Get the map for the specific plotName
    plotMap = gardenMap.get(plotName)
    
    #Create first areaCode and the visited set that tracks all visited coordinates so we are not checking double
    areaCode = 1
    visited = set()

    #Up, down, left, right directions for checking
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #Check if coord is in bounds
    def inBounds(y, x):
        return 0 <= y <= gardenHeight and 0 <= x <= gardenWidth

    def floodFill(y, x, areaCode):
        #We are creating a que in which we will store all coordinates we are going to perform the floodFill check on
        coordinateQueue = deque([(y, x)])

        while coordinateQueue:
            currY, currX = coordinateQueue.popleft()
            if (currY, currX) not in visited:
                visited.add((currY, currX))

                #Put coordinates in the return map
                if currY not in returnMap:
                    returnMap[currY] = {}
                returnMap[currY][currX] = areaCode

                #Loop through directions and check
                for difY, difX in directions:
                    newY, newX = currY + difY, currX + difX

                    #First check map boundary
                    if inBounds(newY, newX):
                        #Only continue if we have not checked this coordinate yet
                        if (newY, newX) not in visited:
                            if newY in plotMap and newX in plotMap[newY]:
                                #Found same plot, add to the same are code
                                coordinateQueue.append((newY, newX))

    # Loop through all items in the plotMap
    for y in plotMap:
        for x in plotMap[y]:
            if (y, x) not in visited:
                #Perform the flood fill on coordinates we have not checked yet
                floodFill(y, x, areaCode)

                #Update area code after finishing each new flood fill
                areaCode += 1

    return returnMap

async def definePerimeter(plotName):
    returnMap = {}

    #Get the map for the specific plotName
    plotMap = gardenMap.get(plotName)    

    #Up, down, left, right directions for checking
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #Check if coord is in bounds
    def inBounds(y, x):
        return 0 <= y <= gardenHeight and 0 <= x <= gardenWidth

    #Function that places the necessary amount of fences around a single coordinate
    def fencePlacer(y, x):
        fenceCount = int(0)

        #Loop through directions and check
        for difY, difX in directions:
            newY, newX = y + difY, x + difX

            #First check map boundary
            if inBounds(newY, newX):
                if newY not in plotMap or newX not in plotMap[newY]:
                    #Coordinate not in our current plotMap, so we place fence
                    fenceCount+=1       
            else:
                #Not in boundary, so we place a fence
                fenceCount+=1
        
        return fenceCount

    #Loop through all coordinates of this garden plot
    for y, xDict in gardenMap[plotName].items():
        for x in xDict.keys():
            #Put plot coordinates in the return map
            if y not in returnMap:
                returnMap[y] = {}
            if x not in returnMap[y]:
                returnMap[y][x] = 0

            #Run fence counter and add the count to the return map
            returnMap[y][x] = fencePlacer(y,x)

    return returnMap

async def createPlotMap(gardenMap):
    #Create the return map to start with
    returnMap = {}

    #Create a list of tasks for asynchronous execution
    createAreaTasks = {}
    createPerimeterTasks = {}

    for plotName in gardenMap:
        #Create tasks for defineing the areas en perimeters by each plot name
        createAreaTasks[plotName] = asyncio.create_task(defineArea(plotName))
        createPerimeterTasks[plotName] = asyncio.create_task(definePerimeter(plotName))

    #Run all scheduled ask concurrently wait for them to finish
    returnMap = {
        "areas": {plotName: result for plotName, result in zip(createAreaTasks.keys(), await asyncio.gather(*createAreaTasks.values()))},
        "perimeters": {plotName: result for plotName, result in zip(createPerimeterTasks.keys(), await asyncio.gather(*createPerimeterTasks.values()))}
    }
    
    #Return
    if "areas" in returnMap and "perimeters" in returnMap:
        return returnMap

#Run function to create the garden plot map
gardenPlotMap = asyncio.run(createPlotMap(gardenMap))

#Build a calculator map
calculatorMap = {}

for areaName, areaMap in gardenPlotMap['areas'].items():
    #Fetch the perimeter map
    perimeterMap = gardenPlotMap['perimeters'][areaName]

    #Loop through the perimeters
    for y, perimeterX in perimeterMap.items():
        for x, fenceCount in perimeterX.items():
            #Fetch the area code that is matched to these coords
            if y in areaMap and x in areaMap[y]:
                areaCode = f"{areaName}{areaMap[y][x]}"

                if areaCode not in calculatorMap:
                    calculatorMap[areaCode] = {}
                    calculatorMap[areaCode] = {"areaSize": int(1), "fences": int(fenceCount)}
                else:
                    newAreaCount = int( calculatorMap[areaCode]["areaSize"] ) + 1
                    newFenceCount = int(  calculatorMap[areaCode]["fences"] ) + int( fenceCount )                    
                    calculatorMap[areaCode] = {"areaSize": int(newAreaCount), "fences": int(newFenceCount)}

#Process the final calculations for the price
for areaCode, values in calculatorMap.items():
    print(f"{areaCode} - Area size: {int(values['areaSize'])}, Fence count: {int(values['fences'])}")

    fencePrice = int(values["areaSize"]) * int(values["fences"])
    answer = answer + fencePrice

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")