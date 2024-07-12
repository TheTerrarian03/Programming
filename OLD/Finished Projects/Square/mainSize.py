import pygame
import variables as v


def main():
    sizePNG = pygame.image.load("mainSize.png")

    game = pygame.display.set_mode((320, 180))
    pygame.display.set_caption("Square - Block Size")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 45 <= event.pos[0] <= 100 and 80 <= event.pos[1] <= 155:
                    return 1
                if 120 <= event.pos[0] <= 195 and 80 <= event.pos[1] <= 155:
                    return 2
                if 205 <= event.pos[0] <= 280 and 80 <= event.pos[1] <= 155:
                    return 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        game.fill(v.colors["white"])
        game.blit(sizePNG, (0, 0))

        pygame.display.update()
