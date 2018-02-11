import pygame
import sys

from constants import *
from game_level import GameLevel
from splash import Splash

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end_game = False
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Dreamer')

        background_img = pygame.image.load('./assets/backgrounds/background.png')
        self.background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.screen.blit(self.background, (0, 0))

        self.splash_screen = Splash(self.screen, 'start')

        self.main_game = GameLevel(self.screen)

        self.tick = 0

        self.final_score = 0

        self.game_screen = 1
        return

    def splash(self):
        self.splash_screen.draw()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game_screen += 1
        return

    def run(self):
        while not self.end_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(LOOP_FREQUENCY)

            if self.game_screen == 1:
                self.splash()

            elif self.game_screen == 2:
                self.final_score = self.main_game.final_score
                self.splash_screen = Splash(self.screen, 'playing', str(self.final_score))
                self.splash_screen.draw()
                if self.main_game.update_state(self.tick):
                    # print("Final score: {}pts.".format(self.final_score))
                    # sys.exit()
                    self.game_screen = 3

            elif self.game_screen == 3:
                self.splash_screen = Splash(self.screen, 'end', str(self.final_score))
                self.splash()

            elif self.game_screen == 4:
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
