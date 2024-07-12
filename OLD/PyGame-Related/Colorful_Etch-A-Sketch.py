import pygame
import tkinter.messagebox
from tkinter import *
import time


# start of variables
s = " "

win = Tk()
win.title("Colorful Etch-A-Sketch V1.0")

infoBox1 = Label(win, text="Choose a horizontal resolution:")
infoBox2 = Label(win, text="Choose a vertical resolution:")
infoBox3 = Label(win, text="A 480 x 270 minimum resolution is recommended.")
ent1 = Entry(win)
ent2 = Entry(win)

global winWidth
global winHeight


def runGame(full):

    if not full:
        winWidth = int(ent1.get())
        winHeight = int(ent2.get())
    else:
        winWidth = None
        winHeight = None

    tkinter.messagebox.showinfo("Some useful info:", "Here are some useful controls:\n"
                                                     "Use the arrow keys to move,\n"
                                                     "Use keypad 4 to move up the color order,\n"
                                                     "Use keypad 1 to move down the color order,\n"
                                                     "Your \"speed\" is how far you go with each button press.\n"
                                                     "Use keypad 5 to increase your speed,\n"
                                                     "Use keypad 2 to decrease your speed.\n"
                                                     "Use space to toggle whether you are drawing or not.\n"
                                                     "Pressing delete will reset what you've drawn,\n"
                                                     "but not where you are or what color you're on.\n"
                                                     "Keypad 0 acts like an undo. There is no redo.\n"
                                                     "If you are Fullscreen and want to exit,\n"
                                                     "Just press escape to quit the game.\n"
                                                     "Unfortunately, there is no real \"save\" feature yet :(\n"
                                                     "HAVE FUN!!!!!!")

    win.destroy()

    print(winWidth)
    print(winHeight)

    if not full:
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
    else:
        midX = 400
        midY = 300

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
        999: "None",
        "purple": (128, 0, 128),
        "blueLight": (0, 153, 255),
    }

    mainColor = colors[1]
    bgColor = colors[2]
    colorOn = 1
    oldColor = None

    coordsList = [midX, midY, 1]  # x, y, colors[number]
    coordsListLen = len(coordsList)

    speed = 1
    maxSpeed = 15
    # end of variables

    if not full:
        game = pygame.display.set_mode((winWidth, winHeight))
    else:
        game = pygame.display.set_mode()
    pygame.display.set_caption("Colorful, Pixelated Etch-A-Sketch, by Logan Meyers")

    while True:  # game loop
        for event in pygame.event.get():  # event-handling loop
            if event.type == pygame.QUIT:
                pygame.quit()
                exitWin = Tk()
                exitWin.title("QUIT")
                infobox4 = Label(exitWin, text="Exiting...\nThanks for playing!\n\n"
                                               "Close the window to completely exit.")
                infobox4.pack()
                mainloop()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for _ in range(speed):
                        coordsList.append(coordsList[-3] - 20)
                        coordsList.append(coordsList[-3])
                        coordsList.append(mainColor)
                if event.key == pygame.K_RIGHT:
                    for _ in range(speed):
                        coordsList.append(coordsList[-3] + 20)
                        coordsList.append(coordsList[-3])
                        coordsList.append(mainColor)
                if event.key == pygame.K_UP:
                    for _ in range(speed):
                        coordsList.append(coordsList[-3])
                        coordsList.append(coordsList[-3] - 20)
                        coordsList.append(mainColor)
                if event.key == pygame.K_DOWN:
                    for _ in range(speed):
                        coordsList.append(coordsList[-3])
                        coordsList.append(coordsList[-3] + 20)
                        coordsList.append(mainColor)
                if event.key == pygame.K_SPACE:
                    if colorOn != 999:
                        oldColor = colorOn
                        colorOn = 999
                    else:
                        colorOn = oldColor
                if event.key == pygame.K_KP_1:
                    colorOn += 1
                if event.key == pygame.K_KP_4:
                    colorOn -= 1
                if event.key == pygame.K_DELETE:
                    coordsList = [coordsList[-3], coordsList[-2], coordsList[-1]]
                    coordsListLen = len(coordsList)
                if event.key == pygame.K_KP_PLUS:
                    if speed != maxSpeed:
                        speed += 1
                if event.key == pygame.K_KP_MINUS:
                    if speed != 0:
                        speed -= 1
                if event.key == pygame.K_KP_ENTER:
                    if speed < maxSpeed / 2:
                        speed = maxSpeed
                    elif speed > maxSpeed / 2:
                        speed = 1
                if event.key == pygame.K_KP_0:
                    if coordsListLen > 3:
                        for _ in range(3):
                            coordsList.pop(-1)
                if event.key == pygame.K_ESCAPE and full:
                    pygame.quit()
                    tkinter.messagebox.showinfo("QUIT", "Exiting...\nThanks for playing!")
                    quit()

        wn1 = 0
        wn2 = 3
        while True:
            if wn1 == coordsListLen - 3:
                break
            while True:
                try:
                    if coordsList[wn1] == coordsList[wn2] and coordsList[wn1 + 1] == coordsList[wn2 + 1]:
                        for _ in range(3):
                            coordsList.pop(wn1)
                    else:
                        wn2 += 3
                        if wn2 > coordsListLen:
                            break
                except IndexError:
                    break
            wn1 += 3

        coordsListLen = len(coordsList)

        try:
            mainColor = colors[colorOn]
        except KeyError:
            colorOn += 1

        if colorOn < 1:
            colorOn = 1
        elif colorOn > len(colors) - 3 and colorOn != 999:
            colorOn = len(colors) - 3

        # start of board drawing
        game.fill(bgColor)
        num = 0
        while num <= coordsListLen:
            try:
                if coordsList[num + 2] == "None":
                    num += 3
                elif num == coordsListLen - 3:
                    pygame.draw.rect(game, colors["purple"], [coordsList[num + 0], coordsList[num + 1], 20, 20])
                    pygame.draw.rect(game, coordsList[num + 2],
                                     [coordsList[num + 0] + 5, coordsList[num + 1] + 5, 10, 10])
                    num += 3
                else:
                    pygame.draw.rect(game, coordsList[num + 2], [coordsList[num + 0], coordsList[num + 1], 20, 20])
                    num += 3
            except IndexError:
                break

        for num3 in range(len(colors)):
            try:
                pygame.draw.rect(game, colors[num3 + 1], [0, num3 * 30, 30, 30])
            except KeyError:
                break

        pygame.draw.rect(game, colors[1], [35, ((colorOn - 1) * 30), 10, 30])

        # preview overlay for the speed feature
        pygame.draw.rect(game, colors["purple"], [coordsList[-3] + (speed * 20) + 5, coordsList[-2] + 5, 10, 10])
        pygame.draw.rect(game, colors["purple"], [coordsList[-3] - (speed * 20) + 5, coordsList[-2] + 5, 10, 10])
        pygame.draw.rect(game, colors["purple"], [coordsList[-3] + 5, coordsList[-2] + (speed * 20) + 5, 10, 10])
        pygame.draw.rect(game, colors["purple"], [coordsList[-3] + 5, coordsList[-2] - (speed * 20) + 5, 10, 10])
        # end of board drawing

        pygame.display.update()  # update window


def runNF():
    runGame(False)


def runF():
    runGame(True)


infoBox1.grid(row=0, column=0)
infoBox2.grid(row=1, column=0)
infoBox3.grid(row=2, column=0, columnspan=2)
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
ent1.insert(0, "1600")
ent2.insert(0, "900")
goButt = Button(win, text="GO!", command=runNF)
goButt.grid(row=3, column=0, columnspan=2)
fullButt = Button(win, text="Full screen instead!", command=runF)
fullButt.grid(row=4, column=0, columnspan=2)


win.mainloop()
