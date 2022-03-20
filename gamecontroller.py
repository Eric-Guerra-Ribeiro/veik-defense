import battlefieldmap
import unit
import enums

class GameController:
    """
    Class that controls the game's logic and objects
    """
    def __init__(self):
        self.running = True
        self.bf_map = battlefieldmap.BattleFieldMap()
        self.units = []

    def run(self):
        # Temporary function for testing TODO remove or improve
        for troop in self.units:
            troop.move()

    def spawn_troop(self):
        # Temporary function for testing TODO Remove this function
        self.units.append(unit.Infantry(self.bf_map))

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
