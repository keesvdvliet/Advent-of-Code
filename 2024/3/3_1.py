#Import dependicies
import re

#Set the current day and puzzle data
day_no = 3
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
corDataString = ""
cleanData = []

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

#Set the regex pattern to find mul(#,#)
regexPattern = r"mul\(\d{1,3},\d{1,3}\)"

#Perform the search on the corrupted datastring and put all matched in the clean data array
cleanData = re.findall(regexPattern, corDataString)

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