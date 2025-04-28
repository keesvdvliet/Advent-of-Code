#Import dependicies
from collections import defaultdict

#Set the current day and puzzle data
day_no = 6
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

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")