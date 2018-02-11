import pygame
import sys

from constants import *
from game_level import GameLevel
from shooter import Shooter


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    end_game = False
    clock = pygame.time.Clock()
    
    pygame.display.set_caption('Blocker')
    background_img = pygame.image.load('assets/backgrounds/background.jpg')
    background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0, 0))
    main_game = GameLevel(screen)

    tick = 0

    while not end_game:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        clock.tick(LOOP_FREQUENCY)
        
        main_game.update_state(tick)

        pygame.display.update()
        if tick == TARGET_UPDATE_DELAY:
            tick = -1

        tick += 1


    
    return


if __name__ == "__main__":
    main()
