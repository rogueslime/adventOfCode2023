# Split the cardsets into game identifier, an array of winning nums, and an array of pulled nums.
# As you walk down the array of pulled nums, compare each pulled num to the winning array. If there's a match,
# begin scoring. If score == 0, add 1; else, add 2.
# Assign point value to card. Once all cards have been read, total point values and add together.

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

#print(gameResults)
#print('Parsed: ',parseCard(gameResults[0][0]))
#print('Parsed: ',parseCard(gameResults[0][1]))
grandTotal = 0

for x in range (0, len(gameResults)):
    parsedWinners = parseCard(gameResults[x][0])
    #if(x % 10 == 0):
    #    print(x,' ', 'Winners: ',parsedWinners)
    parsedScratches = parseCard(gameResults[x][1])
    #if(x % 10 == 0):
    #    print(x,' ','Scratchies: ',parsedScratches)
    counter = 0
    score = 0
    #print('Index: ',x)

    for item in parsedScratches:
        if item in parsedWinners:
            #print('Matched: ', item)
            if score < 1:
                #print('Adding 1 to ',score)
                score += 1
            elif score > 0:
                #print(score)
                score = score * 2
            #if(x%10 == 0):
            #    print(x,' ',item,' ',score)
    grandTotal += score

print(grandTotal)