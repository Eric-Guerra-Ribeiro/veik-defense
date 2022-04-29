# Veik Defense

Tower defense game based in a military invasion. This project was an assignment for the CES-22 course (OOP) at Aeronautics Institute of Technology (ITA).

- [**Setup**](#setup)
- [**Assets**](#assets)
- [**Running The Game**](#running-the-game)
- [**Instructions**](#instructions)


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