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


class GameState(enum.Enum):
    """
    Enum class for the states of the game.
    """
    MENU = enum.auto()
    PLAYING = enum.auto()
