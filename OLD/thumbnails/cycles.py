import pygame


x = 0
y = 0

wid = 1080
hi = 720

perPixel = 1

totalCount = 0
running = True

game = pygame.display.set_mode((wid * perPixel, hi * perPixel))

mp = wid * hi
endTotal = mp * (255*255*255)
print("Total possible thumbnails given the resolution:")
print(endTotal)
print()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(game, (255, 255, 255), (x, y, perPixel, perPixel))
    pygame.display.update()
    totalCount += (255 * 255 * 255)

    x += perPixel
    if x >= wid * perPixel:
        x = 0
        y += perPixel

    if y >= hi * perPixel:
        running = False

running = True
print(totalCount)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.fill((255, 255, 255))
