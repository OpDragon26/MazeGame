import os

clears = ("cls","clear")

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
    direction += turn
    if direction < 0:
        return 3
    if direction > 3:
        return 0
    return direction

def update(map):
    mapPrint = createMapPrint(map)
    clear(1)
    print(mapPrint)