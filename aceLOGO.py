import pygame
from pygame import Vector2
class Logo():
    def __init__(self):
        self.sprite = pygame.image.load('sprites/ace.png')
        self.position = pygame.vector2(750,1080)
        self.velocity = pygame.Vector2(0,-5)
        self.acceleration = 0.0