import enum

class Terrain(enum.Enum):
    """
    Enum class for the types of terrain.
    """
    GRASS = enum.auto()
    ROAD = enum.auto()
    ALLY_CAMP = enum.auto()
    ENEMY_CAMP = enum.auto()


