# Split the cardsets into game identifier, an array of winning nums, and an array of pulled nums.
# As you walk down the array of pulled nums, compare each pulled num to the winning array. If there's a match, initiate a counter.
# Once the walk is finished, begin to call the card parsing method again sequentially for the number of cards required. Each method should
# return an array of card numbers that that method call earned.
# Example: Card 1 returns a counter of 3. Initialize card parsing for card 2, 3, and 4. The array returned as a result will contain all of
# the game IDs earned after card 1.

gameFile = open('cardResults.txt','r')

# Creates an array of results. Each result is an array; the [index][0th] index is the card identifier. The [index][1st] index 
# is another array containing card results. [index][1][0] holds the winning numbers, while [index][1][1] holds the numbers scratched.
gameResults = []
counter = 0
for line in gameFile:
    if counter == 0: print(line)
    gameResults.append(line.strip().split(': '))
    [gameResults[counter][0]].append(gameResults[counter])
    gameResults[counter][0],gameResults[counter][1] = gameResults[counter][1].split(' | ') # Changed this - trying to split into indexes
    # [counter][1] and [counter][2] but 2 is OOB
    counter += 1

# Parses a cardset, which is a single string of scores. Reads the scores; for every sequence of ints, build an int string. When we reach
# a character that isn't an int, append the int string to a list and clear our int string. Once we've parsed the whole list, return the
# array.
def parseCard(cardSet):
    counter = 0
    #print('Cardset: ',cardSet)
    numBuilder = ''
    numArray = []
    for x in range(0, len(cardSet)):
        #print('Cardset target: ',cardSet[x], ' ',numBuilder)
        #print(x,' ',len(cardSet)-1)
        if (cardSet[x].isnumeric()):
            numBuilder+=str(cardSet[x])
        if((not cardSet[x].isnumeric()) or x == len(cardSet)-1):
            if len(numBuilder)>0: numArray.append(numBuilder)
            numBuilder = ''
    return numArray

# Recursively evaluate game results. Initialize method with an array of every index in gameResults. Afterwards, the method will
# recursively call itself if the scratcher won additional tickets by building an array of the IDs succeeding that ticket based on the
# amount of matched scratchoffs.
def evaluateGameResults(gameIDArray):
    print('cycling...: ',len(gameIDArray))
    idArray = []
    #print(len(gameIDArray),' Array: ',gameIDArray)
    for id in gameIDArray:
        winningVals = parseCard(gameResults[int(id)][0])
        scratchedVals = parseCard(gameResults[int(id)][1])
        currentID = id
        for val in scratchedVals:
            if val in winningVals:
                #print('matchy: ',scratchedVals,' ',winningVals)
                currentID += 1
                idArray.append(currentID)
    #print('IDArray: ',idArray)
    #if(len(idArray) > 0):
    #    idArray.append(evaluateGameResults(idArray))
    if(len(idArray) > 0):
        return (idArray + evaluateGameResults(idArray))
    else:
        return idArray

resultsArray = evaluateGameResults(range(0,len(gameResults)))
print(resultsArray)
print('Final ticket count: ',len(resultsArray))