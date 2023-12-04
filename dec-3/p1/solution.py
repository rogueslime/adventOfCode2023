engineFile = open('engineSchematic.txt','r')

engineArray = []

# Build engineFile with each character having its own index in the array
count = 0
for row in engineFile:
    engineArray.append(row.strip())
    engineArray[count] = list(engineArray[count])
    count += 1

# ------------------------------------------------------------------------------------------------------------------------

# Function which seeks symbols that aren't numeric in any given array of characters and returns an array of their indices.
def seekMine(engineArray):
    count = 0
    arrayOfIndices = []
    for item in engineArray:
        if (item != '.' and not item.isnumeric()):
            arrayOfIndices.append(count)
        count += 1
    return arrayOfIndices

# Extract a number from an engineArray line based on a single coordinate.
def locateNumber(row, x, y):
    numBuilder = ''
    for q in range(y-2, y+3):
        if row[x][q].isnumeric():
            numBuilder += str(row[x][q])
    return numBuilder

# Sweep the engine array's specific coordinate for digestable numbers. Add the numbers to an array, convert those numbers to dots
# in our schematic copy, and then return both the valid number and the new engine array.
def digestNumber(engineArr, x, y):
    numeric = True
    currY = y
    validInt = ''
    #find start of number
    while True:
        if currY == 0:
            break
        if engineArr[x][currY-1].isnumeric():
            currY -= 1
        else:
            break
    #from start of number, read numeric characters
    while numeric:
        if engineArr[x][currY].isnumeric():
            validInt+=str(engineArr[x][currY])
            engineArr[x][currY] = '.'
        else:
            numeric = False
        if(currY>=len(engineArr[x])-1):
            break
        else:
            currY+=1

    return [validInt, engineArr]



# Sweep the original engine array on a particular coordinate and return all numbers which surround that coordinate.
# PROBLEM: Currently, the following would be considered a mine: 5..*... -- The code captures the 5.
def minesweep(engineArr, coord):
    nearbyMines = []
    for x in range(coord[0]-1, coord[0]+2):
        for y in range(coord[1]-1, coord[1]+2): # Only search coord[1]-1,coord[1]+1; start searching outward from there.
            #if x < 5:
            #    print(x,' ',y,' ',engineArr[x][y])
            if(engineArr[x][y].isnumeric()):
                results = digestNumber(engineArr, x, y)
                engineArr = results[1]
                nearbyMines.append(results[0])
    return [nearbyMines, engineArr]
            

# Construct an array of tuples. Each tuple is a set of coordinates which points to a 'mine'
mineIndices = []
count = 0
for row in engineArray:
    mineIndices += map(lambda x:[count, x], seekMine(row))
    count+=1
print('Number of mine indices: ',len(mineIndices))

# Minesweep all mine coordinates. Creates a matrix; each index contains a list of valid numbers which were on that mine.
mines = []
for index in mineIndices:
    results = minesweep(engineArray, index)
    engineArray = results[1]
    #results[0].append(index) # Utilize this line to add the index to each set of mines allowing for spot-checking of the engine file
    mines.append(results[0])
print(mines)
print('Len of mines array',len(mines))

# Add all of the valid numbers together to get our puzzle result.
grandTotal = 0
for mineList in mines:
    for mines in mineList:
        grandTotal = grandTotal + int(mines)
print('Grand total: ',grandTotal)
