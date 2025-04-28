#Import dependicies
from datetime import datetime
import asyncio

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
stoneStorage = {}
sleepInterval = 0 #This delays all functions a bit to help with memory

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for row in dataset:
            #Clean the line
            dataRow = row.strip()

            #Split the characters
            startingStones = dataRow.split(" ")
            
            #Build stone dict
            for stone in startingStones:
                if stone in stoneStorage:
                    stoneStorage[int(stone)]+=1
                else:
                    stoneStorage[int(stone)]=int(1)

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Rule 1: Fetch all 0-stones, update and return keys
async def ruleOne(stones):
    await asyncio.sleep(sleepInterval) #Async sleep value
    returnStones = {}

    #Fetch 0 and swap them with 1's
    if 0 in stones:
        stoneCount = stones[0]

        if 1 in returnStones:
            returnStones[1]+=int(stoneCount)
        else:
            returnStones[1] = int(stoneCount)

    #Return stones
    return returnStones

#Rule 2: Fetch all stones divisible by 2, update and return keys
async def ruleTwo(stones):
    await asyncio.sleep(sleepInterval) #Async sleep value
    returnStones = {}

    #Fetch even numbers and split them
    allEvenStones = [key for key in stones.keys() if int(len(str(key))) % 2 == 0]
    for evenStoneKey in allEvenStones:
        stoneCount = stones[evenStoneKey]

        #Generate the stone value
        stoneValue = str(evenStoneKey)
        stoneSplit = int(len(stoneValue) / 2)
        stoneOne = int(stoneValue[0:stoneSplit])
        stoneTwo = int(stoneValue[stoneSplit:])

        #Create dicts
        if stoneOne in returnStones:
            returnStones[stoneOne]+=int(stoneCount)
        else:
            returnStones[stoneOne] = int(stoneCount)

        if stoneTwo in returnStones:
            returnStones[stoneTwo]+=int(stoneCount)
        else:
            returnStones[stoneTwo] = int(stoneCount)

    #Return stones
    return returnStones

#Rule 3: All remaining stones * 2024
async def ruleThree(stones):
    await asyncio.sleep(sleepInterval) #Async sleep value
    returnStones = {}

    #Fetchh remaing numbers and calc. them
    allRemainingStones = [key for key in stones.keys() if int(len(str(key))) % 2 != 0 and key != 0]
    for evenStoneKey in allRemainingStones:
        stoneCount = stones[evenStoneKey]

        #Generate the stone value
        newStoneValue = int(2024 * int(evenStoneKey))

        #Create dict
        if newStoneValue in returnStones:
            stoneStorage[newStoneValue]+=int(stoneCount)
        else:
            returnStones[newStoneValue] = int(stoneCount)

    #Return stones
    return returnStones

#Async function for rule 1 and 2 tasks and remove all processed stones
async def runCalculations(stoneInput):
    #Run all rules concurrently
    runRules = await asyncio.gather(ruleOne(stoneInput), ruleTwo(stoneInput), ruleThree(stoneInput))
    #combinedStones = []

    #If all rules have returned True continue, add a blink and update the stone-list
    if runRules:
        #Add the other numbers
        newStoneUnique = {}
        for d in [runRules[0], runRules[1], runRules[2]]:
            for key, value in d.items():
                if key in newStoneUnique:
                    newStoneUnique[key] += value  # Sum the values for duplicate keys
                else:
                    newStoneUnique[key] = value

        #Return
        return newStoneUnique

#Set blinks values
maxBlinks = 75
curBlinks = 0
newStones = stoneStorage

#Loop until we've reached the maxBlinks
while curBlinks < maxBlinks:
    #Send update signal
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Blink: {curBlinks+1} ({current_time})')

    #New stones value is the value returned by the calculations
    newStones = asyncio.run(runCalculations(newStones))
    print(f"New stones generated ({current_time})")

    #Update the blink count
    curBlinks+=1

#All stones have been processed, the answer is the no. of stones
for stoneCount in newStones.values():
    answer = answer + int(stoneCount)

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")