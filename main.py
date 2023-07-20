import pygame
from pygame.math import Vector2
from Background import background
from aceLOGO import Logo
import math
#more lirary here if neededs 
screen = pygame.display.set_mode((1920,1080))
ace = Logo()
sped = ace.velocity
acceleration = ace.acceleration
pos = ace.position
player_rect = pygame.Rect(pos.x, pos.y,ace.sprite.get_width(), ace.sprite.get_height())

def main():
    pygame.init()
    pygame.display.set_caption("ACE")
    #clean screen
    pygame.display.update
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        screen.blit(background().sprite,(0,0))
        sped.x += acceleration
        sped.y += acceleration
        pos += sped
        screen.blit(ace.sprite, (pos.x,pos.y))

        


if __name__ == "__name__":
    main()#run main sequence