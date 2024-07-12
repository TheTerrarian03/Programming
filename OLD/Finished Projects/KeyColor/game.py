import pygame
import v


def main(resX=None, resY=None, fs=False):
    print(resX)
    print(resY)
    print(fs)

    if fs:
        game = pygame.display.set_mode()
    else:
        game = pygame.display.set_mode((int(resX), int(resY)))
    pygame.display.set_caption(v.name)

    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    v.up_down = True
                if event.key == pygame.K_DOWN:
                    v.down_down = True
                if event.key == pygame.K_LEFT:
                    v.left_down = True
                if event.key == pygame.K_RIGHT:
                    v.right_down = True
            if event.type == pygame.K_UP:
                if event.key == pygame.K_UP:
                    v.up_down = False
                if event.key == pygame.K_DOWN:
                    v.down_down = False
                if event.key == pygame.K_LEFT:
                    v.left_down = False
                if event.key == pygame.K_RIGHT:
                    v.right_down = False
        
        # drawing
        game.fill(v.colors["white"])
        game.blit(v.colorsIMG, (0, 0))

        pygame.display.update()
