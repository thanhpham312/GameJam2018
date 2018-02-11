import pygame
import sys

from constants import *
from game_level import GameLevel

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end_game = False
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Blocker')

        background_img = pygame.image.load('assets/backgrounds/background.jpg')
        self.background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.screen.blit(self.background, (0, 0))
        self.main_game = GameLevel(self.screen)

        self.tick = 0
        return

    def run(self):
        while not self.end_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(LOOP_FREQUENCY)

            if self.main_game.update_state(self.tick):
                final_score = round((self.main_game.total_score - self.main_game.spawn_count / (SPAWN_LIMIT / TIM_CAPACITY)) * 10)
                print("Final score: {}pts.".format(final_score))
                sys.exit()

            pygame.display.update()
            if self.tick == TARGET_UPDATE_DELAY:
                self.tick = -1

            self.tick += 1

            self.screen.blit(self.background, (0, 0))
        return


if __name__ == "__main__":
    newgame = Game()
    newgame.run()
