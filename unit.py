import abc

import enums
import gameconstants as gc

class Unit(abc.ABC):
    """
    Abstract class for military unit
    """
    def __init__(self, bf_map):
        self.path = bf_map.path
        self.cur_pos = bf_map.get_enemy_camp_pos()
        self.next_pos = self.path[self.cur_pos]
        self.move_progress = 0
    
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

    def take_dmg(self, dmg, armor_pierc):
        """
        Reduces the unit's health and
        kills it if health goes to zero or bellow.
        """
        self.health -= dmg*(armor_pierc/self.armor)**gc.AP_EFFECTIVENESS
        if self.health <= 0:
            self.die()

    def damage_camp(self):
        """
        Makes so the unit damages the camp.
        """
        # TODO implement
        pass

    def die(self):
        """
        Make so the unit dies.
        """
        # TODO implement
        pass
    
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
        Returns the unit type
        """
        return self.unit_type


class Infantry(Unit):
    """
    Basic infantry unit
    """
    def __init__(self, bf_map):
        super().__init__(bf_map)
        self.max_health = gc.BASE_HEALTH
        self.health = self.max_health
        self.speed = gc.BASE_SPEED
        self.armor = gc.BASE_ARMOR
        self.unit_type = enums.Unit.INFANTRY
