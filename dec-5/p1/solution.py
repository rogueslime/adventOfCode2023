# Start with our initial seeds. Ingest those seeds and store them in an array for processing.

# destination range, source range, range length

# Creating a decoded map with key:value pairs would take too long and be too large of a data structure. Instead,
# complete the problem using arithmetic. For a seed, see if it's larger than the minimum source range length and smaller than
# maximum source range length. If it is, calculate the destination seed by adding the difference of the source minimum and the
# initial seed value. and pass to the next map.

# Takes a seed and converts it by the arithmetic outlined in the line. Returns the converted seed.
def conversionMath(seed, line):
    arithmeticValues = line.split(' ')
    if (seed == 'seeds:'):
        return seed
    seed = int(seed)
    #print('lower limit: ',int(arithmeticValues[1]))
    #print('upper limit: ',(int(arithmeticValues[1]) + int(arithmeticValues[2])))
    if (seed >= int(arithmeticValues[1]) and seed <= (int(arithmeticValues[1]) + int(arithmeticValues[2]))):
        print('this seed stinks: ',seed)
        seed = int(arithmeticValues[0]) + (seed - int(arithmeticValues[1]))
    return seed

with open('mapFile.txt','r') as mapFile:
    targetSeeds = mapFile.readline().split(' ')    # capture first line as target seeds and move forward
    print('targets: ',targetSeeds)
    for line in mapFile:
        strippedLine = line.strip()
        if strippedLine == '': continue       # if line is empty, pass this iteration
        if (not strippedLine[0].isnumeric()): continue    # if line is non-numeric, pass this iteration

        # If we make it here, we've made it to a new map

        for x in range(0,len(targetSeeds)): # Pass all seeds and perform arithmetic, then modify those seeds.
            newSeed = conversionMath(targetSeeds[x], strippedLine)
            #print('newMap: ',newSeed)   # else print out the line
            targetSeeds[x] = newSeed # Replace each seed with the modified seed
        print(targetSeeds)

print('Final Seeds!')
lowestSeed = int(targetSeeds[1])
for seed in targetSeeds:
    if seed == 'seeds:': continue
    seed = int(seed)
    if seed<lowestSeed:
        lowestSeed = int(seed)

print(lowestSeed)