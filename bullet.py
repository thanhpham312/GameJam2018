import pygame
from constants import *


class Bullet():
    def __init__(self, screen, x_pos, y_pos, width = BULLET_WIDTH, height = BULLET_HEIGHT):
        self.screen = screen
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.move_distance = BULLET_MOVE_DISTANCE
        self.speed = BULLET_SPEED

        self.bullet_img = pygame.image.load('assets/game_elements/bullet.png')
        self.bullet = pygame.transform.scale(self.bullet_img, (self.width, self.height))
        return

    def move(self):
        self.draw()
        self.y_pos -= self.move_distance*self.speed
        return

    def draw(self):
        self.screen.blit(self.bullet, (self.x_pos, self.y_pos))
        return
