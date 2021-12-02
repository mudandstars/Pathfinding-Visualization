"""
This module contains the Button class, allowing to draw buttons and detect mouse movement over them
"""
import pygame as pg


class Button:
    """
    The Button class allows for button object initiation
    """
    def __init__(self, position, color, text, text_color, outline=False):

        self.position = position
        self.color = color
        self.outline = outline
        self.text = text
        self.text_color = text_color
        self.selected = False
        self.dropdown = False

    def is_over(self, pos):
        """
        Detects if the mouse position is over the button
        :param pos: (x, y) mouse position
        :return: Boolean
        """
        if self.position[0] <= pos[0] <= (self.position[0] + self.position[2]):
            if self.position[1] <= pos[1] <= (self.position[1] + self.position[3]):
                return True
        return False

    def draw(self, screen):
        """
        Draws the button on the screen
        :param screen: Surface
        :return: None
        """
        if self.outline:
            pg.draw.rect(screen, (0, 0, 0), (self.position[0] - 1, self.position[1] - 1,
                                             self.position[2] + 2, self.position[3] + 2), 0)

        pg.draw.rect(screen, self.color, self.position, 0)
        # 2 is width, see what changes
        font = pg.font.SysFont('montserrat', 30)
        text = font.render(self.text, True, self.text_color)
        screen.blit(text, (self.position[0] + (self.position[2] / 2 - text.get_width() / 2),
                           self.position[1] + (self.position[3] / 2 - text.get_height() / 2)))
