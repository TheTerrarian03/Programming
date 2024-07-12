import pygame
import variables as v


def main():
    openPNG = pygame.image.load("mainOpen.png")

    game = pygame.display.set_mode((320, 180))
    pygame.display.set_caption("Square - Opening Menu")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= event.pos[0] <= 220 and 85 <= event.pos[1] <= 160:
                    return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        game.fill(v.colors["white"])
        game.blit(openPNG, (0, 0))

        pygame.display.update()
