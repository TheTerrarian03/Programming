import gui
import pygame


# main display
display = gui.Display(isResizable=True, dispX=1080, dispY=720)

# making elements
rect1 = gui.Rectangle(25, 25, 100, 100)
rect1.setupColors([255, 0, 0], [255, 255, 255])

# adding to display page
display.addElement(rect1)

# main loop
while display.running:
    display.update()
