import pygame
from constants import *

class Shooter():
    def __init__(self, screen, width = SHOOTER_HEIGHT, height = SHOOTER_HEIGHT, x_pos = 0, y_pos = SCREEN_HEIGHT - SHOOTER_HEIGHT):
        self.screen = screen
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = 1
        self.speed_modifier = SHOOTER_SPEED

        self.shooter_img = pygame.image.load('assets/game_elements/archery.png')
        self.shooter = pygame.transform.scale(self.shooter_img, (self.width, self.height))
        self.eraser = pygame.Surface((self.width, self.height))
        self.eraser.set_alpha(0)
        self.eraser.fill(WHITE)

        return

    def move(self):
        # self.erase()
        if self.x_pos < SCREEN_WIDTH:
            self.x_pos += self.speed_modifier
        else:
            self.x_pos = 0
        self.draw()
        return

    def draw(self):
        self.screen.blit(self.shooter, (self.x_pos, self.y_pos))

    def erase(self):
        self.screen.blit(self.eraser, (self.x_pos, self.y_pos))
