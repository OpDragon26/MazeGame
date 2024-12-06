# Command Line Maze
A maze game played in the terminal

## Requirements
 ● pynput<br/>
 ● Run the program directly from its directory (cd path then python3 main.py instead of python3 path/main.py)
 
### Windows specific
 ● PowerShell/cmd font: MS Gothic<br/>
 ● Should not be run in VSCode
 
### Linux specific
 ● A terminal emulator in which pynput works (for me this was Tilda) or VSCode

## Controls
 ● movement: arrow keys, WASD, Vim controls<br/>
 ● difficulty selection:<br/>
    1  - 9 by 9<br/>
    2  - 15 by 15<br/>
    3  - 21 by 21<br/>
    4  - 25 by31<br/>
    5  - 31 by 41<br/>
    6  - 41 by 55<br/>
    7  - 45 by 75<br/>
    0  - custom size (format: height-width, numbers must be odd and above 7) for example: 7-51<br/>
   -1 - reset highscores<br/>
   -2 - quit program (KeyboardInterrupt doesn't work during difficulty selection)<br/>
 ● exit: esc<br/>
 
### Maze generation algorithm
 ● Slightly modified Aldous-Broder
