import random

from constants import *
from target import Target


class GameLevel:
    def __init__(self, screen):
        self.targets = []
        self.screen = screen
    
    def create_target(self, input_x=0):
        new_target = Target(self.screen, input_x)
        self.targets.append(new_target)

    def update_state(self, tick):
        if len(self.targets) < 20 and tick == 60:
            self.create_random_target()
        for entry in self.targets:
            entry.update_target_state()

    def create_random_target(self):
        x_coor = random.randint(0, SCREEN_WIDTH - 100)
        self.create_target(x_coor)