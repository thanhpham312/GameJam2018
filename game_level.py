from constants import *
from target import Target


class GameLevel:
    def __init__(self, screen):
        self.targets = []
        self.screen = screen
        self.create_target()
    
    def create_target(self):
        new_target = Target(self.screen)
        self.targets.append(new_target)
    
    def update_state(self):
        for entry in self.targets:
            entry.update_target_state()