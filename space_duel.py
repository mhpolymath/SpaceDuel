#TODO: 
# - make sure you are using consistent naming conventions. noticed issues include: 
#       you sometimes use (player1 and player2), (player_1 and player_2), 
#       (player and enemy), and (spaceship and alien)
# - make sure that decisions made to define some stuff outside or inside the main function 
#       meet the conventions like players, bullet lists, texts to be shown, etc.
# - make the file more readable and follows the python code thingy for line length etc.

# import statements:
import pygame as pg
# import sys
# import os
import game_colors as gc
import game_images as gi
import game_fonts as gf

from Player import Player
from Bullet import Bullet



# initialize pygame modules for safe use
pg.init() 

# set game constants:
# width and height of the window
# the window itself and the caption
# the FPS and the event types
W_WIDTH, W_HEIGHT = 1400, 700
WINDOW = pg.display.set_mode((W_WIDTH, W_HEIGHT),pg.RESIZABLE)
pg.display.set_caption("SPACESHIP VS ALIEN!")
FPS = 120
SHIP_HIT = pg.USEREVENT + 1
ALIEN_HIT = pg.USEREVENT + 2

#import fonts for the game
win_font = gf.GAME_FONT_INACTIVE
health_font = gf.GAME_FONT_ACTIVE

# import images for the game
spaceship_image = gi.SPACESHIP_FINAL_IMAGE
spaceship_image_flipped = gi.FLIPPED_SPACESHIP_IMAGE
alien_image = gi.ALIEN_FINAL_IMAGE
background_image = gi.BACKGROUND_FINAL_IMAGE

# Define control keys for each player as dictionaries:
spaceship_keys = {'U': pg.K_w, 'D': pg.K_s, 'L': pg.K_a, 'R': pg.K_d}
alien_keys = {'U': pg.K_UP, 'D': pg.K_DOWN, 'L': pg.K_LEFT, 'R': pg.K_RIGHT}


# Create players for the game
spaceship = Player((W_WIDTH/5)-gi.SCALED_SPACESHIP_WIDTH/2,
                (W_HEIGHT/2)-gi.SCALED_SPACESHIP_HEIGHT/2,
                gi.SPACESHIP_FINAL_WIDTH,
                gi.SPACESHIP_FINAL_HEIGHT,
                spaceship_image,
                spaceship_keys)
alien = Player((4*W_WIDTH/5)-gi.SCALED_ALIEN_WIDTH/2,
                (W_HEIGHT/2)-gi.SCALED_ALIEN_HEIGHT/2,
                gi.ALIEN_FINAL_WIDTH,
                gi.ALIEN_FINAL_HEIGHT,
                alien_image,
                alien_keys)

spaceship_health_text = health_font.render("Player 1 Health: " + str(spaceship.health), 1, gc.R_FIRE1)
alien_health_text = health_font.render("Player 2 Health: " + str(alien.health), 1, gc.B_FIRE1)

# Define a function to handle bullets collisions and offscreen status:
def handle_bullets(spaceship, alien, spaceship_bullets, alien_bullets):
    
    #player bullets handling
    for bullet in spaceship_bullets:
        bullet.move(spaceship, alien)
        #if player bullet is offscreen, remove it from the player_bullet list
        if bullet.collision(alien):
            pg.event.post(pg.event.Event(ALIEN_HIT))
            spaceship_bullets.remove(bullet)
        
        #if player bullet collides with enemy, remove it from the player_bullet list
        elif bullet.isOffScreen(W_WIDTH):
            spaceship_bullets.remove(bullet)

    #enemy bullets handling
    for bullet in alien_bullets:
        bullet.move(alien, spaceship)
        #if enemy bullet is offscreen, remove it from the enemy_bullet list
        if bullet.collision(spaceship):
            pg.event.post(pg.event.Event(SHIP_HIT))
            alien_bullets.remove(bullet)
        
        #if enemy bullet collides with player, remove it from the enemy_bullet list
        elif bullet.isOffScreen(W_WIDTH):
            alien_bullets.remove(bullet)
    
# Define a function to draw the window
def draw_window(spaceship, alien, spaceship_bullets = [], alien_bullets = [], spaceship_health_text = spaceship_health_text, alien_health_text = alien_health_text):
    spaceship_winning_text = win_font.render("Player 1 Wins!", 1, gc.R_FIRE1)
    alien_winning_text = win_font.render("Player 2 Wins!", 1, gc.B_FIRE1)
    if spaceship.health <= 0 or alien.health <= 0:
        WINDOW.fill(gc.BLACK)
        if spaceship.health <= 0:
            WINDOW.blit(alien_winning_text,
                        (
                            (W_WIDTH - spaceship_winning_text.get_width())/2,
                            (W_HEIGHT - spaceship_winning_text.get_height())/2
                         ))
        elif alien.health <= 0:
            WINDOW.blit(spaceship_winning_text,
                        (
                            (W_WIDTH - spaceship_winning_text.get_width())/2,
                            (W_HEIGHT - spaceship_winning_text.get_height())/2
                         ))
            
        pg.display.update()
    else:
        WINDOW.blit(background_image, (0,0))
        WINDOW.blit(spaceship_health_text, (W_WIDTH/8, W_HEIGHT/14))
        WINDOW.blit(alien_health_text, (7*W_WIDTH/8 - alien_health_text.get_width(), W_HEIGHT/14))
#        WINDOW.blit(player_2_health_text, (W_WIDTH/8, W_HEIGHT/))
        if spaceship.x > alien.x:
            WINDOW.blit(spaceship_image_flipped, (spaceship.x,spaceship.y))
            WINDOW.blit(alien_image, (alien.x,alien.y))
        else:    
            WINDOW.blit(spaceship_image, (spaceship.x,spaceship.y))
            WINDOW.blit(alien_image, (alien.x,alien.y))
        for bullet in spaceship_bullets:
            bullet.draw(WINDOW)
        for bullet in alien_bullets:
            bullet.draw(WINDOW)
        
        pg.display.update()
   
# Define the main function
def main():

    
    # Create a list to store the bullets of each player
    spaceship_bullets = []
    alien_bullets = []
    

    # Create a clock object to control the FPS
    clock = pg.time.Clock()
    
    # Create a boolean to control the game loop
    isRunning = True
    while isRunning:
        
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT: #quitting the game
                isRunning = False
            
            #if event.type == pg.KEYDOWN: #bullet buttons
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    if spaceship.x < alien.x:
                        print("Z key pressed")
                        spaceship_bullet = Bullet(spaceship.x + spaceship.width,
                                                spaceship.y + spaceship.height/2 - Bullet.BULLET_HEIGHT/2,
                                                gc.R_FIRE,
                                                1)
                        spaceship_bullets.append(spaceship_bullet)
                        print("player 1 bullet created")
                    else:
                        print("Z key pressed")
                        spaceship_bullet = Bullet(spaceship.x,
                                                spaceship.y + spaceship.height/2 - Bullet.BULLET_HEIGHT/2,
                                                gc.R_FIRE,
                                                -1)
                        spaceship_bullets.append(spaceship_bullet)
                        print("player 1 bullet created")
                if event.key == pg.K_SLASH:
                    if spaceship.x < alien.x:
                        print("/ key pressed")
                        bullet = Bullet(alien.x,
                                                alien.y + alien.height/2 - Bullet.BULLET_HEIGHT/2,
                                                gc.B_FIRE,
                                                -1)
                        alien_bullets.append(bullet)
                        print("player 2 bullet created")
                    else:
                        print("/ key pressed")
                        bullet = Bullet(alien.x + alien.width,
                                                alien.y + alien.height/2 - Bullet.BULLET_HEIGHT/2,
                                                gc.B_FIRE,
                                                1)
                        alien_bullets.append(bullet)
                        print("player 2 bullet created")

            if event.type == SHIP_HIT:
                print("SHIP HIT")
                if spaceship.health > 0:
                    spaceship.health -= 1
                    #player_1_health_text = health_font.render("Player 1 Health: " + str(player1.health), 1, gc.R_FIRE1)
                    print(spaceship.health)
                else:
                    print("ALIEN WINS!")
                
            if event.type == ALIEN_HIT:
                print("ALIEN HIT")
                if alien.health > 0:
                    alien.health -= 1
                    #player2_health_text = health_font.render("Player 2 Health: " + str(player2.health), 1, gc.B_FIRE1)
                    print(alien.health)
                else:
                    print("SPACESHIP WINS!")

        # Handle player movements
        spaceship.movement_handler()
        alien.movement_handler()
        handle_bullets(spaceship, alien, spaceship_bullets, alien_bullets)
        # Draw window
        draw_window(spaceship,
                    alien,
                    spaceship_bullets,
                    alien_bullets,
                    spaceship_health_text,
                    alien_health_text)
        
        
    # Quit Pygame
    pg.quit()   
        
# Run the main function only if this file is run as a script        
if __name__ == "__main__":
    main()
    