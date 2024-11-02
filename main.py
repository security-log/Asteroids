import pygame
from constants import * # importa todo desde el archivo constants.py
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # estos valores son para iniciar al player en el medio de la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__": 
    main()
