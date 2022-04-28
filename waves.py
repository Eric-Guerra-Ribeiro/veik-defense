import json
import random
import itertools

import enums
import pygameconstants as pgc

class Wave:
    """
    Enemy wave.
    """

    unit_type_converter = {
        "infantry" : enums.Unit.INFANTRY, "armored" : enums.Unit.ARMORED, "air_force" : enums.Unit.AIR_FORCE
    }

    def __init__(self, wave_info, game):
        self.game = game
        self.n_units_total = wave_info[0]["n_units"]
        self.spawned_units = 0
        self.spawn_rate = wave_info[0]["rate"]/pgc.FREQUENCY
        self.spawn_progress = 0
        self.units = self.units_list(wave_info[1])
        
    def units_list(self, units_weights):
        """
        Creates a list with the wave's units and their probability.
        """
        total = sum(units_weights.values())
        return [
            (self.unit_type_converter[unit_type], unit_weight/total)
            for unit_type, unit_weight in zip(units_weights.keys(), itertools.accumulate(units_weights.values()))
        ]
    
    def spawn(self):
        """
        Spawns troops at the right rate and probability
        """
        self.spawn_progress += self.spawn_rate
        while self.spawn_progress >= 1:
            self.spawn_progress -= 1
            self.game.spawn_unit(self.choose_unit())
            self.spawned_units += 1
    
    def is_over(self):
        """
        Returns if the wave should be over
        """
        return self.spawned_units >= self.n_units_total

    def choose_unit(self):
        """
        Chooses the type of unit to spawn
        """
        probability = random.random()
        for unit in self.units:
            if unit[1] >= probability:
                return unit[0]
        return self.units[-1][0]


class WaveController:
    """
    Class that controls the enemy waves.
    """
    def __init__(self, wave_json, game):
        self.game = game
        self.n_curr_wave = 0
        with open(wave_json, "r") as json_file:
            self.waves_list = json.load(json_file)
        self.n_waves = len(self.waves_list)
        self.wave = Wave(self.waves_list[0], game)
    
    def run(self):
        """
        Runs the wave controller
        """
        if self.wave.is_over():
            self.n_curr_wave += 1
            if self.n_curr_wave < self.n_waves:
                self.wave = Wave(self.waves_list[self.n_curr_wave], self.game)
            else:
                return
        self.wave.spawn()
