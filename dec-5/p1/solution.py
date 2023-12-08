# Start with our initial seeds. Ingest those seeds and store them in an array for processing.

# Create a function to decode maps. Each time an empty newline is detected run the map decoding function
# on the next set of data. Create a function to apply this map to the seed array. Iteratively do this until
# we have reached the end of the file, then print out our array of converted seeds.

with open('mapFile.txt','r') as mapFile:
    targetSeeds = mapFile.readline()    # capture first line as target seeds and move forward
    for line in mapFile:
        if line == '\n': continue       # if line is empty, pass this iteration
        else: print('newline: ',line)   # else print out the line
    