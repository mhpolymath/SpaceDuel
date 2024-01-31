''' define a button class using pygame rect and its collidepoint method to detect the mouse position and click event'''
import pygame as pg


class Button():
    def __init__(self, x, y, width, height, image):
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.width = width  # width of the image
        self.height = height  # height of the image
        self.image = image  # image of the object
        self.rect = pg.Rect(x, y, width, height)  # rectangle around the image

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def is_hover(self, mouse_pos):
        # check if the mouse position is inside the button
        return self.rect.collidepoint(mouse_pos)
