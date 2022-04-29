import pygame

import pygameconstants as pgc
import gamecontroller
import art
import inputs


def main():
    """
    Main function for the Veik Defense game, including its main loop.
    """
    pygame.init()
    pygame.display.set_caption("Veik Defense")
    clock = pygame.time.Clock()
    game = gamecontroller.GameController()
    screen = pygame.display.set_mode((pgc.WINDOW_WIDTH, pgc.WINDOW_HEIGHT), pygame.SRCALPHA)
    bkgmusic = art.BackgroundMusic()
    input_sys = inputs.Input(game)
    arts = art.Art(screen, game, input_sys)
    while game.running:
        clock.tick(pgc.FREQUENCY)
        game.run()
        input_sys.input()
        arts.draw()

if __name__ == "__main__":
    main()
