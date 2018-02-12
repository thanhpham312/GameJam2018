import pygame
from constants import *

class Splash():
    def __init__(self, screen, type, text = ''):
        self.splash_elements = []
        self.ended = False
        self.screen = screen
        self.type = type
        self.text = text

        self.populate_splash_screen()

        return

    def populate_splash_screen(self):
        if self.type == 'start':
            self.splash_elements.append(TextBox(self.screen, 'ENTER GAME'))
        elif self.type == 'playing':
            total_score_text = TextBox(self.screen, self.text)
            total_score_text.x_pos = 10
            total_score_text.y_pos = 10
            self.splash_elements.append(total_score_text)
        elif self.type == 'end':
            end_score_text = TextBox(self.screen, 'TOTAL SCORE:')
            end_score_text.y_pos = SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_text)

            end_score_number_text = TextBox(self.screen, self.text)
            end_score_number_text.y_pos = 1.5 * SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_number_text)

            end_score_text = TextBox(self.screen, 'A GAME BY:')
            end_score_text.y_pos = 6.5 * SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_text)

            end_score_text = TextBox(self.screen, 'ALDRICH HUANG')
            end_score_text.y_pos = 7.5 * SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_text)

            end_score_text = TextBox(self.screen, 'THANH PHAM')
            end_score_text.y_pos = 8 * SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_text)

            end_score_text = TextBox(self.screen, 'DAVID XIAO')
            end_score_text.y_pos = 8.5 * SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_text)

            end_score_text = TextBox(self.screen, 'IVAN SHALAGIN')
            end_score_text.y_pos = 9 * SCREEN_HEIGHT / 10
            self.splash_elements.append(end_score_text)
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