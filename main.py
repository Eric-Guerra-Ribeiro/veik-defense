import pygame

import pygameconstants as pgc
import gamecontroller
import art
import sounds

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
    arts = art.Art(screen, game)
     #TODO: Change this
    game.spawn_mgun((2, 1))
    game.spawn_cannon((2, 7))
    game.spawn_antitank((3, 8))
    game.spawn_missile((2, 5))
    while game.is_running():
        clock.tick(pgc.FREQUENCY)
        arts.draw()
        game.run()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.spawn_infantry()
                if event.key == pygame.K_v:
                    game.spawn_tank()
                if event.key == pygame.K_b:
                    game.spawn_airforce()


if __name__ == "__main__":
    main()
