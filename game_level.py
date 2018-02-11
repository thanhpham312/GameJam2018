import random

from constants import *
from target import Target


class GameLevel:
    def __init__(self, screen):
        self.targets = []
        self.screen = screen
    
    def create_target(self, x_coor=0):
        new_target = Target(self.screen, x_coor)
        self.targets.append(new_target)
    
    def update_state(self, tick):

        if len(self.targets) < 10 and tick == TARGET_UPDATE_DELAY:
            self.create_random_target()

        for entry in self.targets:
            entry.update_target_state()
            if entry.end:
                self.targets.remove(entry)

    def create_random_target(self):
        random_x_coor = random.randint(0, SCREEN_WIDTH - 100)
        self.create_target(random_x_coor)