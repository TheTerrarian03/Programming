import pygame


# variables
hsVar = 1
fps = 15
clock = pygame.time.Clock()
paused = False
growing = True

# pygame display
disp = pygame.display.set_mode((256, 256))
bgColor = (243, 193, 219)

# pygame image loading
heart1 = pygame.image.load("heart1.png")
heart2 = pygame.image.load("heart2.png")
heart3 = pygame.image.load("heart3.png")
heart4 = pygame.image.load("heart4.png")
heart5 = pygame.image.load("heart5.png")
heart6 = pygame.image.load("heart6.png")
heart7 = pygame.image.load("heart7.png")
heart8 = pygame.image.load("heart8.png")
heart9 = pygame.image.load("heart9.png")

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if paused:
                paused = False
            elif not paused:
                paused = True

    # clear screen
    disp.fill(bgColor)

    # heart loop, runs if 'not paused'
    if not paused:
        # heart loading and 'blit'ting
        if hsVar == 1:
            disp.blit(heart1, (0, 0), (0, 0, 256, 256))
        elif hsVar == 2:
            disp.blit(heart2, (0, 0), (0, 0, 256, 256))
        elif hsVar == 3:
            disp.blit(heart3, (0, 0), (0, 0, 256, 256))
        elif hsVar == 4:
            disp.blit(heart4, (0, 0), (0, 0, 256, 256))
        elif hsVar == 5:
            disp.blit(heart5, (0, 0), (0, 0, 256, 256))
        elif hsVar == 6:
            disp.blit(heart6, (0, 0), (0, 0, 256, 256))
        elif hsVar == 7:
            disp.blit(heart7, (0, 0), (0, 0, 256, 256))
        elif hsVar == 8:
            disp.blit(heart8, (0, 0), (0, 0, 256, 256))
        elif hsVar == 9:
            disp.blit(heart9, (0, 0), (0, 0, 256, 256))

        # growing if statements
        if growing:
            hsVar += 1
        elif not growing:
            hsVar -= 1

        # growing handling
        if hsVar == 9:
            growing = False
        elif hsVar == 1:
            growing = True

    pygame.display.update()

    clock.tick(fps)
