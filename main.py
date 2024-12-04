import functions
import variables
import random
from pynput.keyboard import Key, Listener
size = 9 # must be odd

map = functions.createEmpty(size)

generatorPosition = [2,2] # y,x
generatorDirection = random.randint(0,3) # from 0 to 3 clockwise, from the top

map[generatorPosition[0]][generatorPosition[1]] = " "

while True:
    if map[generatorPosition[0] + variables.directionOffsets[generatorDirection][0]][generatorPosition[1] + variables.directionOffsets[generatorDirection][1]] == "#":
        map[generatorPosition[0] + variables.directionOffsets[generatorDirection][0]][generatorPosition[1] + variables.directionOffsets[generatorDirection][1]] = " "
        map[generatorPosition[0] + variables.directOffsets[generatorDirection][0]][generatorPosition[1] + variables.directOffsets[generatorDirection][1]] = " "

    break 

functions.update(map)

def on_press(key):
    if key == Key.down:
        pass
         
    if key == Key.esc: 
        return False
 
with Listener(on_press=on_press) as listener:
    listener.join()

    
    