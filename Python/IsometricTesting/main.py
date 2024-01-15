import pygame
import classes as cs


dispSize = [660, 375]
display = pygame.display.set_mode(dispSize)
pygame.display.set_caption("Isometric Testing - LM")

clock = pygame.time.Clock()
fps = 30

tiles = []
for x in range(10):
    for y in range(10):
        tiles.append(cs.Tile("Models/BaseBlock.png", (64, 64), [x, y]))
extra = cs.Tile("Models/Green.png", (64, 64), (x, y))

for tile in tiles:
    tile.setGlobalOffset(298, 10)

extra.setGlobalOffset(298, -22)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keysPressed = pygame.key.get_pressed()
    extra.changeGridPos(1 if keysPressed[pygame.K_RIGHT] == True else -1 if keysPressed[pygame.K_LEFT] == True else 0, 1 if keysPressed[pygame.K_DOWN] == True else -1 if keysPressed[pygame.K_UP] == True else 0)

    mousePos = pygame.mouse.get_pos()
    
    pygame.draw.rect(display, (175, 175, 225), (0, 0, dispSize[0], dispSize[1]))

    for tile in tiles:
        tile.draw(display)
    extra.draw(display)

    pygame.display.flip()
    clock.tick(fps)

"""
(x * 0.5 * w)  + (y * -0.5 * w)
(x * 0.25 * h) + (y * 0.25 * h)
"""