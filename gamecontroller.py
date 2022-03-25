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
        for index, troop in enumerate(self.units):
            if not troop.alive:
                del self.units[index]
            else:
                troop.move()
        for tower in self.towers:
            tower.find_target(self.units)
            tower.shoot()


    def spawn_troop(self):
        # Temporary function for testing TODO Remove this function
        self.units.append(unit.Infantry(self.bf_map))

    def spawn_tower(self, pos):
        # Temporary function for testing TODO Remove this function
        self.towers.append(tower.MachineGun(self.bf_map, pos))

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
