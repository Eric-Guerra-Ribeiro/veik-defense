# Veik Defense

Tower defense game based in a military invasion. This project was an assignment for the CES-22 course (OOP) at Aeronautics Institute of Technology (ITA).

- [**Setup**](#setup)
- [**Assets**](#assets)
- [**Running The Game**](#running-the-game)
- [**Instructions**](#instructions)
- [**Architecture**](#Architecture)


## Setup

### Create python virtual environment
  ```
  virtualenv venv
  ```

### Activate virtual environment (Windows)
  ```
  cd venv/Scripts/
  ./activate
  ```

### Activate virtual environment (Ubuntu)
  ```
  source venv/bin/activate
  ```


### Dependency installation
  ```
  pip install -r requirements.txt
  ```


## Assets
The team would like to thank every artist that made their art public for use at this game.
### Backgrounds
Game Over Background: https://www.publicdomainpictures.net/en/view-image.php?image=175816&picture=verdun-war-cemetery
Main Menu: https://www.insideover.com/war/images-from-a-war-zone-military-photographers-and-the-vietnam-war.html
Win Background: https://qz.com/411672/the-allies-embargoed-germanys-surrender-in-world-war-ii-until-an-ap-reporter-defied-them/
### Sound
Fibra de Herói Song: https://www.youtube.com/watch?v=PIpYx4wfqcg

### Sprites
Terrain Sprites: https://opengameart.org/
Tower Sprites: https://opengameart.org/
Enemy Sprites: https://www.kenney.nl/assets/


## Running the game

Run the main file after all packages were successfully installed.

  ```
  python3 main.py
  ```

## Instructions

To play the game, choose the map and either the mode Campaign (8 waves of increasing difficulty) or Endless (infinite waves).

Each defense tower has a different damage (D) and fire rate (F). Resource towers have profit gains (P) and production rate (R).

To deploy a tower, click on the type at the right side and click at where you would like to deploy it (only at green squares).

To update a tower, click at "UPDATE" at the bottom side and click at the tower you would like to update. The costs for updates of defense towers are the same cost of the tower deployment for the first upgrade and three times that cost for the second upgrade. For the resource toer, the update cost is five times the cost of deployment.

To destroy a tower, click at "DESTROY" at the bottom side and click at the tower you would like to destroy. The square for the tower will be released and you will get half of the total cost invested at the tower back.

## Architecture
The main idea behind the code is creatting "main" classes that handle each of the major subsystems of the game (game logic, input system, graphics/screen).

It was done this way because passing one object of one of this classes as an argument makes it far easier to get the necessary information and to make this subsystems interact then passing each variable separately.

Another important idea is using inheritance and abstract classes. Abstract classes for the units, towers and resource factories were created with the methods of each entity. And based on inheritance, the children classes only set the stats, reusing a lot of code.
### Files
 - ```allycamp.py```: Class for the Ally Camp, controlling its health.
 - ```art.py```: Shows the assets on screen and playing the background music.
 - ```battlefieldmap.py```: Class that represents the battlefield map. It has the path taken by the units and tells which cells are occupied by the towers or factories.
 - ```enums.py```: Enums for game states, types of tiles, units, towers, factories, etc.
 - ```gameconstants.py```: All the constants related to the game balance, such as base stats.
 - ```gamecontroller.py```: Class that controlls the game. It manages the changes of game states, spawns enemy units, runs the game's logic, etc.
 - ```inputs.py```: Classes for input systems via mouse, such as a button class and a board (like the battlefield map). Handles all the inputs from the player, keyboard and mouse, and triggers the corresponding actions such as changing the game state.
 - ```main.py```: Main file. Has the game loop and initializes the objects of the main classes, such as the Game Controller, Input System and Art Manager.
 - ```pygameconstants.py```: Constants for positions in the screen, sizes of the screen, buttons and grid cell, colors and other constants related to displaying the game on the screen.
 - ```resourceFactory.py```: Abstract class for a resource factory and its children.
 - ```screenpos.py```: Functions that help find the position of some object on the screen.
 - ```tower.py```: Abstract class for a defensive tower and its children.
 - ```unit.py```: Abstract class for an enemy unit and its children.
 - ```utils.py```: Miscelleanous functions that help with the implementation.
 - ```waves.py```: Classes for waves and one that controlls the change of waves.
