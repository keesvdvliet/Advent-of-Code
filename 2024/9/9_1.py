#Import dependicies
from datetime import datetime

#Set the current day and puzzle data
day_no = 9
puzzle_no = 1
dataset_no = 1
# dataset_no = "test"

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
diskBlocks = []
fragmentationString = ""

for fileLoc, itemLen in enumerate(diskMap):
    writtenData = int(0)
    itemLen = int(itemLen)

    if fileLoc % 2 == 0: #Write a file
        while( itemLen > writtenData ):
            diskBlocks.append(curFileID)
            fragmentationString = fragmentationString + str( curFileID )
            writtenData += 1
        curFileID+=1
    else: #Write free space
        while( itemLen > writtenData ):
            diskBlocks.append(".")
            fragmentationString = fragmentationString + "."
            writtenData += 1

#Loop through the mirrored disk while there is still free space between the datablocks
for mirrorIndex, moveData in enumerate(diskBlocks[::-1]):
    #Create string from the moveData
    moveDataStr = str(moveData)

    #Set the non-mirrored index of this block and get the first available free-space
    originalIndex = len(diskBlocks) - 1 - mirrorIndex

    try:
        freeSpaceLoc = diskBlocks.index(".")
    except ValueError as ve:
        break #There is not a single free space

    #Split the fragmentation check
    checkFragmentation = [frag for frag in fragmentationString.split(".") if frag != ""] #Create a list with only the fragmented datablocks

    #Update timer
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
        
    if( len(checkFragmentation) > 1 ): #Once we do not have any fragemented datablocks left, stop moving data
        if( moveDataStr != "." ):
            #Put the data in the first free space
            updatedFragString = fragmentationString.replace(".", moveDataStr, 1) #Replaces the first occurence of a free space in the fragmentation string
            diskBlocks[freeSpaceLoc] = moveData #Replaces the first occurence of a free space in the disk blocks

            #Reverse the string and add free space at the location of the data
            updatedFragString = updatedFragString[::-1]
            reversedMoveData = moveDataStr[::-1]
            updatedFragString = updatedFragString.replace(reversedMoveData, ".", 1)

            #Puts the updated value as free space
            diskBlocks[originalIndex] = "."

            #Reverse the string again and update the disk blocks
            fragmentationString = updatedFragString[::-1]

            #Sends update signal
            print(f'Move: { current_time }')
        else:
            #Sends update signal
            print(f'Skip: { current_time }')
    else:
        #Stop the process
        print(f'Defragmentation process done: { current_time }')
        break

#Loop through the diskBlocks to calculate the checksum values
for position, fileID in enumerate(diskBlocks):
    if fileID != ".":
        checkSum = int(position) * int(fileID)
        answer = answer + checkSum

#Print the answer
print(f"Answer for day { day_no } puzzle { puzzle_no }: {answer}")