"""
Module responsible for drawing the legend on the screen
"""

import pygame as pg


light_purple = (175, 0, 188)
light_blue = (0, 239, 255)
light_green = (0, 255, 68)
white = (255, 255, 255)
colors = (white, light_blue, light_purple, light_green)


def load_icons():
    """
    Loads the icons from the .png files
    :return: Surface, Surface (icons)
    """
    raw_corner = pg.image.load('corner.png')
    transformed_corner = pg.transform.scale(raw_corner, (18, 18))
    corner_symbol = pg.transform.rotate(transformed_corner, 225)
    flag_raw = pg.image.load('flag.png')
    flag_symbol = pg.transform.scale(flag_raw, (23, 23))

    return corner_symbol, flag_symbol


def draw_legend(screen):
    """
    Draws the legend on the screen
    :param screen: Surface (screen)
    :return: None
    """
    for color, i in zip(colors, range(4)):
        pg.draw.rect(screen, (0, 0, 0), (400 + 100 * i - 1, 40 - 1, 22, 22), 0)
        pg.draw.rect(screen, color, (400 + 100 * i, 40, 20, 20), 0)
    for i in range(2):
        screen.blit(load_icons()[i], (790 + 110 * i, 37 + i, 32, 32))
