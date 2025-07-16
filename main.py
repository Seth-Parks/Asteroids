# Author: Brandon Parks
# Project Name: Asteroids

import pygame
#Importing wildcard, since the project is relatively small.
from constants import *
from circleshape import *
from player import *


def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill(color=(0,0,0,))

            player.draw(screen)

            player.update(dt)
            dt = clock.tick(60) / 1000
            pygame.display.flip()

            






            

if __name__ == "__main__":
    main()
