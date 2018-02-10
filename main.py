import pygame
import sys

from constants import *
from game_level import GameLevel


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    end_game = False
    clock = pygame.time.Clock()
    
    pygame.display.set_caption('Blocker')
    screen.fill((255, 255, 255))
    main_game = GameLevel(screen)
    while not end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        clock.tick(LOOP_FREQUENCY)
        
        main_game.update_state()
        
        pygame.display.update()
    
    return


if __name__ == "__main__":
    main()
