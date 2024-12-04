import functions
import random
from pynput.keyboard import Key, Listener
from copy import deepcopy as copy

directionOffsets = ((-2,0),(0,2),(2,0),(0,-2)) # (y,x)
directOffsets = ((-1,0),(0,1),(1,0),(0,-1)) # (y,x)

try:
    size = int(input("Input the size of the maze (must be odd and above 9): ")) # must be odd
except:
    size = 21

map = functions.createEmpty(size)

position = [2,2] # y,x
direction = random.randint(0,3) # from 0 to 3 clockwise, from the top

distance = 0
highestDistance = 0
furthestPoint = [2,2]

map[position[0]][position[1]] = "."

while True:
    for i in range(4):
        if map[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] == "#":
            map[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] = "."
            map[position[0] + directOffsets[direction][0]][position[1] + directOffsets[direction][1]] = "."

            position[0] += directionOffsets[direction][0]
            position[1] += directionOffsets[direction][1]

            distance += 1
            if distance > highestDistance:
                highestDistance = copy(distance)
                furthestPoint = copy(position)

            direction = functions.turn(direction,random.randint(-1,1))

            break
        else:
            direction = functions.turn(direction,1)
    else:
        wayBack = [map[position[0] + directOffsets[i][0]][position[1] + directOffsets[i][1]] == "." for i in range(4)].index(True)
        map[position[0]][position[1]] = ":"
        map[position[0] + directOffsets[wayBack][0]][position[1] + directOffsets[wayBack][1]] = ":"

        position[0] += directionOffsets[wayBack][0]
        position[1] += directionOffsets[wayBack][1]

        distance -= 1
    
    if position == [2,2]:
        map[furthestPoint[0]][furthestPoint[1]] = "F"
        break 

map = functions.replaceMap(map)

printedMap = copy(map)

printedMap[2][2] = "🯅"
functions.update(printedMap)

def on_press(key):
    global printedMap
    global map
    global position
    global furthestPoint

    if key == Key.down:
        if map[position[0] + 1][position[1]] in [" ","⬤"]:
            printedMap = copy(map)
            position[0] += 1
            printedMap[position[0]][position[1]] = "🯅"
        functions.update(printedMap)

    if key == Key.up:
        if map[position[0] - 1][position[1]] in [" ","⬤"]:
            printedMap = copy(map)
            position[0] -= 1
            printedMap[position[0]][position[1]] = "🯅"
        functions.update(printedMap)

    if key == Key.right:
        if map[position[0]][position[1] + 1] in [" ","⬤"]:
            printedMap = copy(map)
            position[1] += 1
            printedMap[position[0]][position[1]] = "🯅"
        functions.update(printedMap)

    if key == Key.left:
        if map[position[0]][position[1] - 1] in [" ","⬤"]:
            printedMap = copy(map)
            position[1] -= 1
            printedMap[position[0]][position[1]] = "🯅"
        functions.update(printedMap)
            
    if key == Key.esc: 
        return False
    
    if position == furthestPoint:
        functions.update(map)
        print("\n Congratulations, you successfully completed the maze! :D")
        return False
    
with Listener(on_press = on_press) as listener:
    listener.join()

    
    