import pygame

import pygameconstants as pgc
import enums
import screenpos
class Art:
    """
    Class that handles all art assets of the game (visual and sounds).
    """
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.map_img = self.make_map_surface(game.get_map())
        self.unit_imgs = self.make_unit_imgs()
        self.tower_imgs = self.make_tower_imgs()

    def make_map_surface(self, bf_map):
        """
        Creates a surface with an image corresponding to the map.
        """
        map_img = pygame.Surface((pgc.GRID_SIZE*bf_map.width, (pgc.GRID_SIZE*bf_map.height)))
        terrain_color = {
            enums.Terrain.ROAD: pgc.ROAD_COLOR, enums.Terrain.ALLY_CAMP: pgc.ALLY_CAMP_COLOR,
            enums.Terrain.ENEMY_CAMP: pgc.ENEMY_CAMP_COLOR, enums.Terrain.GRASS: pgc.GRASS_COLOR
        }
        for i in range(bf_map.height):
            for j in range(bf_map.width):
                pygame.draw.rect(map_img, terrain_color[bf_map.get_terrain((i, j))],
                                 pygame.Rect(j*pgc.GRID_SIZE, i*pgc.GRID_SIZE,
                                 pgc.GRID_SIZE, pgc.GRID_SIZE))
        return map_img

    def make_unit_imgs(self):
        """
        Creates surfaces with an image of each unit type.
        """
        inf_sur = pygame.Surface((pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(inf_sur, pgc.WHITE, (pgc.GRID_SIZE//2, pgc.GRID_SIZE//2), pgc.GRID_SIZE//2)
        return {enums.Unit.INFANTRY: inf_sur}

    def make_tower_imgs(self):
        """
        Creates surfaces with an image of each tower type.
        """
        mgun_sur = pygame.Surface((pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(mgun_sur, pgc.ALLY_CAMP_COLOR, (pgc.GRID_SIZE//2, pgc.GRID_SIZE//2), pgc.GRID_SIZE//2)
        cannon_sur = pygame.Surface((pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(cannon_sur, pgc.YELLOW, (pgc.GRID_SIZE//2, pgc.GRID_SIZE//2), pgc.GRID_SIZE//2)
        return {enums.Tower.MACHINE_GUN: mgun_sur, enums.Tower.CANNON: cannon_sur}

    def hp_bar(self, pos, perc_hp):
        """
        Draws a unit's hp bar if not full.
        """
        if perc_hp < 1:
            pygame.draw.rect(self.screen, pgc.RED, pygame.Rect(*pos, perc_hp*pgc.GRID_SIZE, pgc.HP_HEIGHT))

    def draw(self):
        """
        Draws all elements in screen.
        """
        self.screen.fill(pgc.BLACK)
        self.screen.blit(self.map_img, pgc.MAP_CORNER_POS)
        for unit in self.game.units:
            unit_pos = screenpos.unit_pos_in_scrn(unit.cur_pos, unit.next_pos, unit.move_progress)
            self.screen.blit(
                self.unit_imgs[unit.get_unit_type()], unit_pos
            )
        for unit in self.game.units:
            unit_pos = screenpos.unit_pos_in_scrn(unit.cur_pos, unit.next_pos, unit.move_progress)
            self.hp_bar(unit_pos, unit.get_health_perc())
        for tower in self.game.towers:
            tower_pos = screenpos.unit_pos_in_scrn(tower.pos, tower.pos, 1)
            self.screen.blit(
                self.tower_imgs[tower.get_tower_type()], tower_pos
            )
        pygame.display.flip()
