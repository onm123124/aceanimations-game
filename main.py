import os
import pygame
from pygame.math import Vector2
from aceLOGO import Logo
from Background import background  # Check the filename and correct it if needed

pygame.init()
screen_width, screen_height = 1200, 1200
screen = pygame.display.set_mode((screen_width, screen_height))

ace = Logo()
sped = ace.velocity
acceleration = ace.acceleration
pos = Vector2(screen_width // 2, screen_height)  # Set the initial position at the bottom of the screen
logo_width, logo_height = ace.sprite.get_width() // 2, ace.sprite.get_height() // 2

background_img = pygame.transform.scale(background().sprite, (screen_width, screen_height))

def main():
    global pos  # Add this line to indicate that pos is a global variable
    pygame.display.set_caption("ACE")
    clock = pygame.time.Clock()  # Create the Clock object
    running = True
    show_text = False
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time >= 15000:  # 15 seconds (15000 milliseconds)
            show_text = True

        screen.blit(background_img, (0, 0))

        # Update the position with velocity and acceleration
        sped.y += acceleration
        pos.y -= sped.y

        # If the logo goes above the screen, reset its position to the bottom
        if pos.y + logo_height < 0:
            pos.y = screen_height

        # Center the ACE logo on the screen
        x, y = pos.x - logo_width, pos.y - logo_height
        screen.blit(ace.sprite, (x, y))

        # Display the text if show_text is True
        if show_text:
            font = pygame.font.Font(None, 36)  # You can adjust the font size here
            text = font.render("make me admin NOW or I come to your house", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Set the frame rate to 60 frames per second

if __name__ == "__main__":
    main()  # Run the main sequence
