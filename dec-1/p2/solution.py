calibrationFile = open('calibrationFile.txt','r')

#Sloppy method to convert text values to ints; returns 10 otherwise
def elvishConversion(text):
    if ('one' in text.lower()):
        return 1
    elif ('two' in text.lower()):
        return 2
    elif ('three' in text.lower()):
        return 3
    elif ('four' in text.lower()):
        return 4
    elif ('five' in text.lower()):
        return 5
    elif ('six' in text.lower()):
        return 6
    elif ('seven' in text.lower()):
        return 7
    elif ('eight' in text.lower()):
        return 8
    elif ('nine' in text.lower()):
        return 9
    else:
        return 10

    


numLines = 0
sumtotal = 0
for line in calibrationFile:
    print(line)
    numLines += 1
    runningText = ''

    calibratedVal = ''

    for c in line:
        if(c.isnumeric()):
            print('FW ANSWER FOUND: ',c)
            runningText = ''
            calibratedVal += str(c)
            break
        else:
            runningText+=str(c)
            print('Forwards: ',runningText)
            if(elvishConversion(runningText)<10):
                print('FW ANSWER FOUND: ',runningText)
                calibratedVal += str(elvishConversion(runningText))
                runningText = ''
                break
            
    for c in line[::-1]:
        if(c.isnumeric()):
            print('BACK ANSWER FOUND: ',c)
            runningText = ''
            calibratedVal += str(c)
            break
        else:
            runningText=str(c) + runningText
            print('Backwards: ',runningText)
            if(elvishConversion(runningText)<10):
                print('BACK ANSWER FOUND: ',runningText)
                calibratedVal += str(elvishConversion(runningText))
                runningText = ''
                break
            
    sumtotal+=int(calibratedVal)
    print((calibratedVal)," - Running total: ",sumtotal)

print('Lines read: ',numLines)