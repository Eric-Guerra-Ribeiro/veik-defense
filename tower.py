import abc

import enums
import gameconstants as gc


class Tower(abc.ABC):
    """
    Abstract class for defense towers
    """

    def __init__(self, bf_map, pos):
        self.bf_map = bf_map
        self.pos = pos
        self.target = None
        self.range = gc.BASE_RANGE
    
    def in_range(self, pos):
        dist2 = (self.pos[0] - pos[0])**2 + (self.pos[1] - pos[1])**2
        if dist2 <= self.range**2:
            return True
        return False

    def shoot(self):
        if self.target is not None:
            self.target.take_dmg(self.dmg, 1)

    @property
    def target(self):
        return self.target

    @target.setter
    def target(self, target):
        self.target = target


class MachineGun(Tower):
    """
    Machine gun defense tower
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG
        self.size = gc.BASE_SIZE
