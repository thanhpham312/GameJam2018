import pygame
from constants import *

class Mouth():

    def __init__(self, screen):
        self.screen = screen
        self.lxpos = 20 - MOUTH_WIDTH
        self.ypos = SCREEN_HEIGHT-SCREEN_WIDTH/4
        self.rxpos = SCREEN_WIDTH - 20

        self.left_img = pygame.image.load('assets/game_elements/mouth-left.png')
        self.right_img = pygame.image.load('assets/game_elements/mouth-right.png')
        self.left = pygame.transform.scale(self.left_img, (MOUTH_WIDTH, MOUTH_HEIGHT))
        self.right = pygame.transform.scale(self.right_img, (MOUTH_WIDTH, MOUTH_HEIGHT))

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