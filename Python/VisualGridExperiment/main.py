from pygame.constants import *
import classes as cs
import functions as fcs
import UI_Funcs as ui_f
import pygame, random


def runGraphFunction(a=1, x_inc=1):
    x = graphGrid.xMin

    def f(x):
        y = 2*x+5

        return [y]
        
        """ys = []
        ty = graphGrid.yMin
        while ty <= graphGrid.yMax:
            if ((x-3)**2) == 25:
                y = ty

                ys.append(y)

            ty += 1
            print(ty, ys)

        return ys"""

    while (x <= graphGrid.xMax):
        # custom code to run function
        ys = f(x)
        if len(ys) > 0:
            for y in ys:
                graphGrid.setPoint(round(x), round(y), 1)
                print(x, y)
                pygame.display.update()
        x += x_inc

def tempGraphFunction(grid):
    coordSet = [(-3, 3), (-2, 3), (3, 3), (-3, 2), (2, 2), (-3, -2), (2, -2), (-3, -3), (-2, -3), (3, -3)]

    grid.points = grid.setAllPoints(grid.points, 0)

    for coord in coordSet:
        grid.setPoint(coord[0], coord[1], 1)

res240 = [240, 240]
res210 = [210, 210]
res3 = [402, 402]
display = cs.Display(res=res3, title="Square Experiment")

# 20 + 20 + 1 = 41

# visualGrid = cs.VisualGrid(display.res, 16, (255, 0, 0))
# visualGrid.setAllChunks(100)
# graphGrid = cs.GraphGrid(0, 20, 0, 20, 10, (25, 25, 25), (255, 255, 255))
graphGrid = cs.GraphGrid(-100, 100, -100, 100, 2, (25, 25, 25), (255, 255, 255))
graphGrid.setAxis()

display.draw()
graphGrid.drawAxis(display.disp, (255, 0, 0))
# graphGrid.setPoint(0+abs(graphGrid.xMin), 0+abs(graphGrid.yMin), True)

# graphGrid.printPoints()

running = True
clock = pygame.time.Clock()
fps = 30
a = 100
runGraphFunction(3, 1)

# visualGrid.chunks = fcs.chunkFcs.wrappingGradient#(visualGrid.chunks, 100, 0, 10, decreasing=True)

# visualGrid.printChunks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                result = ui_f.userPickAction()
    
    # editing the graph
    # runGraphFunction(0.025, x_inc=1)

    # drawing of things
    display.draw()
    graphGrid.drawAxis(display.disp, (255, 0, 0))
    graphGrid.drawPoints(display.disp)

    # updating the display, wait
    display.dispUpdate()
    clock.tick(fps)
