import pygame as pg
import game_colors as gc
import game_images as gi
import game_fonts as gf
from Player import Player
from Bullet import Bullet
from Button import Button
pg.init() 
W_WIDTH, W_HEIGHT = 1400, 700
WINDOW = pg.display.set_mode((W_WIDTH, W_HEIGHT),pg.RESIZABLE)
pg.display.set_caption("SPACE DUEL!")
FPS = 120
SHIP_HIT = pg.USEREVENT + 1
ALIEN_HIT = pg.USEREVENT + 2
PLAYER_DEATH = pg.USEREVENT + 3
win_font = gf.GAME_FONT_INACTIVE
health_font = gf.GAME_FONT_ACTIVE
start_button_image = gi.START_BUTTON_FINAL_IMAGE
exit_button_image = gi.EXIT_BUTTON_FINAL_IMAGE
reset_button_image = gi.RESET_BUTTON_FINAL_IMAGE
spaceship_image = gi.SPACESHIP_FINAL_IMAGE
spaceship_image_flipped = gi.FLIPPED_SPACESHIP_IMAGE
alien_image = gi.ALIEN_FINAL_IMAGE
active_background_image = gi.GAMEPLAY_BACKGROUND_FINAL_IMAGE
inactive_background_image = gi.ENDGAME_BACKGROUND_FINAL_IMAGE
spaceship_keys = {'U': pg.K_w, 'D': pg.K_s, 'L': pg.K_a, 'R': pg.K_d}
alien_keys = {'U': pg.K_UP, 'D': pg.K_DOWN, 'L': pg.K_LEFT, 'R': pg.K_RIGHT}
def handle_bullets(spaceship, alien,spaceship_bullets, alien_bullets):
    for bullet in spaceship_bullets:
        bullet.move(spaceship, alien)
        if bullet.collision(alien):
            pg.event.post(pg.event.Event(ALIEN_HIT))
            spaceship_bullets.remove(bullet)
        elif bullet.isOffScreen(W_WIDTH):
            spaceship_bullets.remove(bullet)
    for bullet in alien_bullets:
        bullet.move(alien, spaceship)
        if bullet.collision(spaceship):
            pg.event.post(pg.event.Event(SHIP_HIT))
            alien_bullets.remove(bullet)
        elif bullet.isOffScreen(W_WIDTH):
            alien_bullets.remove(bullet)
def draw_text_with_outline(x, y,text, font, color, outline_color,surface, thickness = 2): 
    textobj = font.render(text, 1, color)
    outlineobj = font.render(text, 1, outline_color)
    (x,y) = (x - textobj.get_width()/2, y - textobj.get_height()/2)
    for i in range(1, thickness):
        surface.blit(outlineobj, (x-i, y-i))
        surface.blit(outlineobj, (x+i, y-i))
        surface.blit(outlineobj, (x-i, y+i))
        surface.blit(outlineobj, (x+i, y+i))
    surface.blit(textobj, (x,y))
def draw_window(spaceship, alien,spaceship_bullets = [], alien_bullets = [],spaceship_health_string = "", alien_health_string = ""):
    spaceship_health_string = "Spaceship Health: " + str(spaceship.health)
    alien_health_string = "Alien Health: " + str(alien.health) 
    WINDOW.blit(active_background_image, (0,0))
    draw_text_with_outline(W_WIDTH//7, W_HEIGHT/14, spaceship_health_string, health_font, gc.R_FIRE1, gc.BLACK, WINDOW, 3)
    draw_text_with_outline(6*W_WIDTH//7, W_HEIGHT/14, alien_health_string, health_font, gc.B_FIRE1, gc.BLACK, WINDOW, 3)
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
game_state = 0
winner = ""
def start_screen():
    global game_state
    clock = pg.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state = -1
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if start_button.is_hover(mouse_pos):
                    game_state = 1
                    return
                elif exit_button.is_hover(mouse_pos):
                    game_state = -1
                    return
        WINDOW.blit(inactive_background_image, (0,0))
        start_button = Button(W_WIDTH/3 - gi.START_BUTTON_FINAL_WIDTH/2, W_HEIGHT/2 - gi.START_BUTTON_FINAL_HEIGHT/2, gi.START_BUTTON_FINAL_WIDTH, gi.START_BUTTON_FINAL_HEIGHT, start_button_image)
        exit_button = Button(2*W_WIDTH/3 - gi.EXIT_BUTTON_FINAL_WIDTH/2, W_HEIGHT/2 - gi.EXIT_BUTTON_FINAL_HEIGHT/2, gi.EXIT_BUTTON_FINAL_WIDTH, gi.EXIT_BUTTON_FINAL_HEIGHT, exit_button_image)
        start_button.draw(WINDOW)
        exit_button.draw(WINDOW)
        pg.display.update()
def game_play():
    global game_state
    global winner
    spaceship = Player((W_WIDTH/5)-gi.SCALED_SPACESHIP_WIDTH/2,(W_HEIGHT/2)-gi.SCALED_SPACESHIP_HEIGHT/2,gi.SPACESHIP_FINAL_WIDTH,gi.SPACESHIP_FINAL_HEIGHT,spaceship_image,spaceship_keys)
    alien = Player((4*W_WIDTH/5)-gi.SCALED_ALIEN_WIDTH/2,(W_HEIGHT/2)-gi.SCALED_ALIEN_HEIGHT/2,gi.ALIEN_FINAL_WIDTH,gi.ALIEN_FINAL_HEIGHT,alien_image,alien_keys)
    spaceship_bullets = []
    alien_bullets = []
    clock = pg.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                game_state = -1
                return               
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    if spaceship.x < alien.x:
                        print("Z key pressed")
                        spaceship_bullet = Bullet(spaceship.x + spaceship.width,spaceship.y + spaceship.height/2 - Bullet.BULLET_HEIGHT/2,gc.R_FIRE,1)
                        spaceship_bullets.append(spaceship_bullet)
                        print("player 1 bullet created")
                    else:
                        print("Z key pressed")
                        spaceship_bullet = Bullet(spaceship.x,spaceship.y + spaceship.height/2 - Bullet.BULLET_HEIGHT/2,gc.R_FIRE,-1)
                        spaceship_bullets.append(spaceship_bullet)
                        print("player 1 bullet created")
                if event.key == pg.K_SLASH:
                    if spaceship.x < alien.x:
                        print("/ key pressed")
                        bullet = Bullet(alien.x,alien.y + alien.height/2 - Bullet.BULLET_HEIGHT/2,gc.B_FIRE,-1)
                        alien_bullets.append(bullet)
                        print("player 2 bullet created")
                    else:
                        print("/ key pressed")
                        bullet = Bullet(alien.x + alien.width,alien.y + alien.height/2 - Bullet.BULLET_HEIGHT/2,gc.B_FIRE,1)
                        alien_bullets.append(bullet)
                        print("player 2 bullet created")
            if event.type == PLAYER_DEATH:
                print("PLAYER DEATH")
                if spaceship.health <= 0:
                    winner = "alien"
                    print("ALIEN WINS!")
                elif alien.health <= 0:
                    winner = "spaceship"
                    print("SPACESHIP WINS!")
                game_state = 2
                return
            if event.type == SHIP_HIT:
                print("SHIP HIT")
                if spaceship.health > 0:
                    spaceship.health -= 1
                    print(spaceship.health)
            if event.type == ALIEN_HIT:
                print("ALIEN HIT")
                if alien.health > 0:
                    alien.health -= 1
                    print(alien.health)
            if spaceship.health <= 0 or alien.health <= 0:
                pg.event.post(pg.event.Event(PLAYER_DEATH))
        spaceship.movement_handler()
        alien.movement_handler()
        handle_bullets(spaceship, alien, spaceship_bullets, alien_bullets)
        draw_window(spaceship,alien,spaceship_bullets, alien_bullets)    
        pg.display.update()       
def end_screen(winner = ""):
    global game_state
    spaceship_winning_string = "SPACESHIP WINS!"
    alien_winning_string = "ALIEN WINS!"
    clock = pg.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state = -1
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if reset_button.is_hover(mouse_pos):
                    game_state = 1
                    return
                elif exit_button.is_hover(mouse_pos):
                    game_state = -1
                    return
        WINDOW.blit(inactive_background_image, (0,0))
        if winner == "spaceship":
            print("spaceship winner drawing")
            WINDOW.blit(gi.SPACESHIP_WIN_IMAGE,(W_WIDTH/2 - gi.SPACESHIP_WIN_IMAGE_WIDTH/2,W_HEIGHT/2 - gi.SPACESHIP_WIN_IMAGE_HEIGHT/2))
            draw_text_with_outline(W_WIDTH/2,40 + W_HEIGHT/2 + gi.SPACESHIP_WIN_IMAGE_HEIGHT/2,spaceship_winning_string,win_font,gc.R_FIRE1,gc.BLACK,WINDOW,3)
        elif winner == "alien":
            WINDOW.blit(gi.ALIEN_WIN_IMAGE,(W_WIDTH/2 - gi.ALIEN_WIN_IMAGE_WIDTH/2,W_HEIGHT/2 - gi.ALIEN_WIN_IMAGE_HEIGHT/2))
            draw_text_with_outline(W_WIDTH/2,40 + W_HEIGHT/2 + gi.ALIEN_WIN_IMAGE_HEIGHT/2,alien_winning_string, win_font, gc.B_FIRE1,gc.BLACK,WINDOW,3)
            
        reset_button = Button(W_WIDTH/3 - gi.RESET_BUTTON_FINAL_WIDTH/2,W_HEIGHT/2 - gi.RESET_BUTTON_FINAL_HEIGHT/2,gi.RESET_BUTTON_FINAL_WIDTH, gi.RESET_BUTTON_FINAL_HEIGHT,reset_button_image)
        reset_button.draw(WINDOW)
        exit_button = Button(2*W_WIDTH/3 - gi.EXIT_BUTTON_FINAL_WIDTH/2,W_HEIGHT/2 - gi.EXIT_BUTTON_FINAL_HEIGHT/2,gi.EXIT_BUTTON_FINAL_WIDTH,gi.EXIT_BUTTON_FINAL_HEIGHT,exit_button_image)
        exit_button.draw(WINDOW)
        pg.display.update()      
if __name__ == "__main__":
    while game_state != -1:
        if game_state == 0:
            print("start screen")
            start_screen()
        elif game_state == 1:
            print("gameplay")
            game_play()
        elif game_state == 2:
            print("end screen")
            print("winner: ", winner)
            end_screen(winner)
    print("quitting the game")    
    pg.quit()