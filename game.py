import pygame
from pygame.locals import *
from sys import exit

# from create_timer import Timer
from scenario import Scenario

from character import Character


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def start(self):
        pygame.init()

        scenario = Scenario(self.width, self.height)

        clock = pygame.time.Clock()

        scenario.create_scenario()

        while True:
            clock.tick(30)

            scenario.create_character()

            # scenario.create_scenario()

            # print(clock.get_fps())

            keys = pygame.key.get_pressed()

            # Este -for- "vigia" cada evento do jogo, caso a letra q seja pressionada
            # ou clique no botão de fechar a janela o jogo encerra.
            for event in pygame.event.get():
                if event.type == QUIT or keys[pygame.K_ESCAPE]:
                    print("Bye...")
                    pygame.quit()
                    exit()

            pygame.display.update()


game = Game(600, 400)
game.start()
