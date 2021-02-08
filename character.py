import pygame

from random import randint


class Character:
    def __init__(self, width, height, speed, screen):
        self.width = width
        self.height = height
        self.speed = int(speed)
        self.screen = screen
        self.position_x = int(600 / 2 - width / 2)
        self.position_y = int(400 / 2 - height / 2)
        player = pygame.draw.rect(
            self.screen,
            (0, 255, 255),
            (self.position_x, self.position_y, self.width, self.height),
        )
        self.keys = pygame.key.get_pressed()

    # def create_player(self):

    def move_player(self):

        if self.keys[pygame.K_LEFT]:
            print("seta esquerda acionada")
            self.position_x -= self.speed
            if self.position_x < -40:
                self.position_x = 635

        if self.keys[pygame.K_RIGHT]:
            print("seta direita acionada")
            self.position_x += self.speed
            if self.position_x > 640:
                self.position_x = -35

        if self.keys[pygame.K_UP]:
            self.position_y -= self.speed
        if self.keys[pygame.K_DOWN]:
            self.position_y += self.speed

    def capture_prize(self, prize, prize_x, prize_y):
        if player.colliderect(prize):
            prize_x = randint(1, 599)
            prize_y = randint(1, 419)
            pontos -= 1
            totalPontosMarcados += 1
            print("Pontuação:", pontos)
            barulho_colisao.play()