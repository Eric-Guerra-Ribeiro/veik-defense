import battlefieldmap
from gameconstants import BASE_RESOURCE
import unit
import tower
import enums
import waves


class GameController:
    """
    Class that controls the game's logic and objects
    """

    def __init__(self):
        self.reset()
        
    
    def reset(self):
        self.running = True
        self.go = False
        self.bf_map = battlefieldmap.BattleFieldMap()
        self.units = []
        self.towers = []
        self.selected_tower = enums.Tower.MACHINE_GUN_LVL1
        self.resources = BASE_RESOURCE
        self._game_state = enums.GameState.GRACE_PERIOD
        self.waves = waves.WaveController("waves/classic.json", self)

    def run(self):
        self.waves.run()
        for index, troop in enumerate(self.units):
            if not troop.alive:
                self.increase_resources(self.units[index].resource_reward)
                del self.units[index]
            else:
                troop.move()
        for tower in self.towers:
            tower.find_target(self.units)
            tower.shoot()
            
        if not self.bf_map.ally_camp.alive:
            self.go = True
    
    def increase_resources(self, nmb):
        self.resources += nmb
    
    def decrease_resources(self, nmb):
        self.resources -= nmb

    def spawn_unit(self, subtype):
        """
        Spawns a unit of a given subtype
        """
        if subtype == enums.UnitSubtype.INFANTRY_LVL1:
            self.units.append(unit.InfLvl1(self.bf_map))
        elif subtype == enums.UnitSubtype.INFANTRY_LVL2:
            self.units.append(unit.InfLvl2(self.bf_map))
        elif subtype == enums.UnitSubtype.INFANTRY_LVL3:
            self.units.append(unit.InfLvl3(self.bf_map))
        elif subtype == enums.UnitSubtype.INFANTRY_LVL4:
            self.units.append(unit.InfLvl4(self.bf_map))
        elif subtype == enums.UnitSubtype.ARMORED_LVL1:
            self.units.append(unit.ArmoryLvl1(self.bf_map))
        elif subtype == enums.UnitSubtype.ARMORED_LVL2:
            self.units.append(unit.ArmoryLvl2(self.bf_map))
        elif subtype == enums.UnitSubtype.AIR_FORCE_LVL1:
            self.units.append(unit.AirForceLvl1(self.bf_map))
        elif subtype == enums.UnitSubtype.AIR_FORCE_LVL2:
            self.units.append(unit.AirForceLvl2(self.bf_map))

    def get_map(self):
        """
        Returns the battlefield map.
        """
        return self.bf_map

    @property
    def running(self):
        """
        Returns if the game is running.
        """
        return self._running
    
    @running.setter
    def running(self, is_running):
        self._running = is_running

    @property
    def game_state(self):
        return self._game_state
    
    @game_state.setter
    def game_state(self, state):
        self._game_state = state

    def are_cells_empty(self, map_cell, n):
        return self.bf_map.is_cells_square_empty(*map_cell, n)

    def ocupy_cells(self, map_cell, n):
        self.bf_map.ocupy_cells_square(*map_cell, n)
