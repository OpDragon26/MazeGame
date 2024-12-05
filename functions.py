import os

system = (1,0)[os.name == "nt"]
clears = ("cls","clear")

finishCharacter = "✕"
playerCharacter = "웃"

arrows = ["↑","→","↓","←"]

disallowedCharacters = (arrows + [playerCharacter],[playerCharacter])[system]

replaceFrom = (".",":","+","#","F")
replaceTo = (" "," ","#","#",finishCharacter)

def createEmpty(size):
    map = [["#" for j in range(size[1])] for i in range(size[0])]
    for i in range(size[1]):
        map[0][i] = "+"
        map[size[0] - 1][i] = "+"
    for i in range(size[0]):
        map[i][0] = "+"
        map[i][size[1] - 1] = "+"
    return map

def createMapPrint(map):
    map = '\n'.join([joinRow(row) for row in map])
    for i in range(len(map)):
        if map[i] == playerCharacter:
            map[i - 1] = ""
        break
    return map

def clear(osClear): # 0 - windows, 1 - linux
    os.system(clears[osClear])

def turn(direction,turn):
    return (direction + turn + 4) % 4

def update(map):
    mapPrint = createMapPrint(map)
    clear(system)
    print(mapPrint)

def replace(thing, rfrom, rto):
    return rto[rfrom.index(thing)]

def replaceMap(map):
    return [[replace(tile, replaceFrom, replaceTo) for tile in row ] for row in map]

def joinRow(row):
    rowString = ""
    for i in range(len(row)):
        try:
            if row[i + 1] in disallowedCharacters:
                rowString += row[i]
            else:
                rowString += (row[i] + " ")
        except:
            rowString += (row[i] + " ")
    return rowString

def isOdd(num):
    return num % 2 == 1