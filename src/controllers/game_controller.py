import os, pygame
import sys
from pytmx.util_pygame import load_pygame
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from src.models.player import Player
from src.models.object import Object
from src.views.game_view import GameView
from settings import PLAYER_SPEED
import properties

class GameController:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.map = load_pygame(properties.MAP_FILES[level])
        self.player = Player("media/player/character.png")
        self.static_objects = self.create_static_objects()
        self.game_view = GameView(screen, self.map, self.player, self.static_objects, self.level)  
        self.running = False
        self.game_view.center_view_on_player()
        self.coin_collected = False
        self.colliding = False
        self.state = 1
        self.walls = self.update_collisions()
        self.coins_collected = 0
        self.level_target = properties.TARGETS.get(level, {})

        # Initialize caves for level transitions
        self.grottes = []
        for obj in self.map.objects:
            if obj.type == "grotte":
                self.grottes.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def update_collisions(self):
        # Update collision walls based on map objects
        self.walls = []
        for obj in self.map.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        return self.walls

    def create_static_objects(self):
        # Create static objects (coins, portals, etc.) for the current level
        objects = []
        for obj_info in properties.OBJECTS.get(self.level, []):
            obj = Object(obj_info['x'], obj_info['y'], obj_info['image_path'], obj_info['level'], obj_info.get('can_be_collected', True))
            objects.append(obj)
        return objects

    def run(self):
        clock = pygame.time.Clock()
        self.running = True

        while self.running:
            dt = clock.tick(35) / 1000.0
            self.handle_input()
            self.update(dt)
            self.game_view.draw(self.state, self.coins_collected)
            pygame.display.flip()

    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

        # Handle pressed keys
        pressed = pygame.key.get_pressed()
        self.player.velocity = [0, 0]
        if pressed[K_UP]:
            self.player.velocity[1] = -PLAYER_SPEED
        elif pressed[K_DOWN]:
            self.player.velocity[1] = PLAYER_SPEED
        if pressed[K_LEFT]:
            self.player.velocity[0] = -PLAYER_SPEED
        elif pressed[K_RIGHT]:
            self.player.velocity[0] = PLAYER_SPEED
    
    def update(self, dt):
        self.player.update(dt)
        self.check_collisions(dt)
        # Call update_message to display a new message if conditions are met
        self.game_view.update_message(self.state, self.coins_collected)

        if self.player.feet.collidelist(self.walls) > -1:
            self.player.move_back(dt)

        # Transition from level 1 to level 2
        if self.player.feet.collidelist(self.grottes) > -1 and 'coins' in self.level_target and self.coins_collected >= self.level_target['coins']:
            self.transition_to_next_level()
        
        # Transition from level 2 to level 3
        if self.level == 2:
            for obj in self.static_objects:
                # Portal coordinates
                if obj.rect.collidepoint(1440, 155) and self.player.rect.colliderect(obj.rect):
                    self.transition_to_next_level()
                    break
        
        # End of the game
        if self.level == 3:
            for obj in self.static_objects:
                # Boat coordinates
                if obj.rect.collidepoint(1491, 190) and self.player.rect.colliderect(obj.rect):
                    if self.coins_collected < self.level_target['coins']:
                        break
                    else:
                        self.ending_game()
                        break

    def handle_collection(self, obj):
        if not obj.collected and obj:
            
            # If the player is colliding with the boat or portal, they can't collect

            boat_x, boat_y = 1491, 190  
            boat_width, boat_height = 100, 200 
            boat_rect = pygame.Rect(boat_x, boat_y, boat_width, boat_height)
            
            portal_x, portal_y = 1440, 155
            portal_width, portal_height = 40, 40
            portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)

            if not boat_rect.colliderect(obj.rect) and not portal_rect.colliderect(obj.rect):
                obj.collected = True
                self.coins_collected += 1
                collect_sound = pygame.mixer.Sound(os.path.join('sound', 'collect-coin.wav'))
                pygame.mixer.Sound.play(collect_sound)
                obj.kill()

            if self.coins_collected == self.level_target['coins']:
                self.state = 2

    def check_collisions(self, dt):
        for obj in self.static_objects:
            if self.player.rect.colliderect(obj.rect) and obj.can_be_collected and not obj.collected:
                self.handle_collection(obj)
            
    # Function to transition to the next level
    def transition_to_next_level(self):
        success_sound = pygame.mixer.Sound(os.path.join('sound', 'winning-game-sound-effect.wav'))
        pygame.mixer.Sound.play(success_sound)

        # Increment level, reload map, reset collected coins, reset state, reset player position
        self.level += 1
        self.map = load_pygame(properties.MAP_FILES[self.level])
        self.coins_collected = 0
        self.state = 1
        self.colliding = False
        self.level_target = properties.TARGETS.get(self.level, {})

        self.walls = self.update_collisions()
        self.grottes = []
        self.static_objects = self.create_static_objects()
        # Recall game view to update associated static objects
        self.game_view = GameView(self.screen, self.map, self.player, self.static_objects, self.level)

        # Different starting positions for different maps
        if self.level == 2:
            start_position = [25, 1230]  
        elif self.level == 3:
            start_position = [371, 1558]

        self.player.reset_position(start_position)
        
    def ending_game(self):
        self.screen.fill((0, 0, 255))  

        font = pygame.font.Font(None, 74)
        text = font.render('Game Over!', True, (255, 255, 255)) 
        text_rect = text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))
        self.screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.wait(10000)

        self.end_game()
        
    def end_game(self):
        pygame.quit()
        sys.exit()

