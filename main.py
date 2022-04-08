import pygame

import pygameconstants as pgc
import gamecontroller
import art

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
    arts = art.Art(screen, game)
     #TODO: Change this
    game.spawn_mgun((2, 1))
    game.spawn_cannon((2, 7))
    while game.is_running():
        clock.tick(pgc.FREQUENCY)
        game.run()
        arts.draw()
        if game.go:
            show_go_screen()
            game.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.spawn_troop()


if __name__ == "__main__":
    main()
