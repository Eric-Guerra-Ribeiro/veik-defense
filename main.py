import pygame

import pygameconstants as pgc
import gamecontroller
import art

def main():
    """
    Main function for the Veik Defense game, including its main loop.
    """
    pygame.init()
    pygame.display.set_caption("Veik Defense")
    clock = pygame.time.Clock()
    game = gamecontroller.GameController()
    screen = pygame.display.set_mode((pgc.WINDOW_WIDTH, pgc.WINDOW_HEIGHT))
    arts = art.Art(screen, game)
    while game.is_running():
        clock.tick(pgc.FREQUENCY)
        arts.draw()
        game.run()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.spawn_troop()


if __name__ == "__main__":
    main()