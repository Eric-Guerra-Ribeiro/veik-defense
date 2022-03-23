import abc

import enums
import gameconstants as gc


class Tower(abc.ABC):
    """
    Abstract class for defense towers
    """
    def __init__(self, bf_map):
        self.bf_map = bf_map

class MachineGun(Tower):
    """
    Machine gun defense tower
    """
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.fire_rate = gc.BASE_FIRE_RATE
        self.dps = gc.BASE_TDMG
        self.size = 2
        self.range = gc.BASE_RANGE


