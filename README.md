# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

py __main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycles              (source code for game)
  +-- game              (specific game classes)
    +-- casting         (Actor, Cast, Cycle, End, and Score classes)
    +-- directing       (The director of the game)
    +-- scripting       (specialized backend operations that dictate the behavior of game's action inputs, the control of actors, drawing actors, handling collisions, moving actors, and general script for collecting all actions)
    +-- services        (Keyboard and Video Services)
    +-- shared          (Color and Point classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (set constants to be used universally)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Luke McLean
* lucas.w.mclean@gmail.com
