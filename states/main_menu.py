import pygame
from state import State


class MainMenu(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.main_menu_surface = pygame.Surface((game.GAME_W, game.GAME_H))

    def update(self, actions):
        pass

    def render(self, surface):
        pass