# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the modules
# constants.py and circleshape.py 
# into the current file
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)