import pygame
import random
from circleshape import CircleShape


def random_velocity():
    speed = random.uniform(50, 100)
    angle = random.uniform(0, 360)
    velocity = pygame.Vector2(speed, 0).rotate(angle)
    return velocity

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = random_velocity()

    def draw(self, screen):
        pygame.draw.circle(screen, "goldenrod", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 