# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

# import everything from the modules
# into the current file
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Import logger
from logger import log_state, log_event

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
    # Initializing Pygame
    pygame.init()

    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Adding objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)


    # Initializing Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField() # Initialize asteroid field
    pygame.font.init() # Initialize font module

    # Set up screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    # Game variables
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 30) # Use Arial font, size 30
    dt = 0
    player_score = 0

    # Game Loop
    while running:
        for event in pygame.event.get():    # This will check if the the user has
            if event.type == pygame.QUIT:   # closed the window and close the game
                return
        
        log_state() # Initializing Logger
        
        screen.fill((0, 0, 0)) # Fill the Screen with Black

        score_text_surface = font.render(f"Score: {player_score}", True, (255, 255, 255))
        screen.blit(score_text_surface, (10, 10))

        # Update the Group
        updatable.update(dt)

        # Check for player collision
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Final Score: {player_score}")
                sys.exit()

        # Check for asteroid hit
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.detect_collision(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    player_score += ASTEROID_KILL_POINTS

        # Draw the Group
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()  # Update the full display Surface to the screen
        
        dt = clock.tick(60) / 1000 # Set the FPS

if __name__ == "__main__":
    main()
