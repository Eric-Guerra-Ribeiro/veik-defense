import abc

import enums
import gameconstants as gc


class Tower(abc.ABC):
    """
    Abstract class for defense towers.
    """

    def __init__(self, bf_map, pos):
        self.bf_map = bf_map
        self.pos = pos
        self._target = None
        self.range = gc.BASE_RANGE
        self.shoot_progress = 0
        self.cant_shoot = []

    def in_range(self, pos):
        dist2 = (self.pos[0] - pos[0])**2 + (self.pos[1] - pos[1])**2
        return dist2 <= self.range**2

    def shoot(self):
        """
        Shoots target (unit).
        """
        if self._target is not None:
            self.shoot_progress += self.fire_rate
            while self.shoot_progress >= 1:
                self.shoot_progress -= 1
                self._target.take_dmg(self.dmg, self.get_tower_type())
            if not self._target.alive:
                self.target = None

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, desired_target):
        self._target = desired_target

    def find_target(self, units):
        if self.target is not None:
            if not self.in_range(self.target.cur_pos):
                self.target = None
        if self.target is None:
            for troop in units:
                if self.in_range(troop.cur_pos) and troop.get_unit_type() not in self.cant_shoot:
                    self.target = troop
                    break

    def get_tower_type(self):
        return self.tower_type


class MachineGun(Tower):
    """
    Machine gun defense tower.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = 10*gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MACHINE_GUN
        self.cant_shoot.append(enums.Unit.AIR_FORCE)


class Cannon(Tower):
    """
    Rocket Launcher defense tower.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = gc.BASE_FIRE_RATE*2
        self.dmg = gc.BASE_TDMG * 5
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.CANNON

class AntiTank(Tower):
    """
    Armored defense tower.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG * 15
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.ANTI_TANK
        self.cant_shoot.append(enums.Unit.AIR_FORCE)

class Missile(Tower):
    """
    Air force defense tower.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.range = 1.5*gc.BASE_RANGE
        self.fire_rate = gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG * 10
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MISSILE
        self.cant_shoot.append(enums.Unit.INFANTRY)
        self.cant_shoot.append(enums.Unit.ARMORED)