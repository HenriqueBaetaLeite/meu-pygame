# import pygame
import time

# fonte = pygame.font.SysFont("likhan", 30, bold=True, italic=True)

# width = 600
# height = 400

# screen = pygame.display.set_mode((width, height))


# class CrateTimer:
#     def set_timer():
#         t = 30
#         while t:
#             mins, secs = divmod(t, 60)
#             timer = "{:02d}:{:02d}".format(mins, secs)
#             print(timer, end="\r")
#             time.sleep(1)
#             t -= 1

#         print("Fire in the hole!!")


def set_timer(t):
    # t = 15
    while t:
        mins, secs = divmod(t, 60)
        # timer = f'{mins}:{secs}'
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Game Over!!")


set_timer(25)
