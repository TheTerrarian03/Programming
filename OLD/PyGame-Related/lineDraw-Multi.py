import pygame
import tkinter.messagebox


# start of variables
s = " "

winWidth = 800
winHeight = 400

midX = 0
midY = 0

while True:
    if midX < winWidth / 2:
        midX += 20
    else:
        break

while True:
    if midY < winHeight / 2:
        midY += 20
    else:
        break

# debugging midX/Y print statements
print(midX)
print(midY)
# end of debugging midX/Y print statements

colors = {
    1: (0, 0, 0),
    2: (255, 255, 255),
    3: (255, 0, 0),
    4: (0, 150, 0),
    5: (0, 0, 255),
    6: (255, 165, 0),
    7: (255, 255, 0),
    8: (255, 192, 203),
    9: (0, 255, 0),
    "purple": (128, 0, 128),
    "blueLight": (0, 153, 255),
}

mainColor = colors[1]
mainColor2 = colors[1]
bgColor = colors[2]
colorOn = 1
colorOn2 = 1

coordsList = [midX - 100, midY, 1]  # x, y, colors[number]
coordsListLen = len(coordsList)
coordsList2 = [midX + 100, midY, 1]
coordsList2Len = len(coordsList2)

gameExit = False
exitLoop = False
tMTV = 0
speed = 1
speed2 = 1
maxSpeed = 10
# end of variables

game = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Draw for Nova")

while not gameExit:  # game loop
    for event in pygame.event.get():  # event-handling loop
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for _ in range(speed):
                    coordsList.append(coordsList[-3] - 20)
                    coordsList.append(coordsList[-3])
                    coordsList.append(mainColor)
            if event.key == pygame.K_d:
                for _ in range(speed):
                    coordsList.append(coordsList[-3] + 20)
                    coordsList.append(coordsList[-3])
                    coordsList.append(mainColor)
            if event.key == pygame.K_w:
                for _ in range(speed):
                    coordsList.append(coordsList[-3])
                    coordsList.append(coordsList[-3] - 20)
                    coordsList.append(mainColor)
            if event.key == pygame.K_s:
                for _ in range(speed):
                    coordsList.append(coordsList[-3])
                    coordsList.append(coordsList[-3] + 20)
                    coordsList.append(mainColor)
            if event.key == pygame.K_f:
                if colorOn < len(colors) - 2:
                    colorOn += 1
            if event.key == pygame.K_r:
                if colorOn > 0:
                    colorOn -= 1
            if event.key == pygame.K_SPACE:
                coordsList = [coordsList[-3], coordsList[-2], coordsList[-1]]
                coordsListLen = len(coordsList)
            if event.key == pygame.K_t:
                if speed != maxSpeed:
                    speed += 1
            if event.key == pygame.K_g:
                if speed != 0:
                    speed -= 1
            if event.key == pygame.K_b:
                if speed < maxSpeed / 2:
                    speed = maxSpeed
                elif speed > maxSpeed / 2:
                    speed = 1
            if event.key == pygame.K_v:
                if coordsListLen > 3:
                    for _ in range(3):
                        coordsList.pop(-1)
            if event.key == pygame.K_LEFT:
                if event.key == pygame.K_LEFT:
                    for _ in range(speed):
                        coordsList2.append(coordsList2[-3] - 20)
                        coordsList2.append(coordsList2[-3])
                        coordsList2.append(mainColor2)
                if event.key == pygame.K_RIGHT:
                    for _ in range(speed):
                        coordsList2.append(coordsList2[-3] + 20)
                        coordsList2.append(coordsList2[-3])
                        coordsList2.append(mainColor2)
                if event.key == pygame.K_UP:
                    for _ in range(speed):
                        coordsList2.append(coordsList2[-3])
                        coordsList2.append(coordsList2[-3] - 20)
                        coordsList2.append(mainColor2)
                if event.key == pygame.K_DOWN:
                    for _ in range(speed):
                        coordsList2.append(coordsList2[-3])
                        coordsList2.append(coordsList2[-3] + 20)
                        coordsList2.append(mainColor2)

    coordsListLen = len(coordsList)
    coordsList2Len - len(coordsList2)

    try:
        mainColor = colors[colorOn]
    except KeyError:
        colorOn += 1

    try:
        mainColor2 = colors[colorOn2]
    except KeyError:
        colorOn2 += 1

    # start of board drawing
    game.fill(bgColor)
    num = 0
    num2 = 0
    while num <= coordsListLen:
        try:
            if num == coordsListLen - 3:
                pygame.draw.rect(game, colors["purple"], [coordsList[num], coordsList[num + 1], 20, 20])
                pygame.draw.rect(game, coordsList[num + 2], [coordsList[num] + 5, coordsList[num + 1] + 5, 10, 10])
                num += 3
            else:
                pygame.draw.rect(game, coordsList[num + 2], [coordsList[num], coordsList[num + 1], 20, 20])
                num += 3
        except IndexError:
            break

    while num2 <= coordsList2Len:
        try:
            if num2 == coordsList2Len - 3:
                pygame.draw.rect(game, colors["blueLight"], [coordsList2[num2], coordsList2[num2 + 1], 20, 20])
                pygame.draw.rect(game, coordsList2[num2 + 2], [coordsList2[num2] + 5, coordsList2[num2 + 1] + 5, 10,
                                                               10])
                num2 += 3
            else:
                pygame.draw.rect(game, coordsList2[num2 + 2], [coordsList2[num2], coordsList2[num2 + 1], 20, 20])
                num += 3
        except IndexError:
            break

    for num3 in range(len(colors)):
        try:
            pygame.draw.rect(game, colors[num3 + 1], [0, num3 * 30, 30, 30])
        except KeyError:
            break

    for num4 in range(len(colors)):
        try:
            pygame.draw.rect(game, colors[num4 + 1], [winWidth - 30, num4 * 30, 30, 30])
        except KeyError:
            break

    pygame.draw.rect(game, colors[1], [35, ((colorOn - 1) * 30), 10, 30])
    pygame.draw.rect(game, colors[1], [winWidth - 45, ((colorOn2 - 1) * 30), 10, 10])

    # preview overlay for the speed feature
    pygame.draw.rect(game, colors["purple"], [coordsList[-3] + (speed * 20) + 5, coordsList[-2] + 5, 10, 10])
    pygame.draw.rect(game, colors["purple"], [coordsList[-3] - (speed * 20) + 5, coordsList[-2] + 5, 10, 10])
    pygame.draw.rect(game, colors["purple"], [coordsList[-3] + 5, coordsList[-2] + (speed * 20) + 5, 10, 10])
    pygame.draw.rect(game, colors["purple"], [coordsList[-3] + 5, coordsList[-2] - (speed * 20) + 5, 10, 10])

    pygame.draw.rect(game, colors["blueLight"], [coordsList2[-3] + (speed2 * 20) + 5, coordsList2[-2] + 5, 10, 10])
    pygame.draw.rect(game, colors["blueLight"], [coordsList2[-3] - (speed2 * 20) + 5, coordsList2[-2] + 5, 10, 10])
    pygame.draw.rect(game, colors["blueLight"], [coordsList2[-3] + 5, coordsList2[-2] + (speed2 * 20) + 5, 10, 10])
    pygame.draw.rect(game, colors["blueLight"], [coordsList2[-3] + 5, coordsList2[-2] - (speed2 * 20) + 5, 10, 10])
    # end of board drawing

    pygame.display.update()  # update window

pygame.quit()  # un-initialize it
quit()  # exits out of python
