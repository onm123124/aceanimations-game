import os
import pygame
from pygame.math import Vector2
from aceLOGO import Logo
from Background import background  # Check the filename and correct it if needed

pygame.init()
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))

ace = Logo()
sped = ace.velocity
acceleration = ace.acceleration
pos = ace.position
logo_width, logo_height = ace.sprite.get_width()/2, ace.sprite.get_height()/2

background_img = pygame.transform.scale(background().sprite, (screen_width, screen_height))

def main():
    global pos  # Add this line to indicate that pos is a global variable
    pygame.display.set_caption("ACE")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        screen.blit(background_img, (0, 0))

        sped.x += acceleration
        sped.y += acceleration
        pos += sped

        # Center the ACE logo on the screen
        x, y = pos.x - logo_width // 2, pos.y - logo_height // 2
        screen.blit(ace.sprite, (x, y))
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()  # Run the main sequence