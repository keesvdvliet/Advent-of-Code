#Set the current day and puzzle data
day_no = 2
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
processedData = []
minDiff = int(1)
maxDiff = int(3)

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:

            #Clean the line
            dataRow = line.strip()

            #Split the numbers into two columns (we split on spaces)
            dataCol = dataRow.split(" ")

            #Add the full report array to the processed data array
            processedData.append(dataCol)

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Create an function that checks if a report is either True or False
def reportIsSafe(report):
    #Create a list so the array gets treated as integers
    report = list(map(int, report))

    #Set the safe value to False as a starter
    isSafe = False

    #Check if the report is either increasing or decreasing within the maximum limits
    increasing = all(0 < report[i+1] - report[i] <= maxDiff for i in range(len(report) - minDiff))
    decreasing = all(0 < report[i] - report[i+1] <= maxDiff for i in range(len(report) - minDiff))
        
    #Return the if the increase or decreasing values are good
    if( increasing or decreasing ):
        return True
    else:
        return False

#Loop through the proccessed data
for report in processedData:
    #Check if this single report is safe
    safeStatus = reportIsSafe(report)

    #If the report is safe add one to the answer
    if safeStatus == True:
        answer = answer + 1

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")