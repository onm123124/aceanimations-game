import pygame
from pygame import Vector2
class Logo():
    def __init__(self):
        self.sprite = pygame.image.load('sprites/ace.png')  # Corrected image path
        self.position = Vector2(750, 990)  # Use pygame.Vector2 directly, not pygame.Vector2
        self.velocity = pygame.Vector2(0,-5)
        self.acceleration = 0.1