import battlefieldmap
import unit
import tower
import enums

class GameController:
    """
    Class that controls the game's logic and objects
    """
    def __init__(self):
        self.running = True
        self.bf_map = battlefieldmap.BattleFieldMap()
        self.units = []
        self.towers = []

    def run(self):
        # Temporary function for testing TODO remove or improve
        for troop in self.units:
            troop.move()
        for tower in self.towers:
            target = tower.target
            if target is not None:
                if tower.in_range(target.cur_pos):
                        target = None
            if target is None:
                for troop in self.units:
                    if tower.in_range(troop.cur_pos):
                        tower.target = troop
                        break
            tower.shoot()


    def spawn_troop(self):
        # Temporary function for testing TODO Remove this function
        self.units.append(unit.Infantry(self.bf_map))

    def spawn_tower(self):
        # Temporary function for testing TODO Remove this function
        self.towers.append(tower.MachineGun(self.bf_map, (5,4)))

    def get_map(self):
        """
        Returns the battlefield map.
        """
        return self.bf_map

    def is_running(self):
        """
        Returns if the game is running.
        """
        return self.running
