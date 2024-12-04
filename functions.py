import os

clears = ["cls","clear"]
dir = [1,-1]
turns = ["right","left"]

def createEmpty(size):
    map = [[" " for j in range(size)] for i in range(size)]
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
    direction += dir[turns.index(turn)]
    if direction < 0:
        return 3
    if direction > 3:
        return 0
    return direction