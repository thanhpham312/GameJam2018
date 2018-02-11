import pygame
from constants import *

class Shooter():
    def __init__(self, screen, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, x_pos = 0, y_pos = SCREEN_HEIGHT - SHOOTER_HEIGHT):
        self.screen = screen
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = 1
        self.speed_modifier = 0.1

        self.shooter_img = pygame.image.load('./assets/game_elements/archery.png')
        self.apple = pygame.transform.scale(self.shooter_img, (self.width, self.height))
        self.eraser = pygame.Surface((self.width, self.height))
        self.eraser.fill(WHITE)

        return

    def move(self):
        self.erase()
        self.x_pos += self.speed_modifier
        self.draw()
        return

    def draw(self):
        self.screen.blit(self.apple, (self.x_pos, self.y_pos))

    def erase(self):
        self.screen.blit(self.eraser, (self.x_pos, self.y_pos))
