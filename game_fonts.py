#TODO:
# - read more into fonts and pygame to explore more options
# - add other sizes and/or fonts if needed to the file to use in the game

'''
fonts for the game
'''
import pygame as pg
import os

pg.font.init()
#Font to use while the game is running (i.e. the game has started and no one lost yet)
GAME_FONT_ACTIVE = pg.font.Font(os.path.join('Assets', 'Arcade.ttf'), 50)
#Font to use for static states (i.e. the start button and the end of game text "player x won")
GAME_FONT_INACTIVE = pg.font.Font(os.path.join('Assets', 'Arcade.ttf'), 70)