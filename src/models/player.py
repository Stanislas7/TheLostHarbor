import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        # Load the image and resize it
        original_image = pygame.image.load(image_path).convert_alpha()
        original_rect = original_image.get_rect()
        new_size = (original_rect.width // 7, original_rect.height // 7) 
        self.image = pygame.transform.scale(original_image, new_size)

        # Initialize position and velocity attributes
        self.velocity = [0, 0]
        self._position = [186, 1323] # Initial position specific to level 1
        self._old_position = self._position[:]
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.3, 4)  # Rectangle for collisions

    @property
    def position(self) -> list[float]:
        return list(self._position)

    @position.setter
    def position(self, value: list[float]) -> None:
        self._position = list(value)
    
    def reset_position(self, position):
        self.position = position
        self.velocity = [0, 0]
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def update(self, dt: float) -> None:
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt: float) -> None:
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom
