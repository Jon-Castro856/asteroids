import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
Player.containers = (updatable, drawable)
AsteroidField.containers = updatable

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for rock in asteroids:
           if rock.collision_check(player):
               print("Game Over!")
               sys.exit()
        pygame.Surface.fill(screen, (0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()