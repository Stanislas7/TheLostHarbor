import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, ICON_PATH

def init_screen() -> pygame.Surface:
    """
    Initialize and return a screen with the dimensions specified in settings.py
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(TITLE)

    if ICON_PATH:
        icon = pygame.image.load(ICON_PATH).convert_alpha()
        pygame.display.set_icon(icon)
    
    return screen
