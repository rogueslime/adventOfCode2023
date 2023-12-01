calibrationFile = open('calibrationFile.txt','r')

#numLines = 0
sumtotal = 0
for line in calibrationFile:
    #print(line)
    #numLines += 1
    calibratedVal = ''
    for c in line:
        if(c.isnumeric()):
            print(c)
            calibratedVal += str(c)
            break
    for c in line[::-1]:
        if(c.isnumeric()):
            print(c)
            calibratedVal += str(c)
            break
    sumtotal+=int(calibratedVal)
    print((calibratedVal)," - Running total: ",sumtotal)

#print('Lines read: ',numLines)