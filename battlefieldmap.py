import json

import enums
import gameconstants as gc
import utils
from allycamp import AllyCamp

class BattleFieldMap:
    """
    Map of the battlefield.
    """
    def __init__(self, map_json):
        self.width = gc.MAP_WIDTH
        self.height = gc.MAP_HEIGHT
        with open(map_json, "r") as json_file:
            map_dict = json.load(json_file)
        paths_pos = map_dict["paths"]
        self.ally_camp_pos = tuple(map_dict["ally_camp"])
        self.ally_camp = AllyCamp(self.ally_camp_pos)
        self.enemy_camp_pos = tuple(map_dict["enemy_camp"])

        self.grid = [self.width*[enums.Terrain.GRASS] for _ in range(self.height)]
        self.is_cell_empty = [self.width*[True] for _ in range(self.height)]
        self.grid[self.ally_camp_pos[0]][self.ally_camp_pos[1]] = enums.Terrain.ALLY_CAMP
        self.is_cell_empty[self.ally_camp_pos[0]][self.ally_camp_pos[1]] = False
        self.grid[self.enemy_camp_pos[0]][self.enemy_camp_pos[1]] = enums.Terrain.ENEMY_CAMP
        self.is_cell_empty[self.enemy_camp_pos[0]][self.enemy_camp_pos[1]] = False
        for pos in paths_pos:
            self.grid[pos[0]][pos[1]] = enums.Terrain.ROAD
            self.is_cell_empty[pos[0]][pos[1]] = False
        
        self.path = self.find_path()

    def find_path(self):
        """
        Does a search in the grid to find the unit's path.
        """
        cur_pos = self.enemy_camp_pos
        prev_pos = cur_pos
        map_dim = (self.height, self.width)
        path = {}
        count = 0
        while cur_pos != self.ally_camp_pos:
            count += 1
            i, j = cur_pos
            for index in ((i+1,j), (i-1, j), (i, j+1), (i, j-1)):
                if (
                    utils.valid_index(index, map_dim)
                    and self.grid[index[0]][index[1]] != enums.Terrain.GRASS
                    and index != prev_pos
                ):
                    prev_pos = cur_pos
                    cur_pos = index
                    path[prev_pos] = cur_pos
                    break
            if count > map_dim[0]*map_dim[1]:
                raise Exception("Invalid Map Layout")
        path[self.ally_camp_pos] = self.ally_camp_pos
        return path

    def get_next_pos(self, cur_pos):
        """
        Returns the next position along the path.
        """
        return self.path[cur_pos]
    
    def get_terrain(self, pos):
        """
        Returns the terrain in a given position.
        """
        return self.grid[pos[0]][pos[1]]

    def get_enemy_camp_pos(self):
        """
        Returns the position of an enemy camp.
        """
        return self.enemy_camp_pos
    
    def is_cells_square_empty(self, row, column, n):
        """
        Returns if a square of size n is empty.
        """
        for x in range(row, row + n):
            for y in range(column, column + n):
                if not self.is_cell_empty[x][y]:
                    return False
        return True


    def ocupy_cells_square(self, row, column, n):
        """
        Makes so the cells in the square of size n are not empty.
        """
        for x in range(row, row + n):
            for y in range(column, column + n):
                self.is_cell_empty[x][y] = False
    
    def desocupy_cells_square(self, row, column, n):
        """
        Makes so the cells in the square of size n are empty.
        """
        for x in range(row, row + n):
            for y in range(column, column + n):
                self.is_cell_empty[x][y] = True
