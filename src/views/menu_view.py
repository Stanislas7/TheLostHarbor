import pygame
from src.utils.draw_functions import draw_button, draw_text

class MenuView:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = pygame.Rect((self.screen.get_width() - 400) // 2, 250, 400, 50)
        self.info_button = pygame.Rect((self.screen.get_width() - 400) // 2, 350, 400, 50)

    def display_menu(self):
        self.screen.fill((0, 0, 255))
        draw_text(self.screen, "The Lost Harbor", (255, 255, 255), self.screen.get_width() / 2, 30)

        button_color = (139, 69, 19)
        draw_button(self.screen, *self.play_button, "Play", (255, 255, 255), button_color)
