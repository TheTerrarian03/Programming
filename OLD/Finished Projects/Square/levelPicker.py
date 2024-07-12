import pygame
import variables as v
import thinkrs


def main():
    bg = pygame.image.load("levels.png")

    pygame.init()
    game = pygame.display.set_mode((668, 376))
    pygame.display.set_caption("Square - Level Picker")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 16 <= event.pos[0] <= 75 and 80 <= event.pos[1] <= 139:
                    return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                else:
                    return 1

        game.fill(v.colors["black"])
        game.blit(bg, (0, 0))
        pygame.display.update()
