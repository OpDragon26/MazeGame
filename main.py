import functions
import random
from pynput.keyboard import Key, Listener
from copy import deepcopy as copy
import time
import os

directionOffsets = ((-2,0),(0,2),(2,0),(0,-2)) # (y,x)
directOffsets = ((-1,0),(0,1),(1,0),(0,-1)) # (y,x)
sizes = ((9,9),(15,15),(21,21),(25,31),(31,41),(41,55),(45,75))

while True:
    difficulty = int(input("Enter difficulty (1-7): "))
    if difficulty == 0:
        size = int(input("Enter custom size (must be odd and larger than 7): ")).split("-")
        break
    elif difficulty == -1:
        highscores = open("highscores.txt","w")
        highscores.write('\n'.join(["99999" for i in range(7)]))
        highscores.close()
        print("Reset highscores.txt")
    elif difficulty > 0 and difficulty < 8:
        size = sizes[difficulty - 1]
        break
    else:
        print("\nDifficulty outside given range.")


map = functions.createEmpty(size)

position = [2,2] # y,x
direction = random.randint(0,3) # from 0 to 3 clockwise, from the top

distance = 0
highestDistance = 0
furthestPoint = [2,2]

map[position[0]][position[1]] = "."

startTime = time.time()

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

printedMap[2][2] = functions.playerCharacter

functions.update(printedMap)

exploredTiles = set()

def on_press(key):
    global printedMap
    global map
    global position
    global furthestPoint
    global difficulty

    if key == Key.down:
        if map[position[0] + 1][position[1]] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[0] += 1
            printedMap[position[0]][position[1]] = functions.playerCharacter
            exploredTiles.add((position[0],position[1],2))
        functions.update(printedMap)

    if key == Key.up:
        if map[position[0] - 1][position[1]] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[0] -= 1
            printedMap[position[0]][position[1]] = functions.playerCharacter
            exploredTiles.add((position[0],position[1],0))
        functions.update(printedMap)

    if key == Key.right:
        if map[position[0]][position[1] + 1] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[1] += 1
            printedMap[position[0]][position[1]] =functions.playerCharacter
            exploredTiles.add((position[0],position[1],1))
        functions.update(printedMap)

    if key == Key.left:
        if map[position[0]][position[1] - 1] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[1] -= 1
            printedMap[position[0]][position[1]] = functions.playerCharacter
            exploredTiles.add((position[0],position[1],3))
        functions.update(printedMap)
            
    if key == Key.esc:
        print("Exiting program...")
        return False
    
    if position == furthestPoint:
        for tile in exploredTiles:
            map[tile[0]][tile[1]] = functions.arrows[tile[2]]
        map[2][2] = functions.playerCharacter
        map[furthestPoint[0]][furthestPoint[1]] = functions.finishCharacter

        completionTime = time.time() - startTime

        highscores = open("highscores.txt","r")
        highscoreList = [float(score.replace("\n","")) for score in highscores.readlines()]
        
        newHighScore = False
        if highscoreList[difficulty - 1] > completionTime:
            newHighScore = True
            numBy = highscoreList[difficulty - 1] - completionTime
            
        highscores.close()

        if completionTime >= 100:
            completionTime = str(completionTime)[:len(str(int(completionTime))) + 2]
        else:
            completionTime = str(completionTime)[:4]

        functions.update(map)
        print(f"\nCongratulations, you completed a difficulty {difficulty} maze in {completionTime} seconds! :D")
        if newHighScore:
            if highscoreList[difficulty - 1] != 99999:
                print(f"New high score by {str(numBy)[:len(str(int(numBy))) + 2]} seconds!")
            highscoreList[difficulty - 1] = completionTime
            highscores = open("highscores.txt","w")
            highscores.write('\n'.join([str(highscoreList[i]) for i in range(7)]))
            highscores.close()

        return False
    
with Listener(on_press = on_press) as listener:
    listener.join()