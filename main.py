import functions
import random
from pynput.keyboard import Key, Listener

directionOffsets = ((-2,0),(0,2),(2,0),(0,-2)) # (y,x)
directOffsets = ((-1,0),(0,1),(1,0),(0,-1)) # (y,x)

size = int(input("Input the size of the maze (must be odd and above 9): ")) # must be odd

map = functions.createEmpty(size)

position = [2,2] # y,x
direction = random.randint(0,3) # from 0 to 3 clockwise, from the top

map[position[0]][position[1]] = "."

while True:
    for i in range(4):
        if map[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] == "#":
            map[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] = "."
            map[position[0] + directOffsets[direction][0]][position[1] + directOffsets[direction][1]] = "."

            position[0] += directionOffsets[direction][0]
            position[1] += directionOffsets[direction][1]

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
    
    if position == [2,2]:
        break 

map = functions.replaceMap(map)

functions.update(map)

if False:
    def on_press(key):
        if key == Key.down:
            pass
            
        if key == Key.esc: 
            return False
    
    with Listener(on_press=on_press) as listener:
        listener.join()

    
    