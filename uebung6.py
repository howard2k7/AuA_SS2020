import time

showsteps = 1

numberOfColumns = 20
numberOfRows = 10

emptyMarker = ' '
filledMarker = 'o'
wallMarker = 'x'

filename = 'field.txt'

def generateField(nOC, nOR):

    if nOC > 4 and nOR > 4:
        newField = [[emptyMarker for i in range(nOC)] for j in range(nOR)]
        for a in range(0, nOR):
            newField [a][3] = wallMarker
            newField [a] [nOC-5] = wallMarker
        for i in range(0,nOC):
            newField[1][i] = wallMarker
            newField[nOR-2] [i] = wallMarker
        return newField
    else:
        return -1

def printField(toPrint):
    for a in range(0, len(toPrint)):
        print(''.join(str(i) for i in toPrint[a]))


def floodFill(start_C,start_R, toFill):
    if toFill[start_C][start_R] == wallMarker:
        return
    if toFill[start_C][start_R] == filledMarker:
        return
    else:
        toFill[start_C][start_R] = filledMarker
        if showsteps:
            printField(toFill)
            time.sleep(1)

    if (start_C - 1) >= 0:
        floodFill(start_C - 1, start_R,toFill)
    if (start_C + 1) < (len(toFill)):
        floodFill(start_C + 1, start_R, toFill)
    if (start_R - 1) >= 0:
        floodFill(start_C, start_R - 1, toFill)
    if (start_R + 1) < (len(toFill[start_C])):
        floodFill(start_C, start_R + 1, toFill)
    return

def readMaze():
    newMaze = []
    with open(filename) as fp:
        line = fp.readline()
        count = 0
        while line:
            newMaze.append([])
            line = line.strip('\n')
            for i in line:
                newMaze[count].append(i)
            line = fp.readline()
            count+= 1
    return newMaze

def fillToBoarder(toFill, startingPoints):
    # Nur für das Ursprungsfeld. Um beliebige Muster zu füllen müsste es nach Wall Markern suchen
    for point in startingPoints:
        for a in range(2,8):
           toFill[a][point[1]] = filledMarker
        for a in range(4,15):
            toFill[point[0]][a] = filledMarker

    return toFill

def fillToBoarderExt(toFill, startingPoints):
    for point in startingPoints:
        toFill[point[0]][point[1]] = filledMarker;






# Übung 6: a-c Feld generieren
'''
printField(generateField(numberOfColumns, numberOfRows))
'''

#Übung 6: d
'''
me = generateField(numberOfColumns, numberOfRows)
me = fillToBoarder(me,[(5,5),(5,10)])
printField(me)
'''

#Übung 7:
'''
me = readMaze()
floodFill(1,4,me)
printField(me)
'''
'''
me = generateField(20,15)
floodFill(10,10,me)
printField(me)
'''