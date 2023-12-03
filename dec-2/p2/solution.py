# This code may not be fully refined as I did not simplify any functions or the main body after achieving a solution. I will edit this note
# if I find the time to do so!

gameResults = open('gameRecord.txt','r')
IDtracker = 0

# Grabs object color by checking the last value in the string as all colors end in a different character. Returns the number of colors
# rolled as an int as well as the color identifier in an array of size 2.
def checkColor(string):
    rollVal = ''
    for x in range(0,2):
        if string[x].isnumeric():
            rollVal+= string[x]
    if(string[-1] == 'e'):
        return([int(rollVal),'blue'])  
    if(string[-1] == 'd'):
        return([int(rollVal),'red'])  
    if(string[-1] == 'n'):
        return([int(rollVal),'green'])  
    
# Grabs game ID and returns it as an int.
def getGameID(string):
    gameID = ''

    # Utilize 5 as starting index as it's the end of the word 'Game ' with a space included allowing us to target only numbers
    for x in range (5,len(string)):
        if string[x].isnumeric():
            gameID += string[x]
    return int(gameID)

# Iterates through each line and separates them into the gameID and the gameset as a large string.
for line in gameResults:
    newLine = line.strip().split(': ')
    gameID = getGameID(newLine[0])
    gameValid = True
    newLine = newLine[1].split('; ')
    redMax = 0
    blueMax = 0
    greenMax = 0
    print(newLine)
    print(gameID)

    # Separates the gameset into individual games and validates them.
    for item in newLine:
        gameSet = item.split(', ')
        print('-',gameID,'-')
        for roll in gameSet:
            print(checkColor(roll)[0],': ',checkColor(roll)[1])
            if(checkColor(roll)[1] == 'red'):
                if checkColor(roll)[0] > redMax:
                    redMax = checkColor(roll)[0]
            if(checkColor(roll)[1] == 'blue'):
                if checkColor(roll)[0] > blueMax:
                    blueMax = checkColor(roll)[0]
            if(checkColor(roll)[1] == 'green'):
                if checkColor(roll)[0] > greenMax:
                    greenMax = checkColor(roll)[0]
        print('----------')
    
    # If code doesn't break the loop before this point, the gameset is valid and gameID should be added to the IDtracker.
    if gameValid == True:
        IDtracker += (greenMax*blueMax*redMax)

print(IDtracker)

        
        