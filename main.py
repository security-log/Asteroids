import pygame
import sys
from constants import * # importa todo desde el archivo constants.py
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # estos valores son para iniciar al player en el medio de la pantalla

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    asteroid_field = AsteroidField()

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if asteroid.if_collision(player):
                sys.exit("Game over!")


        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__": 
    main()
