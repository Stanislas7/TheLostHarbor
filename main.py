import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, ICON_PATH
from src.controllers.menu_controller import MenuController
from src.controllers.game_controller import GameController
from src.views.menu_view import MenuView  

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)

    # Creation of the MenuView instance
    menu_view = MenuView(screen)
    # Initialization of controllers with their views
    menu_controller = MenuController(screen, menu_view)
    game_controller = None


    current_state = "menu"
    current_level = 1
    clock = pygame.time.Clock()

    # Here the states are different from the message states, they represent the game state (playing or menu)

    while True:
        if current_state == "menu":
            current_state, selected_level = menu_controller.run()
            if current_state.startswith("playing"):
                current_level = selected_level if selected_level is not None else current_level
                game_controller = GameController(screen, current_level)

        elif current_state.startswith("playing") and game_controller:
            current_state = game_controller.run()

        elif current_state == "quit":
            break

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()