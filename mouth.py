import pygame
from constants import *

class Mouth():

    def __init__(self, screen):
        self.screen = screen
        self.lxpos = 0-SCREEN_WIDTH/4
        self.ypos = SCREEN_HEIGHT-SCREEN_WIDTH/4
        self.rxpos = SCREEN_WIDTH*3/4

        self.left_img = pygame.image.load('assets/game_elements/mouth-left.png')
        self.right_img = pygame.image.load('assets/game_elements/mouth-right.png')
        self.left = pygame.transform.scale(self.left_img, (int(SCREEN_WIDTH / 2), int(SCREEN_WIDTH / 4)))
        self.right = pygame.transform.scale(self.right_img, (int(SCREEN_WIDTH / 2), int(SCREEN_WIDTH / 4)))

    def draw(self):
        self.screen.blit(self.left, (self.lxpos, self.ypos))
        self.screen.blit(self.right, (self.rxpos, self.ypos))

    def close(self):
        self.lxpos = 0
        self.rxpos = SCREEN_WIDTH/2
        self.draw()


if __name__ == '__main__':
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    m=Mouth(screen)
    m.draw()