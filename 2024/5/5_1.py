#Set the current day and puzzle data
day_no = 5
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
rawData = []
printerOrders = []
ruleSet = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:
            #Clean the line
            dataRow = line.strip()

            #Add line to the data input array
            rawData.append(dataRow)

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Split te rawData into two datasets
splitIndex = rawData.index('')
printerOrders = rawData[splitIndex:]
rawRules = rawData[0:splitIndex]

#Create the rule set list
for singleRule in rawRules:
    ruleSet.append(singleRule.split("|"))

#Page order checker
def validatePrintOrder(input):
    def ruleChecker(staticIndex, checkIndex, previousResult):
        #Final result value
        finalResult = previousResult

        #If the previous result was False, we stop the loop and return a False result
        if previousResult == False:
            return finalResult

        #We reached the end, all is well, return a True result
        if staticIndex >= pageCount:
            return finalResult

        #Keep on checking
        num1 = str(input[staticIndex])
        num2 = str(input[checkIndex])
        selectRule = [rule for rule in ruleSet if num1 in rule and num2 in rule] #Fetch the rule we are checking against

        #Check if we meet the requirements of the rule
        resultStorage = False
        if selectRule:
            for rule in selectRule:
                if rule[0] == num1 and rule[1] == num2:  #Numbers are in the correct order, yay
                    resultStorage = True
        else:  #No rules, allow progression
            resultStorage = True

        #Update the checker if the result was True
        if resultStorage == True:
            checkIndex = int(checkIndex) + 1

            if checkIndex > pageCount:
                checkIndex = int(staticIndex) + 2
                staticIndex = int(staticIndex) + 1

        #Update the final result
        finalResult = resultStorage

        # Re-run the checker
        return ruleChecker(staticIndex, checkIndex, finalResult)

    #Start the checker
    pageCount = len(input) - 1
    return ruleChecker(0, 1, True)

#Loop through the print orders
for orderNo, order in enumerate(printerOrders):
    if( order != "" ): #Lil' failsafe for empty lines
        #Get each page number in a list and set the no. of pages
        pages = order.split(',')

        #Run check function
        orderIsAccepted = validatePrintOrder(pages)
        print(f"Order({orderNo}) { order } accepted? {orderIsAccepted}") 

        #If the order is accepted we need to fetch the middle number
        if orderIsAccepted == True:
            orderLength = len(pages)
            middleIndex = int((((int( orderLength ) - 1) / 2))) #This is ugly but it works. Be removing 1 we create an even number, we divide this by 2 and because the list count start at 0 this is the middle item :D

            #Fetch the value and add it to the answer
            middleValue = pages[middleIndex]
            answer = answer + int(middleValue)

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")