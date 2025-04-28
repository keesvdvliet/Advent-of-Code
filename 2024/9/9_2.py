#Import dependicies
from datetime import datetime

#Set the current day and puzzle data
day_no = 9
puzzle_no = 2
dataset_no = 1
dataset_no = "test"

#Set the dataset path
dataset_path = f"./{day_no}/data/input_{dataset_no}.txt"

#Answer storage
answer = 0

#Set some variables
diskMap = []

#Read the dataset
try:
    #Read all the data in the dataset TXT file and put it into the data variable
    with open(dataset_path, "r") as dataset:

        #Loop through all the lines in the data
        for line in dataset:
            #Clean the line
            dataRow = line.strip()

            #Split the characters
            diskMap = list(dataRow)

#Throw error if we can't read the dataset for some reason
except Exception as errorCode:
    print(f"Err: {errorCode}")

#Loop through the disk mapping and generate the file/freespace blocks
curFileID = 0
fragmentedDisk = []
diskBlocks = []
tempStorage = {}

for fileLoc, itemLen in enumerate(diskMap):
    writtenData = int(0)
    itemLen = int(itemLen)

    if fileLoc % 2 == 0: #Write a file
        file = { "id": curFileID, "size": itemLen }
        diskBlocks.append(file)
        curFileID+=1
    else: #Write free space
        freespace = { "id": ".", "size": itemLen }
        diskBlocks.append(freespace)

#Loop through the mirrored disk while there is still free space between the datablocks
for mirrorIndex, currentData in enumerate(diskBlocks[::-1]):
    #Set the non-mirrored index of this block and get the first available free-space
    originalIndex = len(diskBlocks) - 1 - mirrorIndex

    #Update timer
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    #Check if the current data is a file
    if(currentData['id'] != "."):
        fileSize = int(currentData['size'])

        #Find the first available free space on the disk
        freespaceIndex = next(
            (i for i, block in enumerate(diskBlocks) if block['id'] == '.' and block['size'] >= fileSize),
            False #Returns index of free space, if none is available returns fals
        )

        #Continue is there is a free space and it is earlier in the string than the original index
        if freespaceIndex != False and freespaceIndex < originalIndex:
            #Check the length of the free space we found
            freeSpaceLen = int(diskBlocks[freespaceIndex]['size'])

            if freeSpaceLen == fileSize: #Easy: swap the file and the free space arround
                diskBlocks[freespaceIndex] = currentData
                diskBlocks[originalIndex] = { "id": ".", "size": freeSpaceLen }

                #Sends update signal
                print(f'Move: { current_time }')
            elif freeSpaceLen > fileSize:
                #We add the file to a temp storage, the index-key is the location after the files need to be injected
                if freespaceIndex not in tempStorage:
                    tempStorage[freespaceIndex] = []
                tempStorage[freespaceIndex].append(currentData)

                #Update the free space with the remaining size
                sizeDifference = freeSpaceLen - fileSize
                diskBlocks[freespaceIndex] = { "id": ".", "size": sizeDifference }
                diskBlocks[originalIndex] = { "id": ".", "size": fileSize }

                #Sends update signal
                print(f'Temp: { current_time }')
            else:
                #Sends update signal
                print(f'Skip: { current_time }')    
    else:
        #Sends update signal
        print(f'Skip: { current_time }')

#Loop through the temp storage and place it in the correct spot on the disk
keyManipulator = 0
sortedTempStorage = dict(sorted(tempStorage.items())) #Sort the temp storage first

for insertAfter in sortedTempStorage:
    #Files in temp. storage container
    insertFiles = tempStorage[insertAfter]
    insertLocation = insertAfter

    #Update timer
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    #Loop through files to insert
    for tempFile in insertFiles:
        insertKey = insertLocation + keyManipulator
        diskBlocks.insert(insertKey, tempFile)
        keyManipulator+=1

        #Send update
        print(f'Move from temp: { current_time }')

for file in diskBlocks:
    writtenData = int(0)
    fileSize = int(file['size'])

    while( fileSize > writtenData ):
        fragmentedDisk.append(file['id'])
        writtenData += 1

#Loop through the fragmented disk to calculate the checksum values
for position, fileID in enumerate(fragmentedDisk):
    if fileID != ".":
        checkSum = int(position) * int(fileID)
        answer = answer + checkSum

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")