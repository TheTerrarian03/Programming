import pygame
import messages


def main():
    pygame.init()
    menu = pygame.display.set_mode((590, 368))
    pygame.display.set_caption("UnitConverter - Menu")

    menuIMG = pygame.image.load("menu.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "EXIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 18 <= event.pos[0] <= 287 and 123 <= event.pos[1] <= 156:
                    return 1
                if 303 <= event.pos[0] <= 572 and 123 <= event.pos[1] <= 156:
                    return 2
                if 18 <= event.pos[0] <= 287 and 172 <= event.pos[1] <= 205:
                    return 3
                if 303 <= event.pos[0] <= 532 and 172 <= event.pos[1] <= 205:
                    return 4
                if 543 <= event.pos[0] <= 572 and 172 <= event.pos[1] <= 205:
                    messages.lcmQMark()
                if 18 <= event.pos[0] <= 287 and 221 <= event.pos[1] <= 254:
                    return 5
                if 303 <= event.pos[0] <= 572 and 221 <= event.pos[1] <= 254:
                    return 6
                if 18 <= event.pos[0] <= 287 and 270 <= event.pos[1] <= 303:
                    return 7
                if 270 <= event.pos[1] <= 303 <= event.pos[0] <= 572:
                    return 8
                if 18 <= event.pos[0] >= 287 and 319 >= event.pos[1] >= 352:
                    return 9
                if 303 <= event.pos[0] >= 572 and 319 >= event.pos[1] >= 352:
                    return 10

        menu.fill((255, 255, 255))
        menu.blit(menuIMG, (0, 0))

        pygame.display.update()
