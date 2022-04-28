import enum


class Terrain(enum.Enum):
    """
    Enum class for the types of terrain.
    """
    GRASS = enum.auto()
    ROAD = enum.auto()
    ALLY_CAMP = enum.auto()
    ENEMY_CAMP = enum.auto()


class Unit(enum.Enum):
    """
    Enum class for the types of military units.
    """
    INFANTRY = enum.auto()
    ARMORED = enum.auto()
    AIR_FORCE = enum.auto()


class Tower(enum.Enum):
    """
    Enum class for the types of towers.
    """
    MACHINE_GUN = enum.auto()
    CANNON = enum.auto()
    ANTI_TANK = enum.auto()
    MISSILE = enum.auto()
    COAL_FACTORY = enum.auto()
    NUCLEAR_PLANT = enum.auto()

    def succ(self):
        v = self.value + 1
        try:   
            return Tower(v)
        except:
            return Tower(1)

class GameState(enum.Enum):
    """
    Enum class for the states of the game.
    """
    MENU = enum.auto()
    PLAYING = enum.auto()

class Direction(enum.Enum):
    """
    Enum class for the direction of the movement of the unit.
    """
    RIGHT = enum.auto()
    UP = enum.auto()
    LEFT = enum.auto()
    DOWN = enum.auto()
