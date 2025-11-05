# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the modules
# constants.py and player.py into the 
# current file
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    # Initializing Pygame
    pygame.init()

    # Initializing Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set up screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game variables
    running = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 0

    # Game Loop
    while running:
        for event in pygame.event.get():    # This will check if the the user has
            if event.type == pygame.QUIT:   # closed the window and close the game
                return
        screen.fill((0, 0, 0)) # Fill the Screen with Black

        #Draw the player
        player.draw(screen)
        
        pygame.display.flip()  # Update the full display Surface to the screen
        
        clock.tick(fps) # Set the FPS

if __name__ == "__main__":
    main()
