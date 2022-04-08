import pygame

import pygameconstants as pgc
import gamecontroller
import art
import input


def main():
    """
    Main function for the Veik Defense game, including its main loop.
    """

    def show_go_screen():
        arts.draw_game_over_text()
        waiting = True
        while waiting:
            clock.tick(pgc.FREQUENCY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False


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
    game.spawn_antitank((3, 8))
    game.spawn_missile((2, 5))
    while game.running:
        if game.go:
            show_go_screen()
            game.reset()
        clock.tick(pgc.FREQUENCY)
        game.run()
        inputs.input()
        arts.draw()

if __name__ == "__main__":
    main()
