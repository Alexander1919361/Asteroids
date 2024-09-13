import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        # Pass x, y and PLAYER_RADIUS to the parent class
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize additional Player attributes
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)