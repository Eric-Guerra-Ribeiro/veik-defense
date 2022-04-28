import pygame
import random

import pygameconstants as pgc
import gameconstants as gc
import enums
import screenpos
import utils

class Art():
    """
    Class that handles all art assets of the game (visual and sounds).
    """
    def __init__(self, screen, game, inputs_):
        self.screen = screen
        self.game = game
        self.input = inputs_
        self.map_img = self.make_map_surface(game.get_map())
        self.unit_imgs = self.make_unit_imgs()
        self.tower_imgs = self.make_tower_imgs()
        self.regular_font = pygame.font.Font('freesansbold.ttf', 30)
        self.big_font = pygame.font.Font('freesansbold.ttf', 50)
        self.tower_sounds = self.make_tower_sounds()

    def make_map_surface(self, bf_map):
        """
        Creates a surface with an image corresponding to the map.
        """
        terrainsprites = []
        for i in range(pgc.GRASS_SPRITES):
            terrainsprites.append(pygame.image.load("sprites/terrain/grass{0}.png".format(i)))
        roadsprites = []
        for i in range(pgc.ROAD_SRITES):
            roadsprites.append(pygame.image.load("sprites/terrain/road{0}.png".format(i)))
        map_img = pygame.Surface((pgc.GRID_SIZE*bf_map.width, (pgc.GRID_SIZE*bf_map.height)))
        terrain_color = {
            enums.Terrain.ALLY_CAMP: pgc.ALLY_CAMP_COLOR,
            enums.Terrain.ENEMY_CAMP: pgc.ENEMY_CAMP_COLOR,
        }
        for i in range(bf_map.height):
            for j in range(bf_map.width):
                if bf_map.get_terrain((i, j)) == enums.Terrain.GRASS:
                    map_img.blit(random.choice(terrainsprites), (j*pgc.GRID_SIZE, i*pgc.GRID_SIZE))
                elif bf_map.get_terrain((i, j)) == enums.Terrain.ROAD:
                    map_img.blit(random.choice(roadsprites), (j*pgc.GRID_SIZE, i*pgc.GRID_SIZE))
                else:
                  pygame.draw.rect(map_img, terrain_color[bf_map.get_terrain((i, j))],
                  pygame.Rect(j*pgc.GRID_SIZE, i*pgc.GRID_SIZE,
                  pgc.GRID_SIZE, pgc.GRID_SIZE))
        return map_img

    def make_unit_imgs(self):
        """
        Creates surfaces with an image of each unit type.
        """
        infantryunit = pygame.image.load("sprites/enemies/soldier0.png")
        armoredunit = pygame.image.load("sprites/enemies/tank0.png")
        airforceunit = pygame.image.load("sprites/enemies/plane0.png")
        return {enums.Unit.INFANTRY: infantryunit, enums.Unit.ARMORED: armoredunit, enums.Unit.AIR_FORCE: airforceunit}

    def make_tower_imgs(self):
        """
        Creates surfaces with an image of each tower type.
        """
        mgun_sur = pygame.image.load("sprites/tower/machinegun0.png")
        cannon_sur = pygame.image.load("sprites/tower/cannon0.png")
        antitank_sur = pygame.image.load("sprites/tower/antitank0.png")
        missile_sur = pygame.image.load("sprites/tower/missile0.png")
        return {enums.Tower.MACHINE_GUN: mgun_sur, enums.Tower.CANNON: cannon_sur,
                enums.Tower.ANTI_TANK: antitank_sur, enums.Tower.MISSILE: missile_sur}
    
    def make_tower_sounds(self):
        """
        Creates sounds for a shoot in each tower type.
        """
        mgun_snd = pygame.mixer.Sound("sounds/AKShoot.ogg")
        cannon_snd = pygame.mixer.Sound("sounds/HEShoot.ogg")
        antitank_snd = pygame.mixer.Sound("sounds/AWPShoot.ogg")
        missile_snd = pygame.mixer.Sound("sounds/AKShoot.ogg")
        return {enums.Tower.MACHINE_GUN: mgun_snd, enums.Tower.CANNON: cannon_snd,
                enums.Tower.ANTI_TANK: antitank_snd, enums.Tower.MISSILE: missile_snd}
    
    def hp_bar(self, pos, perc_hp):
        """
        Draws a unit's hp bar if not full.
        """
        if perc_hp < 1:
            pygame.draw.rect(self.screen, pgc.RED, pygame.Rect(*pos, perc_hp*pgc.GRID_SIZE, pgc.HP_HEIGHT))
        
    def draw_ally_camp_hp_bar(self):
        """
        Draws ally's camp hp bar.
        """
        ally_camp = self.game.get_map().ally_camp
        pos = pgc.ALLY_CAMP_HP_POS
        perc_hp = ally_camp.get_health_perc()
        perc = max(0, int(100*perc_hp))
        pygame.draw.rect(self.screen, pgc.GREEN, pygame.Rect(*pos, perc_hp*pgc.GRID_SIZE*3, pgc.ALLY_CAMP_HP_HEIGHT))
        text = self.regular_font.render(str(perc) + '%', True, pgc.RED)
        self.screen.blit(text, pgc.ALLY_CAMP_HP_PERC_POS)
        self.screen.blit(pygame.image.load("sprites/general/heart.png"), pgc.ALLY_CAMP_HP_POS)

    def draw_buttons(self):
        for button in self.input.get_buttons():
            self.screen.blit(button.content, button.pos)

    def draw(self):
        """
        Draws all elements in screen.
        """
        self.screen.fill(pgc.BLACK)
        if self.game.game_state == enums.GameState.GRACE_PERIOD:
            self.draw_playing()
            self.draw_wave_text()
        elif self.game.game_state == enums.GameState.PLAYING:
            self.draw_playing()
        self.draw_buttons()
        pygame.display.flip()

    def draw_playing(self):
        """
        Draws the elements in the screen in the playing state
        """
        self.screen.blit(self.map_img, pgc.MAP_CORNER_POS)

        self.draw_ally_camp_hp_bar()
        for unit in self.game.units:
            unit_pos = screenpos.unit_pos_in_scrn(unit.cur_pos, unit.next_pos, unit.move_progress)
            self.screen.blit(
                pygame.transform.rotate(self.unit_imgs[unit.get_unit_type()], utils.direction2angle(unit.get_direction())), unit_pos
            )
        for unit in self.game.units:
            unit_pos = screenpos.unit_pos_in_scrn(unit.cur_pos, unit.next_pos, unit.move_progress)
            self.hp_bar(unit_pos, unit.get_health_perc())
        for tower in self.game.towers:
            tower_pos = screenpos.unit_pos_in_scrn(tower.pos, tower.pos, 1)
            self.screen.blit(
                self.tower_imgs[tower.get_tower_type()], tower_pos
            )

    def draw_wave_text(self):
        """
        Draws wave number in text
        """
        text = self.big_font.render(f"WAVE {self.game.waves.get_wave_n()}", True, pgc.RED)
        self.screen.blit(
            text, (pgc.MAP_CORNER_POS[0] + (pgc.GRID_SIZE*gc.MAP_WIDTH - text.get_width())//2,
                   pgc.MAP_CORNER_POS[1] + (pgc.GRID_SIZE*gc.MAP_HEIGHT - text.get_height())//2)
        )

    def draw_game_over_text(self):
        """
        Draws game over text on screen.
        """
        text = self.big_font.render('GAME OVER', True, pgc.RED)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/3))

        text = self.regular_font.render('Aperte qualquer tecla para reiniciar', True, pgc.RED)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2))

        pygame.display.flip()

def BackgroundMusic():
    backgroundmusic = pygame.mixer.music.load("sounds/BackgroundMusic_FibradeHeroi.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    return backgroundmusic
