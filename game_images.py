#TODO: 
# - find a way to make the images adjust to the screen if screen size is changed 
#       especially the ones that depend on the screen size like the background 
#       maybe use pygame.display.get_wiondow_size()?
# - check if you can get the dimensions after all transformations 
#       instead of with each one
# - check naming convention for images in python and pygame
#       because some of these names are longer than your life expectancy

import pygame
import os 


#Constants for screen size.
W_WIDTH, W_HEIGHT = 1400, 700

'''
Getting the images from the Assets directory and getting their dimensions (Width & Height)
'''
ORIGINAL_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship.png"))
ORIGINAL_SPACESHIP_WIDTH, ORIGINAL_SPACESHIP_HEIGHT = ORIGINAL_SPACESHIP_IMAGE.get_width(), ORIGINAL_SPACESHIP_IMAGE.get_height()
ORIGINAL_ALIEN_IMAGE = pygame.image.load(os.path.join("Assets", "alien.png"))
ORIGINAL_ALIEN_WIDTH, ORIGINAL_ALIEN_HEIGHT = ORIGINAL_ALIEN_IMAGE.get_width(), ORIGINAL_ALIEN_IMAGE.get_height()
ORIGINAL_GAMEPLAY_BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))
ORIGINAL_ENDGAME_BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "endgame_space_background.png"))
'''
Rotating the images to face the direction of movement (if necessary)
and getting the new dimensions (Width & Height)
'''
ANGLE = 90
ROTATED_SPACESHIP_IMAGE = pygame.transform.rotate(ORIGINAL_SPACESHIP_IMAGE, -ANGLE)
ROTATED_SPACESHIP_WIDTH, ROTATED_SPACESHIP_HEIGHT = ROTATED_SPACESHIP_IMAGE.get_width(), ROTATED_SPACESHIP_IMAGE.get_height()


'''
Scaling the images (if necessary) and getting the new dimensions (Width & Height)
'''
SCALE = 1.5
SCALED_SPACESHIP_WIDTH, SCALED_SPACESHIP_HEIGHT = int(SCALE*ROTATED_SPACESHIP_WIDTH), int(SCALE*ROTATED_SPACESHIP_HEIGHT)
SCALED_SPACESHIP_IMAGE = pygame.transform.scale(ROTATED_SPACESHIP_IMAGE, (SCALED_SPACESHIP_WIDTH, SCALED_SPACESHIP_HEIGHT))
SCALED_ALIEN_WIDTH, SCALED_ALIEN_HEIGHT = int(SCALE*ORIGINAL_ALIEN_WIDTH), int(SCALE*ORIGINAL_ALIEN_HEIGHT)
SCALED_ALIEN_IMAGE = pygame.transform.scale(ORIGINAL_ALIEN_IMAGE, (SCALED_ALIEN_WIDTH, SCALED_ALIEN_HEIGHT))

#Scaled winner image
SPACESHIP_WIN_IMAGE_WIDTH, SPACESHIP_WIN_IMAGE_HEIGHT = int(5*ORIGINAL_SPACESHIP_WIDTH), int(5*ORIGINAL_SPACESHIP_HEIGHT)
SPACESHIP_WIN_IMAGE = pygame.transform.scale(ORIGINAL_SPACESHIP_IMAGE, (SPACESHIP_WIN_IMAGE_WIDTH, SPACESHIP_WIN_IMAGE_HEIGHT))
ALIEN_WIN_IMAGE_WIDTH, ALIEN_WIN_IMAGE_HEIGHT = int(5*ORIGINAL_ALIEN_WIDTH), int(5*ORIGINAL_ALIEN_HEIGHT)
ALIEN_WIN_IMAGE = pygame.transform.scale(ORIGINAL_ALIEN_IMAGE, (ALIEN_WIN_IMAGE_WIDTH, ALIEN_WIN_IMAGE_HEIGHT))


# SCALE THE BACKGROUND IMAGE TO FIT THE WINDOW
SCALED_GAMEPLAY_BACKGROUND_IMAGE = pygame.transform.scale(ORIGINAL_GAMEPLAY_BACKGROUND_IMAGE, (W_WIDTH, W_HEIGHT))
SCALED_ENDGAME_BACKGROUND_IMAGE = pygame.transform.scale(ORIGINAL_ENDGAME_BACKGROUND_IMAGE, (W_WIDTH, W_HEIGHT))
'''
Flipping the images to face the opposite direction if necessary
'''
FLIPPED_SPACESHIP_IMAGE = pygame.transform.flip(SCALED_SPACESHIP_IMAGE, True, False)
FLIPPED_ALIEN_IMAGE = pygame.transform.flip(SCALED_ALIEN_IMAGE, True, False)

'''
Final images to be used in the game
'''
SPACESHIP_FINAL_IMAGE = SCALED_SPACESHIP_IMAGE
SPACESHIP_FINAL_WIDTH, SPACESHIP_FINAL_HEIGHT = SCALED_SPACESHIP_WIDTH, SCALED_SPACESHIP_HEIGHT
ALIEN_FINAL_IMAGE = SCALED_ALIEN_IMAGE
ALIEN_FINAL_WIDTH, ALIEN_FINAL_HEIGHT = SCALED_ALIEN_WIDTH, SCALED_ALIEN_HEIGHT
GAMEPLAY_BACKGROUND_FINAL_IMAGE = SCALED_GAMEPLAY_BACKGROUND_IMAGE
ENDGAME_BACKGROUND_FINAL_IMAGE = SCALED_ENDGAME_BACKGROUND_IMAGE