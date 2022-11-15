import os
import pygame

from states.main_menu import MainMenu


class Game:
    def __init__(self):
        pygame.init()

        self.GAME_W, self.GAME_H = 1920, 1080
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN, 8
        )

        self.SCREEN_W, self.SCREEN_H = pygame.display.get_surface().get_size()

        self.actions = {
            "event_1": False,
            "event_2": False,
            "event_3": False,
        }

        self.state_stack = []

        self.load_assets()
        self.load_states()

        self.running, self.playing = True, True

    def game_loop(self):
        while self.playing:
            self.get_events()
            self.update()
            self.render()

    def update(self):
        self.state_stack[-1].update(self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(
            pygame.transform.scale(self.game_canvas, (self.SCREEN_W, self.SCREEN_H)),
            (0, 0),
        )

        pygame.display.flip()

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.big_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 100)
        self.medium_font = pygame.font.Font(
            os.path.join(self.font_dir, "Inter.ttf"), 64
        )
        self.small_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 48)

    def load_states(self):
        self.main_menu = MainMenu(self)
        self.state_stack.append(self.main_menu)

    def reset_actions(self):
        for action in self.actions:
            self.actions[action] = False

    def draw_text(self, surface, position, text, size, color):
        match size:
            case "BIG":
                text_surface = self.big_font.render(text, True, color)
            case "MEDIUM":
                text_surface = self.medium_font.render(text, True, color)
            case "SMALL":
                text_surface = self.small_font.render(text, True, color)

        text_rect = text_surface.get_rect()
        text_rect.center = position
        surface.blit(text_surface, text_rect)


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
