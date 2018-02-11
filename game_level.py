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
        self.eat_count = 0
        self.screen = screen
        self.shooter = Shooter(self.screen)
        self.mouth = Mouth(screen)
        self.total_score = 0
        self.final_score = 0
        self.eating = False
        self.chew_timer = 0
        self.spawn_count = 0
        
    def create_target(self, x_coor=0):
        new_target = Target(self.screen, x_coor)
        self.targets.append(new_target)
        self.spawn_count += 1
    
    def update_state(self, tick):
        
        self.mouth.draw()
        if len(self.targets) < TARGET_LIMIT and tick == TARGET_UPDATE_DELAY and self.spawn_count < SPAWN_LIMIT:
            self.create_random_target()

        for entry in self.targets:
            entry.update_target_state()
            if entry.eaten:
                self.total_score += entry.score
                self.eat_food.append(entry)
                self.targets.remove(entry)
                self.eating = True
                self.eat_count += 1
                
            elif entry.end:
                self.targets.remove(entry)
                
        if self.eat_count == TIM_CAPACITY:
            new_score = 0
            for entry in self.eat_food:
                new_score += (entry.score * 10)
                self.eat_food.remove(entry)
            self.total_score += new_score
            return True
        for bullet in self.shooter.bullets:
            bullet.move()
            if bullet.y_pos < 0:
                self.shooter.bullets.remove(bullet)

        self.shooter.update_shooter()

        if self.eating:
            if self.chew_timer < CHEW_DELAY:
                self.mouth.close()
                self.chew_timer += 1
            else:
                self.mouth.open()
                self.chew_timer = 0
                self.eating = False
        
        self.check_collision()

        # self.final_score = round((self.total_score - self.spawn_count / (SPAWN_LIMIT / TIM_CAPACITY)) * 10)
        self.final_score = self.total_score * 10
        
        if self.spawn_count >= SPAWN_LIMIT and len(self.targets) == 0:
            return True
        
        return False
        
    def check_collision(self):
        for bullet in self.shooter.bullets:
            for target in self.targets:
                if bullet.y_pos <= target.y_coor + target.size - HIT_BOX_PADDING >= bullet.y_pos >= target.y_coor + \
                        HIT_BOX_PADDING and not target.exploding:
                    if target.x_coor + target.size - HIT_BOX_PADDING >= bullet.x_pos >= target.x_coor + HIT_BOX_PADDING\
                            and not target.exploding:
                        self.shooter.bullets.remove(bullet)
                        target.exploding = True
                        self.total_score += (target.score * -1)
                        continue

    def create_random_target(self):
        random_x_coor = random.randint(0, SCREEN_WIDTH - 100)
        self.create_target(random_x_coor)
