import pygame
import random
from constants import *

class Target:
    __Y_OFFSET = 1
    
    def __init__(self, screen, x_coor=0.5*SCREEN_WIDTH):
        self.x_coor = x_coor
        self.y_coor = TARGET_INITIAL_Y
        self.size = TARGET_SIZE
        self.screen = screen
        self.exploding = False
        self.detonate_timer = 0
        self.eaten = False
        self.score = 0
        img_file = self.get_random_img()
        
        self.apple_img = pygame.image.load(img_file)
        self.apple = pygame.transform.scale(self.apple_img, (self.size, self.size))
        # self.apple_erase_img = pygame.image.load(img_file[1])
        # self.apple_erase = pygame.transform.scale(self.apple_erase_img, (100, 100))
        self.explode_img = pygame.image.load("./assets/game_elements/explosion.png")
        self.explode_block = pygame.transform.scale(self.explode_img, (self.size, self.size))
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

    @staticmethod
    def get_random_offset():
        trajectory_pool = TRAJECTORY
        random.shuffle(trajectory_pool)
        return trajectory_pool[0]

    def get_random_img(self):
        type_index = random.randint(0, 1)
        food_list = TARGETS[type_index]
        random.shuffle(food_list)
        if type_index == 1:
            self.score = BAD_SCORE
        else:
            self.score = GOOD_SCORE

        return FOOD[type_index] + food_list[0] + IMG_EXT

    def update_target_state(self):

        if not self.exploding:
            self.move()
            self.draw()
            self.check_y_pos()
        else:
            self.explode()

        

    def check_y_pos(self):
        if self.y_coor >= SCREEN_HEIGHT - MOUTH_HEIGHT and not self.exploding:
            self.eaten = True

    def explode(self):

        if self.detonate_timer < 50:
            self.screen.blit(self.explode_block, (self.x_coor, self.y_coor))
            self.detonate_timer += 1
        else:
            self.y_coor = SCREEN_HEIGHT + 10

    @property
    def end(self):
        return self.y_coor > SCREEN_HEIGHT
