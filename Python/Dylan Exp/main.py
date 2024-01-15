import pygame, random
import classes as cs


disp = pygame.display.set_mode((500, 500))
running = True

planet = cs.Shape((0, 126, 255), (249, 249), 100)
player = cs.Shape((225, 225, 225), (100, 100), 25)

redColors = [(255, 0, 0), (240, 0, 0), (225, 0, 0), (210, 0, 0), (195, 0, 0), (170, 0, 0)]
blueColors = [(0, 255, 0), (0, 240, 0), (0, 225, 0), (0, 210, 0), (0, 195, 0), (0, 170, 0)]
greenColors = [(0, 0, 255), (0, 0, 240), (0, 0, 225), (0, 0, 210), (0, 0, 195), (0, 0, 170)]

planet.makeCollisionCircleBorder(redColors)  # one-time event

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    xChange, yChange = 0, 0
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_LEFT]:
        xChange -= 1
    if keysPressed[pygame.K_RIGHT]:
        xChange += 1
    if keysPressed[pygame.K_UP]:
        yChange -= 1
    if keysPressed[pygame.K_DOWN]:
        yChange += 1
    
    if (xChange != 0) or (yChange != 0):
        player.changeCenterPosition(xChange, yChange)
        player.makeCollisionCircleBorder(blueColors)  # constant event

    pygame.draw.rect(disp, (25, 25, 25), (0, 0, 500, 500))

    # planet
    planet.draw(disp)
    planet.drawCollisionPoints(disp)

    # player
    colliding = False
    if set(player.getCoordList()).intersection(planet.getCoordList()):
        colliding = True

    if colliding:
        player.color = (225, 0, 0)
    if not colliding:
        player.color = (225, 225, 225)

    player.draw(disp)
    player.drawCollisionPoints(disp)

    pygame.display.flip()