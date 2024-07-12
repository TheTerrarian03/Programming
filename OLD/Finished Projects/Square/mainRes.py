import pygame
import variables as v


def main():
    resPNG = pygame.image.load("mainRes.png")

    game = pygame.display.set_mode((320, 345))
    pygame.display.set_caption("Square - Resolution")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 22 <= event.pos[0] <= 297 and 80 <= event.pos[1] <= 155:
                    return 1
                if 22 <= event.pos[0] <= 297 and 165 <= event.pos[1] <= 240:
                    return 2
                if 22 <= event.pos[0] <= 297 and 250 <= event.pos[1] <= 325:
                    return 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        game.fill(v.colors["white"])
        game.blit(resPNG, (0, 0))

        pygame.display.update()
