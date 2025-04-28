#Set the current day and puzzle data
day_no = 1
puzzle_no = 1
dataset_no = 1

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
leftRow = []
rightRow = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:

            #Clean the line
            dataRow = line.strip()

            #Split the numbers into two columns
            dataCol = dataRow.split()

            #Check if we have two numbers before proceeding otherwise this all breaks down (blegh)
            if len(dataCol) == 2:
                #Put the numbers into the correct arrays
                leftRow.append(int(dataCol[0]))
                rightRow.append(int(dataCol[1]))

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Sort both arrays from low to high
leftRow.sort()
rightRow.sort()

#Loop through the leftRow array (enumerate adds an index/value to the array)
for index, value in enumerate(leftRow):
    #Set the values
    valueLeft = value
    valueRight = rightRow[index]

    #Calculate the distance between the values
    valueDistance = valueLeft - valueRight

    #Check if value is not negetive, if so make it positive :)
    if( valueDistance < 0 ):
        valueDistance = valueDistance * -1
    
    #Add the distance to the answer value
    answer = answer + valueDistance

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")