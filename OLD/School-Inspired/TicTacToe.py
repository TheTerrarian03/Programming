import pygame

pygame.init()

game = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
fps = 30
gameGoing = True

p1 = (50, 128, 255)
bgColor = (255, 255, 255)

while gameGoing:
    """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameGoing = False"""

    # drawing
    game.fill(bgColor)

    clock.tick(fps)


pygame.quit()
quit()
