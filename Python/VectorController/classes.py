import pygame
from PIL import Image


class GUI:
    def __init__(self, title, res=[400, 400], bg=(50, 50, 50)):
        self.title = title
        self.res = res
        self.bg = bg
        self.setPygameVariables()
    
    def setPygameVariables(self):
        self.display = pygame.display.set_mode(self.res)
        pygame.display.set_caption(self.title)
    
    def draw(self):
        pygame.draw.rect(self.display, self.bg, (0, 0, self.res[0], self.res[1]))
    
    def updateDisplay(self):
        pygame.display.update()
    
    def pilImageToSurface(self, pilImage):
        return pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

class keyboardKey:
    def __init__(self, pygameKeyCode, position, resolution, colorOff=(200, 0, 0), colorOn=(0, 200, 0), additionalValue=0):
        self.keyCode = pygameKeyCode
        self.pos = position
        self.res = resolution
        self.off = colorOff
        self.on = colorOn
        self.pressed = False
        self.value = additionalValue
    
    def eventPressed(self, pressedPygameKeyCode):
        if pressedPygameKeyCode == self.keyCode:
            self.pressed = True
            return True
        else:
            return False
    
    def eventReleased(self, releasedPygameKeyCode):
        if releasedPygameKeyCode == self.keyCode:
            self.pressed = False
            return True
        else:
            return False

    def draw(self, display):
        if self.pressed:
            pygame.draw.rect(display, self.on, (self.pos[0], self.pos[1], self.res[0], self.res[1]))
        else:
            pygame.draw.rect(display, self.off, (self.pos[0], self.pos[1], self.res[0], self.res[1]))

    def getValue(self):
        if self.pressed:
            return self.value
        else:
            return 0
