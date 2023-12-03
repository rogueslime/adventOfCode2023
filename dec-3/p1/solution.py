engineFile = open('engineSchematic.txt','r')

engineArray = []
count = 0

# Build engineFile with each character having its own index in the array
for row in engineFile:
    engineArray.append(row.strip())
    engineArray[count] = list(engineArray[count])
    count += 1

# Seek symbols which are not numeric in any given line of the engineFile
def seekMine(engineArray):
    count = 0
    arrayOfIndices = []
    for item in engineArray:
        if (item != '.' and not item.isnumeric()):
            arrayOfIndices.append(count)
        count += 1
    return arrayOfIndices

# Seek mines in each row and return an array of indices
for row in engineArray:
    print(seekMine(row))
