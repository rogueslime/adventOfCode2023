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
    #gameResults[counter][1],gameResults[counter][2] = gameResults[counter][1].split(' | ') Changed this - trying to split into indexes
    # [counter][1] and [counter][2] but 2 is OOB
    counter += 1
    if counter == 5: break

def parseCard(cardSet):
    counter = 0
    print('Cardset: ',cardSet)
    numBuilder = ''
    numArray = []
    for x in range(0, len(cardSet)):
        if (cardSet[x].isnumeric()):
            numBuilder+=str(cardSet[x])
        else:
            if len(numBuilder)>0: numArray.append(numBuilder)
            numBuilder = ''
    return numArray

print(gameResults)
print('Parsed: ',parseCard(gameResults[0][1][0]))
print('Parsed: ',parseCard(gameResults[0][1][1]))


