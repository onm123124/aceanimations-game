import pygame
from pygame.math import Vector2
#more lirary here if need

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

if __name__ == "__name__":
    main()#run main sequence