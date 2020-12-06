import pygame

def duckimage():
    duckpic = pygame.image.load(r"duckhunt/bird.gif")
    pygame.transform.scale(duckpic, (30, 30))
    display_surface.blit(image, (600, 600))
