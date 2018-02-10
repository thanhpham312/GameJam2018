import pygame
from constants import *


class Target:
    __X_OFFSET = 1
    __Y_OFFSET = 1
    
    def __init__(self, screen):
        self.x_coor = 0.5 * SCREEN_WIDTH
        self.y_coor = 0
        self.screen = screen
        
        self.apple_img = pygame.image.load('./assets/food/apple.png')
        self.apple = pygame.transform.scale(self.apple_img, (100, 100))
        self.apple_box = pygame.Surface((100, 100))
        self.apple_box.fill(WHITE)
        
        self.draw()
        
    def draw(self):
        self.screen.blit(self.apple, (self.x_coor, self.y_coor))
        
    def erase(self):
        self.screen.blit(self.apple_box, (self.x_coor, self.y_coor))
    
    def move(self):
        self.x_coor += Target.__X_OFFSET
        self.y_coor += Target.__Y_OFFSET
    
    def update_target_state(self):
        self.erase()
        self.move()
        self.draw()