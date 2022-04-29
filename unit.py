import abc

import enums
import gameconstants as gc
import screenpos

class Unit(abc.ABC):
    """
    Abstract class for military unit
    """
    def __init__(self, bf_map):
        self.ally_camp = bf_map.ally_camp
        self.path = bf_map.path
        self.cur_pos = bf_map.get_enemy_camp_pos()
        self.next_pos = self.path[self.cur_pos]
        self.move_progress = 0
        self.alive = True
        self.pierc_dict = {}
    
    def move(self):
        """
        Moves the unit across the map.
        """
        self.move_progress += self.speed
        while self.move_progress >= 1:
            self.move_progress -=1
            self.cur_pos = self.next_pos
            self.next_pos = self.path[self.cur_pos]
            # Reached camp
            if self.cur_pos == self.next_pos:
                self.damage_camp()
                break

    def take_dmg(self, dmg, tower_type):
        """
        Reduces the unit's health and
        kills it if health goes to zero or bellow.
        """
        if tower_type in self.pierc_dict.keys():
            armor_pierc = self.pierc_dict[tower_type]
        else:
            armor_pierc = 1

        self.health -= dmg*(armor_pierc/self.armor)
        if self.health <= gc.EPSILON:
            self.die()

    def damage_camp(self):
        """
        Makes so the unit damages the camp.
        """
        self.ally_camp.take_dmg(self.dmg)

    def die(self):
        """
        Make so the unit dies.
        """
        self.alive = False
    
    def get_move_prog(self):
        """
        Returns move progress.
        """
        return self.move_progress
    
    def get_cur_pos(self):
        """
        Returns the position that the unit is in.
        """
        return self.cur_pos

    def get_next_pos(self):
        """
        Returns the position that the unit is moving to.
        """
        return self.next_pos

    def get_health_perc(self):
        """
        Returns the unit's health in percentage.
        """
        return self.health/self.max_health
    
    def get_unit_type(self):
        """
        Returns the unit type.
        """
        return self.unit_type
    
    def get_unit_subtype(self):
        """
        Returns the unit subtype.
        """
        return self.unit_subtype
    
    def get_direction(self):
        """
        Returns the direction that the unit is heading towards.
        """
        vec_direction = (screenpos.Coords(*self.next_pos) - screenpos.Coords(*self.cur_pos)).get()
        if vec_direction == (0, 0) or vec_direction == (0,1):
            return enums.Direction.RIGHT
        elif vec_direction == (-1, 0):
            return enums.Direction.UP
        elif vec_direction == (0, -1):
            return enums.Direction.LEFT
        elif vec_direction == (1, 0):
            return enums.Direction.DOWN


class Infantry(Unit):
    """
    Abstract infantry unit
    """
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.armor = gc.BASE_ARMOR
        self.max_health = gc.BASE_HEALTH
        self.unit_type = enums.Unit.INFANTRY
        self.speed = gc.BASE_SPEED

class InfLvl1(Infantry):
    """
    Infantry unit Lvl 1
    """
    resource_reward = gc.BASE_RESOURCE_REWARD
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.health = self.max_health
        self.armor = gc.BASE_ARMOR
        self.unit_subtype = enums.UnitSubtype.INFANTRY_LVL1
        self.dmg = gc.BASE_DMG

class InfLvl2(Infantry):
    """
    Infantry unit Lvl 2
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 1
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.health = self.max_health
        self.armor = gc.BASE_ARMOR * 2
        self.unit_subtype = enums.UnitSubtype.INFANTRY_LVL2
        self.dmg = gc.BASE_DMG * 1.2

class InfLvl3(Infantry):
    """
    Infantry unit Lvl 3
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 2
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.health = self.max_health
        self.armor = gc.BASE_ARMOR * 2.5
        self.unit_subtype = enums.UnitSubtype.INFANTRY_LVL3
        self.dmg = gc.BASE_DMG * 1.5

class InfLvl4(Infantry):
    """
    Infantry unit Lvl 4
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 2
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.health = self.max_health
        self.armor = gc.BASE_ARMOR * 3.0
        self.unit_subtype = enums.UnitSubtype.INFANTRY_LVL4
        self.dmg = gc.BASE_DMG * 1.8

class AirForce(Unit):
    """
    Abstract air force unit
    """
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.max_health = gc.BASE_HEALTH
        self.health = self.max_health
        self.speed = gc.BASE_SPEED * 2
        self.unit_type = enums.Unit.AIR_FORCE
        self.pierc_dict = {enums.Tower.MISSILE_LVL1 : 3}

class AirForceLvl1(AirForce):
    """
    Air Force unit Lvl 1
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 2
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.health = self.max_health
        self.armor = gc.BASE_ARMOR * 2
        self.unit_subtype = enums.UnitSubtype.AIR_FORCE_LVL1
        self.dmg = gc.BASE_DMG
        self.pierc_dict = {enums.Tower.MISSILE_LVL1 : 3,
                           enums.Tower.MISSILE_LVL2 : 3}
    
class AirForceLvl2(AirForce):
    """
    Air Force unit Lvl 2
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 2.5
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.health = self.max_health
        self.armor = gc.BASE_ARMOR * 4
        self.unit_subtype = enums.UnitSubtype.AIR_FORCE_LVL2
        self.dmg = gc.BASE_DMG * 1.5
        self.pierc_dict = {enums.Tower.MISSILE_LVL1 : 2,
                           enums.Tower.MISSILE_LVL2 : 2.5}

class Armory(Unit):
    """
    Abstract armory unit
    """
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.max_health = gc.BASE_HEALTH
        self.health = self.max_health
        self.speed = gc.BASE_SPEED * 0.7
        self.unit_type = enums.Unit.ARMORED

class ArmoryLvl1(Armory):
    """
    Armory unit Lvl 1
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 2.5
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.armor = gc.BASE_ARMOR * 4
        self.unit_subtype = enums.UnitSubtype.ARMORED_LVL1
        self.dmg = gc.BASE_DMG * 2
        self.pierc_dict = {enums.Tower.ANTI_TANK_LVL1 : 2,
                           enums.Tower.ANTI_TANK_LVL2 : 2,
                           enums.Tower.MACHINE_GUN_LVL1 : 0.3,
                           enums.Tower.MACHINE_GUN_LVL2 : 0.3,
                           enums.Tower.MACHINE_GUN_LVL3 : 0.3}

class ArmoryLvl2(Armory):
    """
    Armory unit Lvl 2
    """
    resource_reward = gc.BASE_RESOURCE_REWARD * 4
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.armor = gc.BASE_ARMOR * 6
        self.unit_subtype = enums.UnitSubtype.ARMORED_LVL2
        self.dmg = gc.BASE_DMG * 2.5
        self.pierc_dict = {enums.Tower.ANTI_TANK_LVL1 : 2,
                           enums.Tower.ANTI_TANK_LVL2 : 2,
                           enums.Tower.MACHINE_GUN_LVL1 : 0.2,
                           enums.Tower.MACHINE_GUN_LVL2 : 0.2,
                           enums.Tower.MACHINE_GUN_LVL3 : 0.2}