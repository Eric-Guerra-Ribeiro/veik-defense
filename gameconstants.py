import pygameconstants as pgc

# Map/Grid Constants
MAP_HEIGHT = 9
MAP_WIDTH = 16
BASE_SIZE = 1

# Units Stats
BASE_HEALTH = 1.0
BASE_DMG = 0.2
BASE_SPEED = 1/pgc.FREQUENCY # 1 square/s
BASE_ARMOR = 1.0
BASE_ARMOR_PIERC = 1.0
AP_EFFECTIVENESS = 2.0
BASE_SCORE_REWARD = 100
BASE_RESOURCE_REWARD = 100

# Tower Stats
BASE_FIRE_RATE = 1/(2 * pgc.FREQUENCY)
BASE_TDMG = 0.10
BASE_RANGE = 3.0
BASE_PRICE = 500

# Economy Stats
BASE_RESOURCE = 1000

# Wave Stats
WAVE_GRACE_PERIOD = 5 # seconds
WAVE_GRACE_PROGRESS = 1/(WAVE_GRACE_PERIOD*pgc.FREQUENCY)

EPSILON = 1e-6
