import pygame

import pygameconstants as pgc
import gamecontroller
import art
import sounds
import input

def main():
    """
    Main function for the Veik Defense game, including its main loop.
    """
    pygame.init()
    pygame.display.set_caption("Veik Defense")
    clock = pygame.time.Clock()
    game = gamecontroller.GameController()
    screen = pygame.display.set_mode((pgc.WINDOW_WIDTH, pgc.WINDOW_HEIGHT))
    bkgmusic = art.BackgroundMusic()
    inputs = input.Input(game)
    arts = art.Art(screen, game)
     #TODO: Change this
    game.spawn_mgun((2, 1))
    game.spawn_cannon((2, 7))
    while game.running:
        clock.tick(pgc.FREQUENCY)
        arts.draw()
        game.run()
        inputs.input()


if __name__ == "__main__":
    main()
