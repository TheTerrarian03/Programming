import anki_vector, time, pygame
import classes as cs
from PIL import Image


gui = cs.GUI("Anki Vector Dashboard - LM", res=[800, 600])

keys = {
    "Forward":   cs.keyboardKey(pygame.K_w, (50,  gui.res[1]-100), (50, 50), additionalValue=100),
    "Left":      cs.keyboardKey(pygame.K_a, (0,   gui.res[1]-50),  (50, 50), additionalValue=100),
    "Backward":  cs.keyboardKey(pygame.K_s, (50,  gui.res[1]-50),  (50, 50), additionalValue=100),
    "Right":     cs.keyboardKey(pygame.K_d, (100, gui.res[1]-50),  (50, 50), additionalValue=100),

    "Lift Up":   cs.keyboardKey(pygame.K_r, (150, gui.res[1]-100), (50, 50), additionalValue=2),
    "Lift Down": cs.keyboardKey(pygame.K_f, (150, gui.res[1]-50),  (50, 50), additionalValue=2),

    "Head Up":   cs.keyboardKey(pygame.K_t, (200, gui.res[1]-100), (50, 50), additionalValue=2),
    "Head Down": cs.keyboardKey(pygame.K_g, (200, gui.res[1]-50),  (50, 50), additionalValue=2),
}

running = True

while running:
    ### keys
    for event in pygame.event.get():
        # quit window
        if event.type == pygame.QUIT:
            running = False
        # key presses
        if event.type == pygame.KEYDOWN:
            for key in keys:
                keys[key].eventPressed(event.key)
            if event.key == pygame.K_SPACE:
                # navMapWriteData(robot.nav_map.latest_nav_map)
                pass
        if event.type == pygame.KEYUP:
            for key in keys:
                keys[key].eventReleased(event.key)
    
    ### graphics
    ## background
    gui.draw()

    ## keys
    for key in keys:
        keys[key].draw(gui.display)
    
    ## from Vector's camera - processing
    pilImage = Image.open("Assets/400px.png")
    pygameImage = gui.pilImageToSurface(pilImage)
    ## from Vector's camera - displaying
    gui.display.blit(pygameImage, (0, 0))
    
    gui.updateDisplay()