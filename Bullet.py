'''
class for bullet object to be used in the game

'''
import pygame as pg
import math

class Bullet():
    
    BULLET_WIDTH = 15
    BULLET_HEIGHT = 8
    BULLET_VELOCITY = 16 #8
    
    #def bullets as pygame rectangles
    def __init__(self,
                 x,
                 y,
                 colorSet,
                 direction):
        
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.colorSet = colorSet # color of the bullet
        self.direction = direction # direction of the bullet
        self.rect = pg.Rect(x, y, self.BULLET_WIDTH, self.BULLET_HEIGHT) # rectangle around the bullet (similar to hitbox)
    
    def draw(self, window):
        color = self.colorSet[math.floor(pg.time.get_ticks()/100)%5]
        pg.draw.rect(window, color, self.rect)
    
    def move(self, Player1, Player2):
        self.x += self.BULLET_VELOCITY * self.direction
        self.rect.x = self.x
    
    def isOffScreen(self, width):
        return not(self.x <= width and self.x >= 0)
    
    def collision(self, obj):
        return self.rect.colliderect(obj)
    