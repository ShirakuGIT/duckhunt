import pygame, sys
from pygame.locals import *



#Initializing the game window
pygame.display.init()

#This just helps with the uninitialization of the game window
running = True

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
duckpic = [duckpic]

#This captions the game window
pygame.display.set_caption("Duck Hunt")

#display the output screen
while running:
    display_surface.blit(image, (0, 0))
    display_surface.blit(duckpic, (200, 200))

    for i in range(10):
        display_surface.blit(duckpick[i], (i*10, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    pygame.time.Clock().tick(frames)


   