#Import dependicies
import re

#Set the current day and puzzle data
day_no = 3
puzzle_no = 2
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
corDataString = ""
processedCorDataString = ""
cleanData = []
doFunctions = []
dontFunctions = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:
            corDataString = corDataString+line

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#First find all locations of the do() and don't() functions in the corrupted data string
doRegexPattern = r"do\(\)"
doFunctions = re.finditer(doRegexPattern, corDataString)
doFunctions = [function.start(0) for function in doFunctions] #This fetched the start location in the datastring of the do() function

dontRegexPattern = r"don\'t\(\)"
dontFunctions = re.finditer(dontRegexPattern, corDataString)
dontFunctions = [function.start(0) for function in dontFunctions] #This fetched the start location in the datastring of the don't() function

#We are going to create an array which we will use to strip the string of all mul() functions excluded from the calculations by the don't() functions
stringStripper = []

for functionLoc in doFunctions:
    stringStripper.append( {'location': functionLoc, 'type': "DO" } )
for functionLoc in dontFunctions:
    stringStripper.append( {'location': functionLoc, 'type': "DONT" } )

#Add a additional do() function to location 0
stringStripper.append( {'location': 0, 'type': "DO" } )

#Now sort the string stripper based on the location key
stringStripper.sort(key=lambda functionLoc: functionLoc['location'])

#Loop through the string stripper
stringStripperLen = len(stringStripper)

for index, stripCheck in enumerate(stringStripper):
    #Set the start and end of the location
    start = int(stripCheck['location'])

    if index+1 == stringStripperLen: #Last check in the do/dont functions
        end = int(len(corDataString))
    else:
        end = int(stringStripper[index+1]['location'])

    #Check if this is a do function, if so put this part in our new processed data string
    if( stripCheck['type'] == "DO" ):
        subString = corDataString[start:end]
        processedCorDataString = processedCorDataString+subString

#Set the regex pattern to find mul(#,#)
regexPattern = r"mul\(\d{1,3},\d{1,3}\)"

#Perform the search on the processed corrupted datastring and put all matched in the clean data array
cleanData = re.findall(regexPattern, processedCorDataString)

#Loop through the clean datalines
for mulFunction in cleanData:
    #First remove the mul( and the closing-) from the string
    mulInput = mulFunction.replace('mul(', '').replace(')', '')

    #Split the input on the comma
    mulNumbers = mulInput.split(",")

    #Now perform mul function
    mulResult = int(mulNumbers[0]) * int(mulNumbers[1])

    #Add the mul function result to the final answer
    answer = answer + mulResult

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")