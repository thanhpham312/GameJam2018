import pygame
import random
from constants import *

class Target:
    __Y_OFFSET = 1
    
    def __init__(self, screen, x_coor=0.5*SCREEN_WIDTH):
        self.x_coor = x_coor
        self.y_coor = 0
        self.size = 100
        self.screen = screen
        self.exploding = False

        img_file = self.get_random_img()
        
        self.apple_img = pygame.image.load(img_file)
        self.apple = pygame.transform.scale(self.apple_img, (self.size, self.size))
        # self.apple_erase_img = pygame.image.load(img_file[1])
        # self.apple_erase = pygame.transform.scale(self.apple_erase_img, (100, 100))
        self.x_offset = self.get_random_offset()
        self.draw()
        
    def draw(self):
        self.screen.blit(self.apple, (self.x_coor, self.y_coor))
        
    def erase(self):
        self.screen.blit(self.apple_erase, (self.x_coor, self.y_coor))
    
    def move(self):
        self.x_coor += self.x_offset
        if self.x_coor + self.size > SCREEN_WIDTH or self.x_coor < 0:
            self.x_coor -= self.x_offset
            self.x_offset *= -1
        self.y_coor += Target.__Y_OFFSET

    def get_random_offset(self):
        trajectory_pool = TRAJECTORY
        random.shuffle(trajectory_pool)
        return trajectory_pool[0]

    @staticmethod
    def get_random_img():
        type_index = random.randint(0, 1)
        food_list = TARGETS[type_index]
        random.shuffle(food_list)

        return FOOD[type_index] + food_list[0] + IMG_EXT

    def update_target_state(self):

        # self.erase()
        #self.erase()

        self.move()
        self.draw()

        self.test_explosion()

    def test_explosion(self):
        if self.y_coor <= 150:
            self.exploding = True

    @property
    def end(self):
        return self.y_coor > SCREEN_HEIGHT
