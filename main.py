import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updateable)
    AsteroidField.containers = updateable
    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                return

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
