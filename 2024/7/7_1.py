#Import dependicies
from functools import lru_cache
from datetime import datetime

#Set the current day and puzzle data
day_no = 7
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = int(0)

#Set some variables
calibrationTest = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:
            #Clean the line
            dataRow = line.strip()

            #Split the answer from the numbers
            splitDataRow = dataRow.split(":")
            correct = splitDataRow[0]
            numbers = splitDataRow[1].strip().split(" ") #Add strip so we remove the leading blank space

            #Add a answer/number dict to the calibrationTest dictionary
            answernumber = {"answer": correct, "numbers": numbers}
            calibrationTest.append(answernumber)

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Function that generates all possible calculation-options starting from the answer
def generateCalculations(inputNumbers, correctAnswer):
    @lru_cache(None) #Caching function to store calculations, for efficiency

    #Nested function that finds all possible ways to get to the answer and returns the number of possibilities
    def findCalcs(currentIndex, currentResult):
        #Last number in our loop, now we will return the ammount of possible calculations
        if currentIndex == len(inputNumbers):
            return 1 if currentResult == correctAnswer else 0

        # Perform + and * check with the next number
        nextNumber = inputNumbers[currentIndex]
        addWays = findCalcs(currentIndex + 1, int(currentResult) + int(nextNumber))
        multiplyWays = findCalcs(currentIndex + 1, int(currentResult) * int(nextNumber))

        #Combine total posisble calculations, we use this in the next loop
        return addWays + multiplyWays

    #Start calculation check from the first number in our list, we will loop within the nested function
    findCalcs = findCalcs(1, inputNumbers[0])
    return findCalcs if findCalcs > 0 else False
    
#Loop through all calibration rows we need to check
for lineNo, testLine in enumerate(calibrationTest):
    #Start the calculation generation
    numberInput = testLine['numbers']
    correctAnswer = int(testLine['answer'])

    possibleAnswers = generateCalculations(numberInput, correctAnswer)

    #Print so we know it's working :D
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Checking line: {lineNo} ({current_time}) - {correctAnswer}: {numberInput}')

    #Add all found answers to the total answer calculations
    if possibleAnswers != False:
        answer = answer + correctAnswer

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")