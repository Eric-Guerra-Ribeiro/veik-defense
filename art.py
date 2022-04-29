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
        self.factory_imgs = self.make_factory_images()
        self.regular_font = pygame.font.Font('freesansbold.ttf', 30)
        self.big_font = pygame.font.Font('freesansbold.ttf', 50)
        self.menu_background = pygame.image.load("backgrounds/menu.png")
        self.game_over_background = pygame.image.load("backgrounds/game_over.png")
        self.win_background = pygame.image.load("backgrounds/win.png")
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
        map_img = pygame.Surface((pgc.GRID_SIZE*bf_map.width, pgc.GRID_SIZE*bf_map.height))
        base_sprite = {
            enums.Terrain.ALLY_CAMP: pygame.image.load("sprites/general/ally_base.png"),
            enums.Terrain.ENEMY_CAMP: pygame.image.load("sprites/general/enemy_base.png"),
        }
        for i in range(bf_map.height):
            for j in range(bf_map.width):
                if bf_map.get_terrain((i, j)) == enums.Terrain.GRASS:
                    map_img.blit(random.choice(terrainsprites), (j*pgc.GRID_SIZE, i*pgc.GRID_SIZE))
                elif bf_map.get_terrain((i, j)) == enums.Terrain.ROAD:
                    map_img.blit(random.choice(roadsprites), (j*pgc.GRID_SIZE, i*pgc.GRID_SIZE))
                else:
                    map_img.blit(random.choice(roadsprites), (j*pgc.GRID_SIZE, i*pgc.GRID_SIZE))
                    map_img.blit(base_sprite[bf_map.get_terrain((i, j))], (j*pgc.GRID_SIZE, i*pgc.GRID_SIZE))
        return map_img

    def make_unit_imgs(self):
        """
        Creates surfaces with an image of each unit type.
        """
        infantryunitlvl1 = pygame.image.load("sprites/enemies/soldier0.png")
        infantryunitlvl2 = pygame.image.load("sprites/enemies/soldier1.png")
        infantryunitlvl3 = pygame.image.load("sprites/enemies/soldier2.png")
        infantryunitlvl4 = pygame.image.load("sprites/enemies/soldier3.png")
        armoredunitlvl1 = pygame.image.load("sprites/enemies/tank0.png")
        armoredunitlvl2 = pygame.image.load("sprites/enemies/tank1.png")
        airforceunitlvl1 = pygame.image.load("sprites/enemies/plane0.png")
        airforceunitlvl2 = pygame.image.load("sprites/enemies/plane1.png")
        return {enums.UnitSubtype.INFANTRY_LVL1: infantryunitlvl1, enums.UnitSubtype.INFANTRY_LVL2: infantryunitlvl2,
                enums.UnitSubtype.INFANTRY_LVL3: infantryunitlvl3, enums.UnitSubtype.INFANTRY_LVL4: infantryunitlvl4,
                enums.UnitSubtype.ARMORED_LVL1: armoredunitlvl1, enums.UnitSubtype.ARMORED_LVL2: armoredunitlvl2,
                enums.UnitSubtype.AIR_FORCE_LVL1: airforceunitlvl1, enums.UnitSubtype.AIR_FORCE_LVL2: airforceunitlvl2}

    def make_tower_imgs(self):
        """
        Creates surfaces with an image of each tower type.
        """
        mgunlvl1_sur = pygame.image.load("sprites/tower/machinegun0.png")
        mgunlvl2_sur = pygame.image.load("sprites/tower/machinegun1.png")
        mgunlvl3_sur = pygame.image.load("sprites/tower/machinegun2.png")
        cannonlvl1_sur = pygame.image.load("sprites/tower/cannon0.png")
        cannonlvl2_sur = pygame.image.load("sprites/tower/cannon1.png")
        cannonlvl3_sur = pygame.image.load("sprites/tower/cannon2.png")
        antitanklvl1_sur = pygame.image.load("sprites/tower/antitank0.png")
        antitanklvl2_sur = pygame.image.load("sprites/tower/antitank1.png")
        missilelvl1_sur = pygame.image.load("sprites/tower/missile0.png")
        missilelvl2_sur = pygame.image.load("sprites/tower/missile1.png")
        return {enums.Tower.MACHINE_GUN_LVL1: mgunlvl1_sur, enums.Tower.MACHINE_GUN_LVL2: mgunlvl2_sur,
                enums.Tower.MACHINE_GUN_LVL3: mgunlvl3_sur, enums.Tower.CANNON_LVL1: cannonlvl1_sur,
                enums.Tower.CANNON_LVL2: cannonlvl2_sur, enums.Tower.CANNON_LVL3: cannonlvl3_sur,
                enums.Tower.ANTI_TANK_LVL1: antitanklvl1_sur, enums.Tower.ANTI_TANK_LVL2: antitanklvl2_sur, 
                enums.Tower.MISSILE_LVL1: missilelvl1_sur, enums.Tower.MISSILE_LVL2: missilelvl2_sur}
    
    def make_factory_images(self):
        nuclearpp_sur = pygame.image.load("sprites/general/nuclearplant.png")
        coalfactory_sur = pygame.image.load("sprites/general/factory.png")
        return {enums.ResourceFactory.NUCLEAR_PLANT: nuclearpp_sur, enums.ResourceFactory.COAL_FACTORY: coalfactory_sur}

    
    def make_tower_sounds(self):
        """
        Creates sounds for a shoot in each tower type.
        """
        mgun_snd = pygame.mixer.Sound("sounds/AKShoot.ogg")
        cannon_snd = pygame.mixer.Sound("sounds/HEShoot.ogg")
        antitank_snd = pygame.mixer.Sound("sounds/AWPShoot.ogg")
        missile_snd = pygame.mixer.Sound("sounds/AKShoot.ogg")
        return {enums.Tower.MACHINE_GUN_LVL1: mgun_snd, enums.Tower.CANNON_LVL1: cannon_snd,
                enums.Tower.ANTI_TANK_LVL1: antitank_snd, enums.Tower.MISSILE_LVL1: missile_snd}

    def tower_sound(self):
        """
        Play the unit shoot sound
        """
        self.tower_sounds[self.game.tower.get_tower_type()].play
    
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
    
    def draw_resource_number(self):
        """
        Draws ally's camp resources number.
        """
        resource_number = self.game.resources
        text = self.regular_font.render(f"{resource_number:.0f}", True, pgc.YELLOW)
        self.screen.blit(text, pgc.ALLY_CAMP_RESOURCE_NUMBER_POS)
        self.screen.blit(pygame.image.load("sprites/general/coin.png"), pgc.ALLY_CAMP_RESOURCE_POS)

    def draw_buttons(self):
        for button in self.input.get_buttons():
            self.screen.blit(button.content, button.pos)

    def draw(self):
        """
        Draws all elements in screen.
        """
        if self.game.changed_map:
            self.game.changed_map = False
            self.map_img = self.make_map_surface(self.game.get_map())
        self.screen.fill(pgc.DARK_SLATE_GRAY)
        if self.game.game_state == enums.GameState.GRACE_PERIOD:
            self.draw_playing()
            self.draw_wave_text()
        elif self.game.game_state == enums.GameState.PLAYING:
            self.draw_playing()
        elif self.game.game_state == enums.GameState.GAME_OVER:
            self.draw_game_over()
        elif self.game.game_state == enums.GameState.MENU:
            self.draw_menu()
        elif self.game.game_state == enums.GameState.WIN:
            self.draw_win()
        elif self.game.game_state == enums.GameState.TUTORIAL:
            self.draw_tutorial()
        elif self.game.game_state == enums.GameState.PAUSED:
            self.draw_playing()
        self.draw_buttons()
        pygame.display.flip()

    def draw_playing(self):
        """
        Draws the elements in the screen in the playing state
        """
        self.screen.blit(self.map_img, pgc.MAP_CORNER_POS)

        for unit in self.game.units:
            unit_pos = screenpos.unit_pos_in_scrn(unit.cur_pos, unit.next_pos, unit.move_progress)
            self.screen.blit(
                pygame.transform.rotate(self.unit_imgs[unit.get_unit_subtype()], utils.direction2angle(unit.get_direction())), unit_pos
            )
        for unit in self.game.units:
            unit_pos = screenpos.unit_pos_in_scrn(unit.cur_pos, unit.next_pos, unit.move_progress)
            self.hp_bar(unit_pos, unit.get_health_perc())
        for tower in self.game.towers:
            tower_pos = screenpos.unit_pos_in_scrn(tower.pos, tower.pos, 1)
            self.screen.blit(
                self.tower_imgs[tower.get_tower_type()], tower_pos
            )
        for factory in self.game.resource_factories:
            factory_pos = screenpos.unit_pos_in_scrn(factory.pos, factory.pos, 1)
            self.screen.blit(
                self.factory_imgs[factory.get_factory_type()], factory_pos
            )

    
        self.draw_ally_camp_hp_bar()
        self.draw_resource_number()

    def draw_wave_text(self):
        """
        Draws wave number in text
        """
        text = self.big_font.render(f"WAVE {self.game.waves.get_wave_n()}", True, pgc.RED)
        self.screen.blit(
            text, (pgc.MAP_CORNER_POS[0] + (pgc.GRID_SIZE*gc.MAP_WIDTH - text.get_width())//2,
                   pgc.MAP_CORNER_POS[1] + (pgc.GRID_SIZE*gc.MAP_HEIGHT - text.get_height())//2)
        )

    def draw_game_over(self):
        """
        Draws game over text on screen.
        """
        self.screen.blit(self.game_over_background, (0, 0))

        text = self.big_font.render('GAME OVER', True, pgc.RED)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2))
    
        text = self.regular_font.render("Press any key to restart", True, pgc.RED)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2 + 2*text.get_height()))

    def draw_menu(self):
        """
        Draws the Menu
        """
        self.screen.blit(self.menu_background, (0, 0))
        text = self.big_font.render('VEIK DEFENSE', True, pgc.RED)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(2*text.get_height())))
        selected_map_text = self.regular_font.render(f'Selected map: {self.game.selected_map + 1}', True, pgc.RED)
        self.screen.blit(selected_map_text, ((pgc.WINDOW_WIDTH - selected_map_text.get_width())/2, pgc.WINDOW_HEIGHT - selected_map_text.get_height()))

    def draw_win(self):
        """
        Draws win end screen.
        """
        self.screen.blit(self.win_background, (0, 0))

        text = self.big_font.render('YOU WIN!', True, pgc.BLUE)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2))

        text = self.regular_font.render("Press any key to restart", True, pgc.BLUE)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2 + 2*text.get_height()))

    def draw_tutorial(self):
        """
        Draws the tutorial screen.
        """
        text = self.big_font.render('TUTORIAL', True, pgc.RED)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(2*text.get_height())))
        text = self.big_font.render('Read README.md', True, pgc.YELLOW)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2))
        text = self.regular_font.render("Press any key to return to menu", True, pgc.YELLOW)
        self.screen.blit(text, ((pgc.WINDOW_WIDTH - text.get_width())/2 ,(pgc.WINDOW_HEIGHT - text.get_height())/2 + 2*text.get_height()))


def BackgroundMusic():
    backgroundmusic = pygame.mixer.music.load("sounds/BackgroundMusic_FibradeHeroi.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    return backgroundmusic

def create_text_box(text):
    img = pygame.Surface((3.5 * pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.SRCALPHA)
    regular_font = pygame.font.Font('freesansbold.ttf', 40)
    txt = regular_font.render(text, True, pgc.YELLOW)
    img.blit(txt, (0,0))
    return img

def create_surface(type, cls):
    """
    Create button surface
    """
    width = pgc.TOWER_BUTTON_WIDTH
    img = pygame.Surface((width * pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.SRCALPHA)
    regular_font = pygame.font.Font('freesansbold.ttf', 20)
    if type == enums.ResourceFactory.COAL_FACTORY:
        img.blit(pygame.image.load("sprites/general/factory.png"), (0, 0))

        text1 = regular_font.render(f"P: {int(cls.production_profit)} R: {cls.production_rate * pgc.FREQUENCY:.1f}", True, pgc.GREEN)
        text2 = regular_font.render("$" + str(cls.price), True, pgc.YELLOW)
    else :
        if type == enums.Tower.MACHINE_GUN_LVL1:
            img.blit(pygame.image.load("sprites/tower/machinegun0.png"), (0, 0))
        elif type == enums.Tower.CANNON_LVL1:
            img.blit(pygame.image.load("sprites/tower/cannon0.png"), (0, 0))
        elif type == enums.Tower.MISSILE_LVL1:
            img.blit(pygame.image.load("sprites/tower/missile0.png"), (0, 0))
        elif type == enums.Tower.ANTI_TANK_LVL1:
            img.blit(pygame.image.load("sprites/tower/antitank0.png"), (0, 0))
        text1 = regular_font.render(f"D: {cls.dmg:.1f} F: {cls.fire_rate * pgc.FREQUENCY:.1f}", True, pgc.RED)
        text2 = regular_font.render(f"${cls.price}", True, pgc.YELLOW)

    img.blit(text1, (pgc.GRID_SIZE + ((width - 1)*pgc.GRID_SIZE - text1.get_width())/2, (pgc.GRID_SIZE/2 - text1.get_height())/2))
    img.blit(text2, (pgc.GRID_SIZE + ((width - 1)*pgc.GRID_SIZE - text2.get_width())/2, pgc.GRID_SIZE/2 + (pgc.GRID_SIZE/2 - text2.get_height())/2))
    return img


def menu_button_content(string, fill=False):
    """
    Returns a pygame surface with a string for the size of the menu button.
    """
    regular_font = pygame.font.Font('freesansbold.ttf', 30)
    text = regular_font.render(string, True, pgc.RED)
    content = pygame.Surface((pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), pygame.SRCALPHA)
    if fill:
        content.fill(pgc.DARK_SLATE_GRAY)
    content.blit(text, ((pgc.MENU_BUTTON_WIDTH - text.get_width())/2 ,(pgc.MENU_BUTTON_HEIGHT - text.get_height())/2))
    return content
