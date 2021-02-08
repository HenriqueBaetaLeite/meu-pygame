import pygame
from pygame.locals import *
from sys import exit

# from create_timer import Timer

from scenario import Scenario


# classe de cenário


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def start(self):
        pygame.init()

        scenario = Scenario(self.width, self.height)

        # configuro o tamanho da tela
        # screen = pygame.display.set_mode((self.width, self.height))

        # configuro a letra
        fonte = pygame.font.SysFont("likhan", 30, bold=True, italic=False)

        # Título do game na janela
        # pygame.display.set_caption("Meu PyGame")

        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            # screen.fill((255, 255, 255))

            scenario.create_scenario()

            scenario.create_character()

            # print(clock.get_fps())

            keys = pygame.key.get_pressed()

            texto1 = fonte.render("Tela Inicial", True, (0, 0, 0))

            # Este -for- "vigia" cada evento do jogo, caso a letra q seja pressionada
            # ou clique no botão de fechar a janela o jogo encerra.
            for event in pygame.event.get():
                if event.type == QUIT or keys[pygame.K_ESCAPE]:
                    print("Bye...")
                    pygame.quit()
                    exit()

            # screen.blit(texto1, (200, 10))
            pygame.display.update()


game = Game(600, 400)
game.start()
