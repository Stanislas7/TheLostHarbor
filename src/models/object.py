import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, level, can_be_collected=True):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.can_be_collected = can_be_collected
        self.level = level
        self.collected = False