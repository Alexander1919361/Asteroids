import pygame
from constants import *
from player import Player

def main():
    
    print("""Starting asteroids!
Screen width: 1280
Screen height: 720""")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()