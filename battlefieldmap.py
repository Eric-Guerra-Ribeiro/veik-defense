from chess import BB_FILE_MASKS
import enums
import gameconstants as gc
import utils

class BattleFieldMap:
    """
    Map of the battlefield.
    """
    def __init__(self):
        self.width = gc.MAP_WIDTH
        self.height = gc.MAP_HEIGHT
        # Default map grid for now
        # TODO Improve this
        paths_pos = [
            (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4),
            (4, 4), (5, 4), (6, 4), (6, 5), (6, 6), (5, 6), (4, 6), (3, 6),
            (2, 6), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9),
            (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (7, 12), (7,12), (7,13),
            (7, 14), (6, 14), (5, 14), (4, 14), (3, 14), (3, 13), (3, 12), (2, 12), (1, 12)
        ]
        self.ally_camp_pos = (0, 12)
        self.enemy_camp_pos = (7, 0)
        self.grid = [self.width*[enums.Terrain.GRASS] for _ in range(self.height)]
        self.grid[self.ally_camp_pos[0]][self.ally_camp_pos[1]] = enums.Terrain.ALLY_CAMP
        self.grid[self.enemy_camp_pos[0]][self.enemy_camp_pos[1]] = enums.Terrain.ENEMY_CAMP
        for pos in paths_pos:
            self.grid[pos[0]][pos[1]] = enums.Terrain.ROAD
        
        self.path = self.find_path()

    def find_path(self):
        """
        Does a search in the grid to find the unit's path.
        """
        cur_pos = self.enemy_camp_pos
        prev_pos = cur_pos
        map_dim = (self.height, self.width)
        path = {}
        # TODO Add stop condition if it doesn't get to ally base
        while cur_pos != self.ally_camp_pos:
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
    
    def is_grass_square(self, left, top, n):
        """
        Returns if a square of size n is in grass
        """
        for x in range(left, left + n + 1):
            for y in range(top, top + n + 1):
                pos = (x,y)
                if self.get_terrain(pos) != enums.Terrain.GRASS:
                    return False
        return True
