import pygame, sys
from pygame.locals import *

#Initializing the game window
pygame.display.init()

#This just helps with the uninitialization of the game window
running = True

gray = ( 238, 238, 238)

#This initializes the framerate
frames = 30

#This sets the display size
display_surface = pygame.display.set_mode(size=(800, 600))

#Loads the image background
image = pygame.image.load(r"duckhunt/bettercity.gif")
image = pygame.transform.scale(image, (810, 660))

#Ducks images
duckpic = pygame.image.load(r"duckhunt/bird.gif")
duckpic = pygame.transform.scale(duckpic, (75, 75))
duckpic = pygame.transform.flip(duckpic, True, False)

#Crosshair images
c_hair = pygame.image.load(r"duckhunt/crosshair.png")
c_hair = pygame.transform.scale(c_hair, (25, 27))
'''c_hair = pygame.Surface.set_colorkey(None) <=== Work on this line'''

pygame.mouse.set_visible(False)

#This captions the game window
pygame.display.set_caption("Duck Hunt")
 
#display the output screen
while running:
    display_surface.blit(image, (0, 0))
    display_surface.blit(duckpic, (200, 200))
    mouse_cursor = pygame.mouse.get_pos()
    x = mouse_cursor[0]
    y = mouse_cursor[1]
    display_surface.blit(c_hair, [x, y])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()
    pygame.time.Clock().tick(frames)


   