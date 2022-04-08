import pygame

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
        if self.is_pressed(self, mouse_pos):
            self.action(self.game)

    @property
    def content(self):
        return self._content

