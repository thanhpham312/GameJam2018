import pygame
import sys

from constants import *
from game_level import GameLevel
<<<<<<< HEAD
from shooter import Shooter
from mouth import Mouth


=======
>>>>>>> 91375394e36fb71ae2e45f3c64e60779cd8a849e
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

<<<<<<< HEAD
    shooter = Shooter(screen)
    tick = 0

    while not end_game:
        screen.blit(background, (0, 0))
        mouth = Mouth(screen)
        mouth.draw()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            mouth.close()
=======
    tick = 0

    while not end_game:

>>>>>>> 91375394e36fb71ae2e45f3c64e60779cd8a849e
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        clock.tick(LOOP_FREQUENCY)
        
        main_game.update_state(tick)

        pygame.display.update()
        if tick == TARGET_UPDATE_DELAY:
            tick = -1

        tick += 1

        screen.blit(background, (0, 0))
    
    return


if __name__ == "__main__":
    main()
