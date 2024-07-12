import pygame


pygame.init()

game = pygame.display.set_mode((500, 350))
pygame.display.set_caption("Window")
clock = pygame.time.Clock()
fps = 1000


running = True
x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    colorsImg = pygame.image.load("Colors.png")
    r = colorsImg.get_rect()
    game.fill((255, 255, 255))
    game.blit(colorsImg, [x, 100])  # image loaded as a variable, [x, y], (area of image (as 4 values))

    colorsImgRotated = pygame.transform.rotate(colorsImg, 90)  # image loaded as variable, degrees
    game.blit(colorsImgRotated, [x, 200])

    colorsImgScaled = pygame.transform.scale(colorsImg, (160, 160))  # image, (pixel width, pixel height)
    game.blit(colorsImgScaled, [x, 250])

    pygame.display.update()

    x += 1
    if x == 500:
        x = 0

    clock.tick(fps)


pygame.quit()
quit()
