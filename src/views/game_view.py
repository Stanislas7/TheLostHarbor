import pygame
import pyscroll
from pytmx.util_pygame import load_pygame
from src.models.object import Object
import properties

class GameView:
    def __init__(self, screen, map, player, static_objects, level):
        self.screen = screen
        self.player = player
        self.level = level
        self.target = properties.TARGETS.get(self.level, {})['coins']
        
        # Import the Tiled map with pyscroll
        map_data = pyscroll.data.TiledMapData(map)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 2

        # Create the sprite group with pyscroll
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)
        self.group.add(self.player)

        # Add static objects to the pyscroll group
        for obj in static_objects:
            self.group.add(obj)

    # Function called at each frame (update) to draw all elements on the screen
    def draw(self, state, coins_collected):
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.update_message(state, coins_collected)

    def center_view_on_player(self):
        self.group.center(self.player.rect.center)
        
    def update_message(self, state, coins_collected):
        font = pygame.font.Font(None, 36)
        text_color = (255, 255, 255)
        background_color = (0, 0, 0)

        # Get the message corresponding to the current level and associated state in properties
        message_for_state = properties.LEVEL_MESSAGES.get(self.level, {}).get(state, "") 

        # If the level is 1 or 3 and the state is 1, display the number of collected coins but not for other states
        if (self.level in [1, 3]) and state == 1:
            message = f"{message_for_state} ({coins_collected}/{self.target})"
        else:
            message = message_for_state
        
        text = font.render(message, True, text_color)
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        text_rect.inflate_ip(10, 10)

        self.screen.fill(background_color, text_rect)
        self.screen.blit(text, text_rect)
