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
        self.update_price = 0

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

class MachineGunLvl1(Tower):
    """
    Machine gun defense tower.
    """

    price = gc.BASE_PRICE
    fire_rate = gc.BASE_FIRE_RATE * 10
    dmg = gc.BASE_TDMG

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos


        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MACHINE_GUN_LVL1
        self.cant_shoot.append(enums.Unit.AIR_FORCE)
        self.update_price = gc.BASE_PRICE

class MachineGunLvl2(Tower):
    """
    Machine gun defense tower Level 2.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = 12*gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG*1.3
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MACHINE_GUN_LVL2
        self.cant_shoot.append(enums.Unit.AIR_FORCE)
        self.update_price = 3 *gc.BASE_PRICE

class MachineGunLvl3(Tower):
    """
    Machine gun defense tower Level 3.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = 15*gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG*1.5
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MACHINE_GUN_LVL3
        self.cant_shoot.append(enums.Unit.AIR_FORCE)


class CannonLvl1(Tower):
    """
    Rocket Launcher defense tower Level 1.
    """

    price = gc.BASE_PRICE * 2
    fire_rate = gc.BASE_FIRE_RATE * 1.5
    dmg = gc.BASE_TDMG * 5

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.CANNON_LVL1
        self.update_price = gc.BASE_PRICE * 2

class CannonLvl2(Tower):
    """
    Rocket Launcher defense tower Level 2.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = gc.BASE_FIRE_RATE * 1.8
        self.dmg = gc.BASE_TDMG * 7
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.CANNON_LVL2
        self.update_price = gc.BASE_PRICE * 6
    
class CannonLvl3(Tower):
    """
    Rocket Launcher defense tower Level 2.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = gc.BASE_FIRE_RATE * 1.9
        self.dmg = gc.BASE_TDMG * 10
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.CANNON_LVL3

class AntiTankLvl1(Tower):
    """
    Armored defense tower.
    """

    price = gc.BASE_PRICE * 10
    fire_rate = gc.BASE_FIRE_RATE
    dmg = gc.BASE_TDMG * 15

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.ANTI_TANK_LVL1
        self.cant_shoot.append(enums.Unit.AIR_FORCE)
        self.update_price = gc.BASE_PRICE * 10

class AntiTankLvl2(Tower):
    """
    Armored defense tower.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.fire_rate = 1.3 * gc.BASE_FIRE_RATE
        self.range = 1.5 * gc.BASE_RANGE
        self.dmg = gc.BASE_TDMG * 25
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.ANTI_TANK_LVL2
        self.cant_shoot.append(enums.Unit.AIR_FORCE)


class MissileLvl1(Tower):
    """
    Air force defense tower.
    """

    price = gc.BASE_PRICE * 8
    fire_rate = gc.BASE_FIRE_RATE
    dmg = gc.BASE_TDMG * 10

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.range = 1.5*gc.BASE_RANGE
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MISSILE_LVL1
        self.cant_shoot.append(enums.Unit.INFANTRY)
        self.cant_shoot.append(enums.Unit.ARMORED)
        self.update_price = gc.BASE_PRICE * 8

class MissileLvl2(Tower):
    """
    Air force defense tower.
    """

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos

        self.range = 2.0 * gc.BASE_RANGE
        self.fire_rate = 1.4 * gc.BASE_FIRE_RATE
        self.dmg = gc.BASE_TDMG * 15
        self.size = gc.BASE_SIZE
        self.tower_type = enums.Tower.MISSILE_LVL2
        self.cant_shoot.append(enums.Unit.INFANTRY)
        self.cant_shoot.append(enums.Unit.ARMORED)
