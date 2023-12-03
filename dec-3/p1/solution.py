engineFile = open('engineSchematic.txt','r')

engineArray = []
count = 0
for row in engineFile:
    engineArray.append(row.strip())
    engineArray[count] = list(engineArray[count])
    count += 1

print(engineArray[0])