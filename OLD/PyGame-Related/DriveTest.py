import pygame
import time
from tkinter import *

white = (255, 255, 255)
grey = (150, 150, 150)
black = (0, 0, 0)
red = (255, 0, 0)
darkRed = (150, 0, 0)
orange = (220, 150, 0)
brown = (150, 75, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
darkGreen = (0, 175, 0)
darkDarkGreen = (0, 95, 0)
lightBlue = (50, 100, 255)
blue = (25, 25, 255)
pink = (255, 25, 255)
purple = (150, 25, 150)


class Info:
    def changeColors(self, bgC, mC, pC):
        self.BgColor = bgC.lower()
        self.MainColor = mC.lower()
        self.Pointer = pC.lower()

    def changeSize(self, num):
        self.WidHi = num

    def changeResXY(self, width, height):
        self.dispWid = width
        self.dispHi = height

    def changeResString(self, res):
        i = 0

        while True:
            if res[i] == "x":
                firstLen = i
                print("i = " + str(i))
                break
            else:
                i += 1

        secondLen = len(res) - firstLen - 1

        self.dispWid = int(res[:firstLen])
        self.dispHi = int(res[secondLen + 1:])

    def resetPosition(self):
        self.X = self.DefX
        self.Y = self.DefY

    def resetAll(self):
        self.resetPosition()
        self.Dir = 0
        self.Speed = 0

    dispWid = 0
    dispHi = 0

    DefX = dispWid / 2
    DefY = dispHi / 2
    X = dispWid / 2
    Y = dispHi / 2
    WidHi = 20
    Dir = 0
    Speed = 0
    TopSpeed = 50
    FAcc = 1  # forward acceleration value
    BAcc = 1  # backwards acceleration value
    BreakingVal = 5  # breaking value

    Pointer = red
    BgColor = white
    MainColor = black

    Breaking = False
    UpDown = False
    DownDown = False
    LeftDown = False
    RightDown = False


me = Info


def runTkinter():
    window = Tk()
    window.title("Starter Screen")

    infoBox1 = Label(window, text="This is the main window, where you can set the resolution,\n"
                                  "background color, main color, and pointer color of your \"car\"\n"
                                  "as well as your top speed and size. Your \"car\" is really just\n"
                                  "a square.")
    infoBox2 = Label(window, text="Type a resolution (WIDTHxHEIGHT):")
    resBox = Entry(window)
    infoBox3 = Label(window, text="Your color options are: \"white\", \"grey\", \"black\", \"red\", \"darkRed\", "
                                  "\"orange\"\n"
                                  ", \"brown\", \"yellow\", \"green\", \"darkGreen\", \"darkDarkGreen\", \"lightBlue\""
                                  "\n"
                                  ", \"blue\", \"pink\", and \"purple\".")
    infoBox4 = Label(window, text="Pick a background color:")
    bgBox = Entry(window)
    infoBox5 = Label(window, text="Pick a main color:")
    mainBox = Entry(window)
    infoBox6 = Label(window, text="Pick a pointer color:")
    pointerBox = Entry(window)
    infoBox7 = Label(window, text="Square size in pixels:")
    widHiBox = Entry(window)

    def go():
        me.changeResString(resBox.get())
        me.changeColors(bgBox.get(), mainBox.get(), pointerBox.get())
        me.changeSize(widHiBox.get())

        window.quit()

    goButt = Button(window, text="     GO!    ", command=go)
    infoBox8 = Label(window, text="Have Fun!!!")

    infoBox1.grid(row=0, column=0, columnspan=2)
    infoBox2.grid(row=1, column=0)
    resBox.grid(row=1, column=1)
    infoBox3.grid(row=2, column=0, columnspan=2)
    infoBox4.grid(row=3, column=0)
    bgBox.grid(row=3, column=1)
    infoBox5.grid(row=4, column=0)
    mainBox.grid(row=4, column=1)
    infoBox6.grid(row=5, column=0)
    pointerBox.grid(row=5, column=1)
    infoBox7.grid(row=6, column=0)
    widHiBox.grid(row=6, column=1)
    goButt.grid(row=7, column=0, columnspan=2)
    infoBox8.grid(row=8, column=0, columnspan=2)

    window.mainloop()


runTkinter()

print(me.WidHi)
print(me.X)
print(me.Y)
print(me.dispWid)
print(me.dispHi)
print(me.BgColor)
print(me.MainColor)
print(me.Pointer)

pygame.init()

game = pygame.display.set_mode((dispWid, dispHi))
pygame.display.set_caption("DriveTest")

gameRunning = True

count = 15
countGoing = False

fps = 30
clock = pygame.time.Clock()

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                upDown = True
            if event.key == pygame.K_DOWN:
                downDown = True
            if event.key == pygame.K_LEFT:
                countGoing = True
                leftDown = True
            if event.key == pygame.K_RIGHT:
                countGoing = True
                rightDown = True
                breaking = True
            if event.key == pygame.K_ESCAPE:
                gameRunning = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                upDown = False
            if event.key == pygame.K_DOWN:
                downDown = False
            if event.key == pygame.K_LEFT:
                leftDown = False
                countGoing = False
            if event.key == pygame.K_RIGHT:
                rightDown = False
                countGoing = False
            if event.key == pygame.K_SPACE:
                breaking = False
        if event.type == pygame.QUIT:
            gameRunning = False

    if countGoing:
        count += 1
    elif not countGoing:
        count = 15

    if upDown:
        meSpeed += meFAcc
        if meSpeed > meTopSpeed:
            meSpeed = meTopSpeed
    if downDown:
        meSpeed -= meFAcc / 2
        if meSpeed < -(meTopSpeed / 2):
            meSpeed = -(meTopSpeed / 2)
    if breaking:
        if meSpeed <= meBreakingVal and meSpeed >= -meBreakingVal:
            meSpeed = 0
            breaking = False
        if meSpeed > 0:
            meSpeed -= meBreakingVal
        elif meSpeed < 0:
            meSpeed += meBreakingVal
    if leftDown and (count == 0 or count % 10 == 0):
        meDir += 315
    if rightDown and (count == 0 or count % 10 == 0):
        meDir += 45

    if meDir >= 360:
        meDir -= 360

    if meDir == 0:
        meY -= meSpeed
    elif meDir == 45:
        meX += meSpeed / 2
        meY -= meSpeed / 2
    elif meDir == 90:
        meX += meSpeed
    elif meDir == 135:
        meX += meSpeed / 2
        meY += meSpeed / 2
    elif meDir == 180:
        meY += meSpeed
    elif meDir == 225:
        meX -= meSpeed / 2
        meY += meSpeed / 2
    elif meDir == 270:
        meX -= meSpeed
    elif meDir == 315:
        meX -= meSpeed / 2
        meY -= meSpeed / 2

    if (meX > dispWid - meWidth or meX < 0) or (meY > dispHi - meHeight or meY < 0):
        meX = dispWid / 2
        meY = dispHi / 2

    game.fill(bgColor)

    pygame.draw.rect(game, black, [meX, meY, meWidth, meHeight])

    if meDir == 0:
        pygame.draw.rect(game, mePointer, [meX, meY, meWidth, meHeight / 2])
    elif meDir == 45:
        pygame.draw.rect(game, mePointer, [meX, meY, meWidth, meHeight / 2])
        pygame.draw.rect(game, mePointer, [meX + meWidth - meHeight / 2, meY, meWidth / 2, meHeight])
    elif meDir == 90:
        pygame.draw.rect(game, me.Pointer, [meX + meWidth - meHeight / 2, meY, meWidth / 2, meHeight])
    elif meDir == 135:
        pygame.draw.rect(game, mePointer, [meX + meWidth - meHeight / 2, meY, meWidth / 2, meHeight])
        pygame.draw.rect(game, mePointer, [meX, meY + meHeight / 2, meWidth, meHeight / 2])
    elif meDir == 180:
        pygame.draw.rect(game, mePointer, [meX, meY + meHeight / 2, meWidth, meHeight / 2])
    elif meDir == 225:
        pygame.draw.rect(game, mePointer, [meX, meY + meHeight / 2, meWidth, meHeight / 2])
        pygame.draw.rect(game, mePointer, [meX, meY, meWidth / 2, meHeight])
    elif meDir == 270:
        pygame.draw.rect(game, mePointer, [meX, meY, meWidth / 2, meHeight])
    elif meDir == 315:
        pygame.draw.rect(game, mePointer, [meX, meY, meWidth / 2, meHeight])
        pygame.draw.rect(game, mePointer, [meX, meY, meWidth, meHeight / 2])

    pygame.display.update()

    clock.tick(fps)


print("Exiting...")
pygame.quit()
quit()
