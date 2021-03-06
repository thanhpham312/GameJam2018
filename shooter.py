import pygame
from constants import *
from bullet import Bullet

class Shooter():
    def __init__(self, screen, width = SHOOTER_HEIGHT, height = SHOOTER_HEIGHT, x_pos = SCREEN_WIDTH/2 - SHOOTER_WIDTH/2
                 , y_pos = SCREEN_HEIGHT - SHOOTER_HEIGHT - MOUTH_HEIGHT):
        self.bullets = []

        self.screen = screen
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = 1
        self.move_distance = SHOOTER_MOVE_DISTANCE
        self.speed_modifier = SHOOTER_SPEED
        self.shooting = False

        self.shooter_img = pygame.image.load('./assets/game_elements/shooter.png')
        self.shooter = pygame.transform.scale(self.shooter_img, (self.width, self.height))
        self.eraser = pygame.Surface((self.width, self.height))
        self.eraser.set_alpha(0)
        self.eraser.fill(WHITE)

        return

    def move(self, direction):
        # self.erase()

        if direction == 'left' and self.x_pos > 0:
            self.x_pos -= self.move_distance*self.speed_modifier
        elif direction == 'right' and self.x_pos < SCREEN_WIDTH - self.width:
            self.x_pos += self.move_distance*self.speed_modifier
        # self.draw()
        return

    def update_shooter(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move('left')
        elif keys[pygame.K_d]:
            self.move('right')
        if keys[pygame.K_SPACE] and not self.shooting:
            self.shoot()
            self.shooting = True
        elif not keys[pygame.K_SPACE] and self.shooting:
            self.shooting = False
        self.draw()

    def shoot(self):
        if len(self.bullets) < BULLET_LIMIT:
            self.bullets.append(Bullet(self.screen, self.x_pos + self.width/2.5, self.y_pos))

    def draw(self):
        self.screen.blit(self.shooter, (self.x_pos, self.y_pos))

    def erase(self):
        self.screen.blit(self.eraser, (self.x_pos, self.y_pos))
