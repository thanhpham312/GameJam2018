import random
import pygame

from shooter import Shooter
from constants import *
from target import Target
from mouth import Mouth


class GameLevel:
    def __init__(self, screen):
        self.targets = []
        self.eat_food = []
        self.screen = screen
        self.shooter = Shooter(self.screen)
        self.mouth = Mouth(screen)
        self.total_score = 0
        self.eating = False
        self.chew_timer = 0
        
    def create_target(self, x_coor=0):
        new_target = Target(self.screen, x_coor)
        self.targets.append(new_target)
    
    def update_state(self, tick):
        if not self.eating:
            self.mouth.draw()
            if len(self.targets) < 10 and tick == TARGET_UPDATE_DELAY:
                self.create_random_target()

            for entry in self.targets:
                entry.update_target_state()
                if entry.eaten:
                    self.eat_food.append(entry)
                    self.targets.remove(entry)
                if entry.end:
                    self.targets.remove(entry)
            if len(self.eat_food) > 0:
                new_score = 0
                for entry in self.eat_food:
                    new_score += entry.score
                    self.eat_food.remove(entry)
                self.total_score += new_score
                self.eating = True
            for bullet in self.shooter.bullets:
                bullet.move()
                if bullet.y_pos < 0:
                    self.shooter.bullets.remove(bullet)

            self.shooter.update_shooter()
        else:

            for entry in self.targets:
                entry.draw()
            if self.chew_timer < 10:
                self.mouth.close()
                self.chew_timer += 1
            else:
                self.mouth.open()
                self.chew_timer = 0
                self.eating = False

            self.shooter.draw()

    def create_random_target(self):
        random_x_coor = random.randint(0, SCREEN_WIDTH - 100)
        self.create_target(random_x_coor)