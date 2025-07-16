# Author: Brandon Parks
# Project Name: Asteroids

import pygame
#Importing wildcard, since the project is relatively small.
from constants import *
from circleshape import *
from player import *


def main():
    #Setting up the logic for the game loop
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            #fill the screen with black
            screen.fill(color=(0,0,0,))
            
            
            
            #draw the player to the screen
            for group in drawable:
                group.draw(screen)





            #update the player's location then calculate the new delta
            updatable.update(dt)
            dt = clock.tick(60) / 1000
            pygame.display.flip()

            






            

if __name__ == "__main__":
    main()
