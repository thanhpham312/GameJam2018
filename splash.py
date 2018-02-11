import pygame
from constants import *

class Splash():
    def __init__(self, screen):
        self.splash_elements = []
        self.ended = False
        self.splash_elements.append(EnterButton(screen))
        return

    def draw(self):
        for element in self.splash_elements:
            element.draw()

class EnterButton():
    def __init__(self, screen, width = SPLASH_WIDTH, height = SPLASH_HEIGHT*2, x_pos = SCREEN_WIDTH/2 - SPLASH_WIDTH/2, y_pos = 4*SCREEN_HEIGHT/5 - SPLASH_HEIGHT):
        self.screen = screen
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

        enter_button_font = pygame.font.Font('./assets/font/prstartk.ttf', SPLASH_HEIGHT)
        self.enter_button_surface = enter_button_font.render('ENTER GAME', False, (WHITE))

        return

    def draw(self):
        self.screen.blit(self.enter_button_surface, (self.x_pos, self.y_pos))
        return