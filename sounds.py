import pygame

def BackgroundMusic():
    backgroundmusic = pygame.mixer.music.load("sounds/BackgroundMusic_FibradeHeroi.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    return backgroundmusic