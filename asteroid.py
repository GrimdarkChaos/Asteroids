# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the modules
# constants.py and circleshape.py 
# into the current file
from constants import *
from circleshape import *
from logger import log_event

# impoirting random module for asteroid generation
import random

# Asteroid Class child of Circle
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y,new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y,new_radius)
            new_asteroid_1.velocity = (self.velocity.rotate(random_angle)) * 1.2
            new_asteroid_2.velocity = (self.velocity.rotate(-random_angle)) * 1.2
