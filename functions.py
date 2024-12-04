import os

clears = ("cls","clear")

replaceFrom = (".",":","+","#")
replaceTo = (" "," ","#","#")

def createEmpty(size):
    map = [["#" for j in range(size)] for i in range(size)]
    for i in range(size):
        map[0][i] = "+"
        map[size - 1][i] = "+"
        map[i][0] = "+"
        map[i][size - 1] = "+"
    return map

def createMapPrint(map):
    return '\n'.join([' '.join(row) for row in map])

def clear(osClear): # 0 - windows, 1 - linux
    os.system(clears[osClear])

def turn(direction,turn):
    return (direction + turn + 4) % 4

def update(map):
    mapPrint = createMapPrint(map)
    clear(1)
    print(mapPrint)

def replace(thing, rfrom, rto):
    return rto[rfrom.index(thing)]

def replaceMap(map):
    return [[replace(tile, replaceFrom, replaceTo) for tile in row ] for row in map]