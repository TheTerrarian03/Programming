from pygame import time as pT
import presetColors as pC

drawTopBar = True
topBarColor = [50, 150, 255]
bgColor = [50, 250, 50]
running = True
winDims = [800, 600]

mainClock = pT.Clock()
mainFPS = 60
display = None

testWindow = False
tWBgColor = pC.colors["yellow"]
tWBarColor = pC.colors["fullPink"]
tWBarDims = [640, 480]
tWPos = [22, 22]

"""
tempStartPos = [0, 0]
tempMouseStartPos = [0, 0]
"""
