# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the module
# constants.py into the current file
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    # Initializing Pygame
    pygame.init()

    # Set up screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game variables
    running = True

    # Game Loop
    while running:
        for event in pygame.event.get():    # This will check if the the user has
            if event.type == pygame.QUIT:   # closed the window and close the game
                return
        screen.fill((0, 0, 0)) # Fill the Screen with Black
        pygame.display.flip()  # Update the full display Surface to the screen

if __name__ == "__main__":
    main()
