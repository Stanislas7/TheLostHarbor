import pygame

def draw_text(surface, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def draw_button(surface, x, y, width, height, text, text_color, button_color):
    pygame.draw.rect(surface, button_color, (x, y, width, height))
    draw_text(surface, text, text_color, x + width // 2, y + height // 2)
