#TODO: 
# - check spelling for (handeler or handler) because wtf English please!!
# - check convention and performance for wether or not to pass the window dimensions 
#       to movement_handler() as arguments or define the variables inside is better
# - check if the methods under Extras are needed or remove them

'''
create a player class for the player and enemy objects (change doc)
'''

import pygame as pg

class Player():
    VELOCITY = 5 # velocity of the player: movement per call of handler function
    
    def __init__(self, x, y, width, height, image, keys, health = 10, bullets = []):
        
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.width = width # width of the image
        self.height = height # height of the image
        self.image = image # image of the object
        self.rect = pg.Rect(x, y, width, height) # rectangle around the image (similar to hitbox)
        self.keys = keys # dictionary of keys to move the player
        self.health = health # health of the player
        self.bullets = bullets # list of bullets

    
    def addBullet(self, bullet):
        self.bullets.append(bullet)
        
    def removeBullet(self, bullet):
        self.bullets.remove(bullet)
    
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        
    def movement_handler(self): 
        # maybe make window size passed to the function as args? check which is better.
    
        # moving the player (self) using keys 
        
        W_WIDTH = pg.display.get_window_size()[0]
        W_HEIGHT = pg.display.get_window_size()[1]
        
        keys = pg.key.get_pressed()
        if (keys[self.keys['L']] and self.x - self.VELOCITY >= 0): 
            # left
            self.x -= self.VELOCITY
            self.rect.x = self.x
        
        if (keys[self.keys['R']] and self.x + self.VELOCITY <= W_WIDTH - self.width): 
            # right
            self.x += self.VELOCITY
            self.rect.x = self.x
        
        if (keys[self.keys['U']] and self.y - self.VELOCITY >= 0): 
            # up
            self.y -= self.VELOCITY
            self.rect.y = self.y
        
        if (keys[self.keys['D']] and self.y +self.VELOCITY <= W_HEIGHT-self.height): # down
            # down
            self.y += self.VELOCITY
            self.rect.y = self.y


        
    #Extras:     
    # def get_mask(self):
    #     return pg.mask.from_surface(self.image)
    
    # def collide(self, obj):
    #     return self.rect.colliderect(obj.rect)
    