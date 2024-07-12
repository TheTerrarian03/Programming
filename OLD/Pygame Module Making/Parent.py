import PixelFont
import pygame


def parent():
    disp = pygame.display.set_mode((1000, 900))

    pygame.display.set_caption("Parent - PixelFont Testing")
    disp.fill((255, 255, 255))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                PixelFont.drawChars("0123456789.ABCDEFGH", disp, charSize=1)
                """sheet = pygame.image.load("Chars_7x5_Original.png")
                disp.blit(sheet, (0, 0), (0, 0, 5, 7))
                r = sheet.get_rect()
                xScaled = r[2] * 2
                yScaled = r[3] * 2
                sheetScaled = pygame.transform.scale(sheet, (xScaled, yScaled))
                disp.blit(sheetScaled, (0, 10), (0, 0, 10, 14))
                xScaled = r[2] * 5
                yScaled = r[3] * 5
                sheetScaled = pygame.transform.scale(sheet, (xScaled, yScaled))
                disp.blit(sheetScaled, (0, 40), (0, 0, 25, 35))
                pygame.display.update()"""


parent()
