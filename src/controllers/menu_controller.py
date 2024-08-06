import pygame

class MenuController:
    def __init__(self, screen, menu_view):
        self.screen = screen
        self.menu_view = menu_view

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", None

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if self.menu_view.play_button.collidepoint(x, y):
                    return "playing", 1 
                elif self.menu_view.info_button.collidepoint(x, y):
                    return "info", None  

        self.menu_view.display_menu()
        return "menu", None  
