import functions
import random
from pynput.keyboard import *
from copy import deepcopy as copy
import time

directionOffsets = ((-2,0),(0,2),(2,0),(0,-2)) # (y,x)
directOffsets = ((-1,0),(0,1),(1,0),(0,-1)) # (y,x)
sizes = ((9,9),(15,15),(21,21),(25,31),(31,41),(41,55),(45,75))

while True:
    try:
        difficulty = int(input("Enter difficulty (1-7): "))
    except:
        continue
    if difficulty == 0:
        try:
            size = [int(x) for x in input("Enter custom size (height-width) (must be odd and larger than 7): ").split("-")]
        except: 
            print("Input is in an incorrect format. The correct format is height-width\n")
            continue
        if functions.isOdd(size[0]) and functions.isOdd(size[1]) and size[0] > 6 and size[1] > 6:
            break
        else:
            print("Specified size does not fit the requirements\n")
    elif difficulty == -1:
        highscores = open("highscores.txt","w")
        highscores.write('\n'.join(["99999" for i in range(7)]))
        highscores.close()
        print("Reset highscores.txt")
        exit()
    elif difficulty > 0 and difficulty < 8:
        size = sizes[difficulty - 1]
        break
    elif difficulty == -2:
        exit()
    else:
        print("Difficulty outside given range\n")

map = functions.createEmpty(size)
distances = map[1]
map = map[0]

position = [2,2] # y,x
direction = random.randint(0,3) # from 0 to 3 clockwise, from the top

highestDistance = 0
furthestPoint = [2,2]

map[position[0]][position[1]] = "."

iterations = 0

visitedTiles = set()

while True:
    iterations += 1
    visitedTiles.add((position[0],position[1]))

    direction = functions.turn(direction,random.randint(-1,1))
    if map[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] != "+":
        if map[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] == "#":
            map[position[0] + directOffsets[direction][0]][position[1] + directOffsets[direction][1]] = "."
            distances[position[0] + directionOffsets[direction][0]][position[1] + directionOffsets[direction][1]] = distances[position[0]][position[1]] + 1

            if distances[position[0]][position[1]] + 1 > highestDistance:
                furthestPoint = [position[0] + directionOffsets[direction][0],position[1] + directionOffsets[direction][1]]
                highestDistance = distances[position[0]][position[1]] + 1

        position = [position[0] + directionOffsets[direction][0],position[1] + directionOffsets[direction][1]]
        map[position[0]][position[1]] = "."
        
        if len(visitedTiles) == int((len(map) - 3)/2) * int((len(map[0]) - 3)/2):
            map[furthestPoint[0]][furthestPoint[1]] = "F"
            break

startTime = time.time()

map = functions.replaceMap(map)

functions.update(map)

printedMap = copy(map)

position = [2,2]
printedMap[2][2] = functions.playerCharacter

functions.update(printedMap)

exploredTiles = set()

def on_press(key):
    global printedMap
    global map
    global position
    global furthestPoint
    global difficulty

    if key in [Key.down,KeyCode.from_char("s"),KeyCode.from_char("j")]:
        if map[position[0] + 1][position[1]] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[0] += 1
            printedMap[position[0]][position[1]] = functions.playerCharacter
            exploredTiles.add((position[0],position[1],2))
        functions.update(printedMap)

    if key in [Key.up,KeyCode.from_char("w"),KeyCode.from_char("k")]:
        if map[position[0] - 1][position[1]] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[0] -= 1
            printedMap[position[0]][position[1]] = functions.playerCharacter
            exploredTiles.add((position[0],position[1],0))
        functions.update(printedMap)

    if key in [Key.right,KeyCode.from_char("d"),KeyCode.from_char("l")]:
        if map[position[0]][position[1] + 1] in [" ",functions.finishCharacter]:
            printedMap = copy(map)
            position[1] += 1
            printedMap[position[0]][position[1]] = functions.playerCharacter
            exploredTiles.add((position[0],position[1],1))
        functions.update(printedMap)

    if key in [Key.left,KeyCode.from_char("a"),KeyCode.from_char("h")]:
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

        if difficulty != 0:
            print(f"\nCongratulations, you completed a difficulty {difficulty} maze in {completionTime} seconds! :D")
        else:
            print(f"\nCongratulations, you completed a custom {size[0]} by {size[1]} maze in {completionTime} seconds! :D")
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