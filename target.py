import pygame
from constants import *


class Target:
    __X_OFFSET = 1
    __Y_OFFSET = 1
    
    def __init__(self, screen):
        self.x_coor = 0.5 * SCREEN_WIDTH
        self.y_coor = 0
        self.screen = screen
        
        self.apple_img = pygame.image.load('apple.png')
        self.apple = pygame.transform.scale(self.apple_img, (100, 100))
<<<<<<< HEAD
        self.apple_erase_img = pygame.image.load('./assets/food/apple_erase.png')
        self.apple_erase = pygame.transform.scale(self.apple_erase_img, (100, 100))
=======
        self.apple_box = pygame.Surface((100, 100))
        self.apple_box.fill(WHITE)
>>>>>>> b495cab876f0fd0e20ef964e9df00e955db14d71
        
        self.draw()
        
    def draw(self):
        self.screen.blit(self.apple, (self.x_coor, self.y_coor))
        
    def erase(self):
        self.screen.blit(self.apple_erase, (self.x_coor, self.y_coor))
    
    def move(self):
        self.x_coor += Target.__X_OFFSET
        self.y_coor += Target.__Y_OFFSET
    
    def update_target_state(self):
        self.erase()
        self.move()
        self.draw()