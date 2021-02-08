import pygame

from character import Character


class Scenario:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.screen = pygame.display.set_mode((self.width, self.heigth))
        pygame.display.set_caption("Pygame - Catch me if you can")

    def create_scenario(self):
        black = (0, 0, 0)
        self.screen.fill(black)

    def create_character(self):
        player = Character(40, 60, 10, self.screen)
        # player.create_player()
        player.move_player()
