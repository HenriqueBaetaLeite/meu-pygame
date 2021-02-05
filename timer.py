import pygame

fonte = pygame.font.SysFont("", 20)


class Timer:
    def start_timer():
        timer_formated = fonte.render("Tempo: 00:30", True, (0, 0, 0))
        screen.blit(timer_formated, (10, 10))
