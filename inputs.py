import collections

import pygame

import enums
import utils
import gameconstants as gc
import pygameconstants as pgc
import art
import gamecontroller

class Button:
    """
    Creates a button on screen.
    """
    def __init__(self, pos, size, content, action, game):
        self.pos = pos
        self.size = size
        self._content = pygame.Surface(size, pygame.SRCALPHA)
        self._content.blit(content, ((size[0]-content.get_size()[0])//2, (size[1]-content.get_size()[1])//2))
        self.action = action
        self.game = game
    
    def is_pressed(self, mouse_pos):
        """
        Checks if the mouse is pressing the button
        """
        return (self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0]
                and self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.size[1])

    def press(self, mouse_pos):
        """
        Presses the button if the mouse is on the button.
        """
        if self.is_pressed(mouse_pos):
            self.action(self.game)

    @property
    def content(self):
        return self._content


class Board:
    """
    Class for representing an interactable board map.
    """
    def __init__(self, pos, size, grid_size, action, game):
        self.pos = pos
        self.size = size
        self.grid_size = grid_size
        self.action = action
        self.game = game
    
    def is_pressed(self, mouse_pos):
        """
        Checks if any cell in the board is being pressed.
        """
        return (self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.grid_size*self.size[0]
                and self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.grid_size*self.size[1])

    def mouse_cell(self, mouse_pos):
        """
        Returns the cell that the mouse pressed.
        """
        row = (mouse_pos[1] - self.pos[1])//self.grid_size
        column = (mouse_pos[0] - self.pos[0])//self.grid_size
        return (row, column)

    def press(self, mouse_pos):
        """
        Presses a cell in the board if the mouse is on it.
        """
        if self.is_pressed(mouse_pos):
            self.action(self.mouse_cell(mouse_pos), self.game)


class Input:
    """
    Class that controlls all inputs to the game.
    """
    def __init__(self, game):
        self.game = game
        self.boards = {
            enums.GameState.PLAYING : [
                Board(pgc.MAP_CORNER_POS, (gc.MAP_WIDTH, gc.MAP_HEIGHT), pgc.GRID_SIZE, utils.add_tower, self.game)
            ]
        }
        buttons = {
            enums.GameState.MENU : [
                Button(((pgc.WINDOW_WIDTH - pgc.MENU_BUTTON_WIDTH)/2, pgc.WINDOW_HEIGHT/2 - 2*pgc.MENU_BUTTON_HEIGHT),
                       (pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), art.menu_button_content("CAMPAIGN"),
                       lambda _game: utils.begin_campaign(_game), game),
                Button(((pgc.WINDOW_WIDTH - pgc.MENU_BUTTON_WIDTH)/2, pgc.WINDOW_HEIGHT/2 - 1*pgc.MENU_BUTTON_HEIGHT),
                       (pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), art.menu_button_content("CHALLENGE"),
                       lambda _game: utils.begin_challenge(_game), game),
                Button(((pgc.WINDOW_WIDTH - pgc.MENU_BUTTON_WIDTH)/2, pgc.WINDOW_HEIGHT/2 + 0*pgc.MENU_BUTTON_HEIGHT),
                       (pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), art.menu_button_content("MAP EDITOR"),
                       lambda _game: None, game),
                Button(((pgc.WINDOW_WIDTH - pgc.MENU_BUTTON_WIDTH)/2, pgc.WINDOW_HEIGHT/2 + 1*pgc.MENU_BUTTON_HEIGHT),
                       (pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), art.menu_button_content("TUTORIAL"),
                       lambda _game: utils.begin_tutorial(_game), game)
            ],
            enums.GameState.PAUSED : [
                Button(((pgc.WINDOW_WIDTH - pgc.MENU_BUTTON_WIDTH)/2, pgc.WINDOW_HEIGHT/2 - 1*pgc.MENU_BUTTON_HEIGHT),
                       (pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), art.menu_button_content("UNPAUSE", True),
                       lambda _game: gamecontroller.GameController.unpause(_game), game),
                Button(((pgc.WINDOW_WIDTH - pgc.MENU_BUTTON_WIDTH)/2, pgc.WINDOW_HEIGHT/2 + 0*pgc.MENU_BUTTON_HEIGHT),
                       (pgc.MENU_BUTTON_WIDTH, pgc.MENU_BUTTON_HEIGHT), art.menu_button_content("MENU", True),
                       lambda _game: gamecontroller.GameController.reset(_game), game),
            ],
            enums.GameState.PLAYING : [
                Button((1100,100), (pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.image.load("sprites/tower/machinegun0.png"),
                       lambda _game: utils.select_tower(_game, enums.Tower.MACHINE_GUN), game),
                Button((1100,200), (pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.image.load("sprites/tower/cannon0.png"),
                        lambda _game: utils.select_tower(_game, enums.Tower.CANNON), game),
                Button((1100,300), (pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.image.load("sprites/tower/missile0.png"),
                       lambda _game: utils.select_tower(_game, enums.Tower.MISSILE), game),
                Button((1100,400), (pgc.GRID_SIZE, pgc.GRID_SIZE), pygame.image.load("sprites/tower/antitank0.png"),
                       lambda _game: utils.select_tower(_game, enums.Tower.ANTI_TANK), game)

            ]
        }

        self.buttons = collections.defaultdict(lambda: [], buttons)

    def get_buttons(self):
        if self.game.game_state == enums.GameState.GRACE_PERIOD:
            return self.buttons[enums.GameState.PLAYING]
        return self.buttons[self.game.game_state]

    def input(self):
        """
        Reads the input accoring to game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if (self.game.game_state == enums.GameState.PLAYING
                or self.game.game_state == enums.GameState.GRACE_PERIOD):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game.pause()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for board in self.boards[enums.GameState.PLAYING]:
                        board.press(pygame.mouse.get_pos())
                    for button in self.buttons[enums.GameState.PLAYING]:
                        button.press(pygame.mouse.get_pos())
            elif (self.game.game_state == enums.GameState.GAME_OVER
                  or self.game.game_state == enums.GameState.TUTORIAL
                  or self.game.game_state == enums.GameState.WIN):
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.reset()
            elif self.game.game_state == enums.GameState.MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons[enums.GameState.MENU]:
                        button.press(pygame.mouse.get_pos())
            elif self.game.game_state == enums.GameState.PAUSED:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game.unpause()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons[enums.GameState.PAUSED]:
                        button.press(pygame.mouse.get_pos())
