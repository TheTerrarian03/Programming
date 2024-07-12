import pygame
import os
import variables as v
import calls

# get display width
defRes = 4
resInput = input("Please enter number of tiles wide for display\n"
                 "(press ENTER for default of " + str(defRes) + ")\n"
                 "$ ")
if resInput:
    res = calls.checkIntGT0(resInput, name="resInput")
else:
    res = defRes
# scaleInput = input("\n")

# Pygame (all related)
pygame.init()
v.scale = 64
v.tiles = res
calls.resizeDisplay()
v.images = [pygame.image.load(os.path.join("sprites",
                                           "x16", "grass.png")).convert()]
v.images.append(pygame.image.load(os.path.join("sprites",
                                               "x16", "water.png")).convert())
v.images.append(pygame.image.load(os.path.join("sprites",
                                               "x16", "road.png")).convert())
pygame.display.set_caption("RandomCarGame")
v.clock = pygame.time.Clock()
v.fps = 30

# Other
print("New Grid: " + str(calls.resetGrid(0)))
v.selCol = (200, 0, 0)

while v.sysRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # v.paused = True
            v.sysRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                print("KEYDOWN: K_RETURN/K_KP_ENTER")
                resp = calls.askCommand()
                if resp == 1:
                    v.sysRun = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            mouseB = event.button
            # print(mouseX, mouseY, mouseB)
            calls.changeSelection(mouseX, mouseY, mouseB)
    
    calls.drawGraphics(v.display)
    pygame.display.update()
    v.clock.tick(v.fps)
    
