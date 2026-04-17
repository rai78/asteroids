"""Asteroids class"""


import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_asteroid = self.velocity.rotate(random_angle)
        second_asteroid = self.velocity.rotate(-random_angle)
        first_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        second_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, first_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, second_asteroid_radius)
        asteroid_1.velocity = first_asteroid * 1.2
        asteroid_2.velocity = second_asteroid * 1.2
