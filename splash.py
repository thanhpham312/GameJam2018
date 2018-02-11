import pygame
from constants import *

class Splash():
    def __init__(self, screen, type, text = ''):
        self.splash_elements = []
        self.ended = False
        if type == 'start':
            self.splash_elements.append(TextBox(screen, 'ENTER GAME'))
        elif type == 'end':
            end_score_text = TextBox(screen, 'TOTAL SCORE:')
            end_score_text.y_pos = 3*SCREEN_HEIGHT/5 - SPLASH_HEIGHT
            self.splash_elements.append(end_score_text)
            self.splash_elements.append(TextBox(screen, text))
            pass
        return

    def draw(self):
        for element in self.splash_elements:
            element.draw()

class TextBox():
    def __init__(self, screen, text =''):
        self.screen = screen

        enter_button_font = pygame.font.Font('./assets/font/prstartk.ttf', SPLASH_HEIGHT)
        self.enter_button_surface = enter_button_font.render(text, False, (WHITE))
        text_rect = self.enter_button_surface.get_rect()

        self.width = text_rect.width
        self.height = text_rect.height
        self.x_pos = SCREEN_WIDTH/2 - self.width/2
        self.y_pos = 4*SCREEN_HEIGHT/5 - self.height

        return

    def draw(self):

        self.screen.blit(self.enter_button_surface, (self.x_pos, self.y_pos))
        return