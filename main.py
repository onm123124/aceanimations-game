import pygame
from pygame.math import Vector2
from Background import background
#more lirary here if neededs 
screen = pygame.display.set_mode((900,900))
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
        screen.blit(background.sprite,(0,0))


if __name__ == "__name__":
    main()#run main sequence