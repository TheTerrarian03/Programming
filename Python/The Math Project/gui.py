# copied from version of last update on: 07052023


import pygame
from typing import (Callable, Tuple, Any)

###  ----- GUI FEATURE LIST -----  ###
#    1. Graphical Shapes
#       a. Rectangles
#       b. Circles
#       c. 2-point lines
#       ..
#       y. Movability
#       z. Resizability
#    2. Information
#       a. Simple Text
#       b. Text with Border Box
#       c. Input Box
#       d. Check Box
#       e. Bullet Point Circle
#       f. Button with Text
#       g. Button with Icon
#    3. Window Layout/Navigation
#       a. Border Bars
#       b. Scroll Bars
###  ----------------------------  ###

# GUI FOCUS: simplicity to use

# EXCEPTIONS
class GUI_Exception(Exception):
    """Exception raised when not all required functions are present in an element trying to be added"""

    def __init__(self, message):
        super().__init__(message)

# GRAPHICAL SHAPES
class Rectangle:
    '''Make a Rectangle: This is a simple squared-off rectangle with a border color and filler color
    
        Parameters:
            left (int | Callable): left pos of rectangle
            top (int | Callable): top pos of rectangle
            right (int | Callable): right pos of rectangle (x-width)
            bottom (int | Callable): bottom pos of rectangle (y-height downward)'''
    
    def __init__(self, left: int | Callable, top: int | Callable, width: int | Callable, height: int | Callable):
        # setup positions and sizes
        self.left = left if isinstance(left, Callable) else lambda: left
        self.top = top if isinstance(top, Callable) else lambda: top
        self.width = width if isinstance(width, Callable) else lambda: width
        self.height = height if isinstance(height, Callable) else lambda: height

        # setup default colors and border width
        self.fillerColor = lambda: [255, 0, 0]
        self.borderColor = lambda: [0, 0, 0]
        self.borderWidth = lambda: 1

        # setup default interactions
        self.resizableDirections = lambda: "xy"
        self.canBeMoved = lambda: True

        # intitial mouse state stuff
        self.mouse = {
            "clicked": False,
            "border": "",
            "tl_offset": [0, 0]
        }

        # amount of pixels the mouse can be farther from the original line to be considered near
        PLAY = 3

        # collisions rects for mouse detection
        self.coll_rects = {
            "left": pygame.rect.Rect(self.left()-PLAY, self.top()-PLAY, PLAY, self.height()+(PLAY*2)),
            "top": pygame.rect.Rect(self.left()-PLAY, self.top()-PLAY, self.width()+(PLAY*2), PLAY),
            "right": pygame.rect.Rect((self.left()+self.width()), self.top()-PLAY, PLAY, self.height()+(PLAY*2)),
            "bottom": pygame.rect.Rect(self.left()-PLAY, (self.top()+self.height()), self.width()+(PLAY*2), PLAY),
            "fill": pygame.rect.Rect(self.left(), self.top(), self.width(), self.height())
        }
    
    def setupColors(self, fillerColor: list | Callable, borderColor: list | Callable):
        self.fillerColor = fillerColor if isinstance(fillerColor, Callable) else lambda: fillerColor
        self.borderColor = borderColor if isinstance(borderColor, Callable) else lambda: borderColor

    def setupBorderWidth(self, borderWidth: int | Callable):
        self.borderWidth = borderWidth if isinstance(borderWidth, Callable) else lambda: borderWidth

    def setupInteractions(self, resizableDirections: str | Callable, canBeMoved: bool | Callable):
        self.resizableDirections = resizableDirections if isinstance(resizableDirections, Callable) else lambda: resizableDirections
        self.canBeMoved = canBeMoved if isinstance(canBeMoved, Callable) else lambda: canBeMoved

    def handleEvents(self, pygameEvents):
        # check for mouse at borders
        mousePos = pygame.mouse.get_pos()
        near = ""
        mouseCursorDirection = ""

        if self.coll_rects["left"].collidepoint(mousePos[0], mousePos[1]):
            near += "l"
        if self.coll_rects["top"].collidepoint(mousePos[0], mousePos[1]):
            near += "t"
        if self.coll_rects["right"].collidepoint(mousePos[0], mousePos[1]):
            near += "r"
        if self.coll_rects["bottom"].collidepoint(mousePos[0], mousePos[1]):
            near += "b"
        if self.coll_rects["fill"].collidepoint(mousePos[0], mousePos[1]):
            near = "f"
        
        if ("l" in near and "t" in near) or ("r" in near and "b" in near):
            mouseCursorDirection = "-xy"  # diag down
        elif ("l" in near and "b" in near) or ("t" in near and "r" in near):
            mouseCursorDirection = "+xy"  # diag up
        elif ("l" in near) or ("r" in near):
            mouseCursorDirection = "x"    # x-axis
        elif ("t" in near) or ("b" in near):
            mouseCursorDirection = "y"    # y-axis
        elif "f" in near:
            mouseCursorDirection = "xy"   # cross thingy (the plus of arrows)

        # TODO: set mouse cursor icon

        # set mouse state in self if mouse click events occur
        for event in pygameEvents:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    print("mouse 0 down")
                    self.mouse["clicked"] = True
                    self.mouse["border"] = near
                    self.mouse["tl_offset"] = [mousePos[0]-self.left(), mousePos[1]-self.top()]
            if event.type == pygame.MOUSEBUTTONUP:
                if not pygame.mouse.get_pressed()[0]:
                    print("mouse 0 up")
                    self.mouse["clicked"] = False
                    self.mouse["border"] = ""
                    self.mouse["tl_offset"] = [mousePos[0]-self.left(), mousePos[1]-self.top()]

    def update(self):
        # update positions if mouse dragging
        if self.mouse["clicked"]:
            mousePos = pygame.mouse.get_pos()
            near = self.mouse["border"]
            print(near, self.left(), self.top(), self.width(), self.height(), self.mouse["tl_offset"], self.mouse["border"])
            if near == "f":
                self.left = lambda: mousePos[0]-self.mouse["tl_offset"][0]
                self.top = lambda: mousePos[1]-self.mouse["tl_offset"][1]
            else:
                if ("l" in near):
                    self.left = lambda: mousePos[0]
                    self.width = lambda: mousePos[0]-self.left()
                if ("t" in near):
                    self.top = lambda: mousePos[1]
                    self.height = lambda: mousePos[1]-self.top()
                if ("r" in near):
                    self.width = lambda: mousePos[0]-self.left()
                if ("b" in near):
                    self.height = lambda: mousePos[1]-self.top()

        # amount of pixels the mouse can be farther from the original line to be considered near
        PLAY = 3

        # collisions rects for mouse detection
        self.coll_rects = {
            "left": pygame.rect.Rect(self.left()-PLAY, self.top()-PLAY, PLAY, self.height()+(PLAY*2)),
            "top": pygame.rect.Rect(self.left()-PLAY, self.top()-PLAY, self.width()+(PLAY*2), PLAY),
            "right": pygame.rect.Rect((self.left()+self.width()), self.top()-PLAY, PLAY, self.height()+(PLAY*2)),
            "bottom": pygame.rect.Rect(self.left()-PLAY, (self.top()+self.height()), self.width()+(PLAY*2), PLAY),
            "fill": pygame.rect.Rect(self.left(), self.top(), self.width(), self.height())
        }

    def draw(self, surface):
        # draw filled center
        pygame.draw.rect(surface, self.fillerColor(), (self.left(), self.top(), self.width(), self.height()))
        # draw border
        pygame.draw.rect(surface, self.borderColor(), (self.left(), self.top(), self.width(), self.height()), self.borderWidth())


# MAIN DISPLAY
class Display:
    '''Main Display class! This will handle most event handling, updating and drawing of the main display as well as any other elements added to it.
    
        Parameters:
            caption (str): title of window
            dispX (int): initial x resolution of window
            dispY (int): initial y resolution of window
            isResizable (bool): whether or not to let the user resize the window'''
    
    def __init__(self, caption: str="Pygame GUI Window", dispX: int=1366, dispY: int=768, isResizable: bool=False, maxFPS: float=60):
        pygame.init()
        
        # setup pygame display
        self.dispSize = [dispX, dispY]
        if isResizable:
            self.surf = pygame.display.set_mode(self.dispSize, pygame.RESIZABLE)
        else:
            self.surf = pygame.display.set_mode(self.dispSize)
        pygame.display.set_caption(caption)

        # define an empty pages/elements list
        self.pages = {
            0: []
        }

        self.page = 0

        # define a running variable to true
        self.running = True

        # define clock tick fps rate
        self.clock = pygame.time.Clock()
        self.fps = maxFPS
    
    def addElement(self, elements: Any | list, page: int=0):
        '''Add an element(s) to the display to render and handle.
        
            Parameters:
                element: any element to handle. Can by anything as long as it has handleEvents, update, and draw functions to call periodically
                page: page in ui to add element to. Optional and defaults to 0'''
        
        def addElementToPage(element):
            self.pages[page].append(element)

        def tryAddElement(element):
            # check for required functions
            hasHandleEvents = getattr(element, "handleEvents", None)
            hasUpdate = getattr(element, "update", None)
            hasDraw = getattr(element, "draw", None)

            if (not hasHandleEvents) | (not hasUpdate) | (not hasDraw):
                raise GUI_Exception(f"Missing a handleEvents(), update(), or draw() method on {str(type(element))} element")
            else:
                addElementToPage(element)
        
        if isinstance(elements, list):
            for element in elements:
                tryAddElement(element)
        else:
            tryAddElement(elements)

    def handleEvents(self):
        pygameEvents = pygame.event.get()

        # display-related events
        for event in pygameEvents:
            # print(event)
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.WINDOWRESIZED:
                # resize self display size if window resized
                self.dispSize = self.surf.get_size()
        
        # call handleEvents functions in elements
        for element in self.pages[self.page]:
            element.handleEvents(pygameEvents)

    def draw(self):
        # draw window background
        pygame.draw.rect(self.surf, [25, 25, 25], (0, 0, self.dispSize[0], self.dispSize[1]))

        # update then draw elements
        for element in self.pages[self.page]:
            element.update()
            element.draw(self.surf)

        # update window surface
        pygame.display.update()

    def tickClock(self):
        self.clock.tick(self.fps)

    def update(self):
        self.handleEvents()
        self.draw()
        self.tickClock()

    # getter methods for positions and such
    def left(self):
        return 0
    
    def right(self):
        return self.surf.get_size()[0]
    
    def top(self):
        return 0
    
    def bottom(self):
        return self.surf.get_size()[1]