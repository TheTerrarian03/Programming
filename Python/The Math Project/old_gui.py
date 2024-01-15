import pygame
from typing import (Callable, Tuple, Any)

### Special data-tracking-or-holding classes

class Font:
    '''Make a font! Takes in font name, font size, and color

        Parameters:
            fontName (str): name of the font
            fontSize (int): size of the font
            color (list): the colors, in rgb values, for of the text
    '''
    def __init__(self, fontName: str="default", fontSize: int=16, color: list[int]=[0, 0, 0]):
        self.fontName = fontName
        self.fontSize = fontSize
        self.color = color

        if self.fontName == "default":
            self.fontName = pygame.font.get_default_font()

        self.initFont()
    
    # def default():
    #     '''Return an object of Font that serves as a "default" font'''
    #     return Font("default", 16, [0, 0, 0])

    def initFont(self):
        '''Load a font from PyGame'''
        self.pyFont = pygame.font.SysFont(self.fontName, self.fontSize)
    
    def render(self, content: str):
        '''Render and return and image, with the content as text, to be blit'd'''
        return self.pyFont.render(content, True, self.color)

class Coord2D:
    '''Make a 2D coordinate! Used to hold either a static int for x and y, or lambdas for dynamic x-and-y-getters
    
        Parameters:
            x (int or Callable): value for x
            y (int or Callable): value for y
            marginX (int): optional margin value for x
            marginY (int): optional margin value for y'''
    
    def __init__(self, x: int | Callable, y: int | Callable, marginX: int=0, marginY: int=0):
        # setup self values by calling self's set method
        self.set(x, y, marginX, marginY)

    def set(self, x: int | Callable, y: int | Callable, marginX: int=0, marginY: int=0):
        '''Setup the Coord2D object
    
        Parameters:
            x (int or Callable): value for x
            y (int or Callable): value for y
            marginX (int): optional margin value for x
            marginY (int): optional margin value for x'''
        
        # set margins
        self.marginX = marginX
        self.marginY = marginY
        
        # set x and y value lambdas based on whether an int or callable is passed in
        if isinstance(x, Callable):
            self.xGetter = lambda : x() + self.marginX
        else:
            self.xGetter = lambda : x + self.marginX
        
        if isinstance(y, Callable):
            self.yGetter = lambda : y() + self.marginY
        else:
            self.yGetter = lambda : y + self.marginY

    def get(self):
        '''Get the (x, y) values of the Coord2D'''
        return (self.xGetter(), self.yGetter())

### Simple shapes

class SimpleRect:
    '''A simple rectangle to draw over anything you need drawn over
    
        Parameters:
            pos (Tuple[int, int], Coord2D): the top-left position for the rectangle
            width (int, Callable): the width for the rectangle
            height (int, Callable): the height for the rectangle
            color (list): the rgb values for the color for the rectangle'''
    
    def __init__(self, pos: Tuple[int, int] | Coord2D, width: int | Callable, height: int | Callable, color: list[int] | tuple[int, int, int]):
        # assign position
        if isinstance(pos, Tuple):
            self.posGetter = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.posGetter = lambda : pos.get()
        
        # assign width
        if isinstance(width, int):
            self.widthGetter = lambda : width
        elif isinstance(width, Callable):
            self.widthGetter = lambda : width()
        
        # assign height
        if isinstance(height, int):
            self.heightGetter = lambda : height
        elif isinstance(height, Callable):
            self.heightGetter = lambda : height()
        
        # assign colors
        self.color = color

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # draw rectangle
        pygame.draw.rect(surface, self.color, (self.posGetter()[0], self.posGetter()[1], self.widthGetter(), self.heightGetter()))

### Text

class Text:
    '''Make some text to put on screen! Takes in 3 simple arguments
    
        Parameters:
            pos (tuple or coord2D): top-left position for text
            content (any): text to write out to the screen
            font (Font): font for text'''
    
    def __init__(self, pos: Tuple[int, int] | Coord2D, content: Any | Callable, font: Font):
        # set pos
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
        
        # set content
        if isinstance(content, Callable):
            self.content = lambda : content()
        else:
            self.content = lambda : str(content)
        
        # set font obj
        self.font = font
    
    def getTextImg(self):
        '''Render and return the image of the text, rendered'''
        return self.font.render(self.content())

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # get rendrered image
        textImg = self.getTextImg()
        # blit image to surface
        surface.blit(textImg, self.pos())

class TextBox:
    '''Make a text box! It's a box of color, but with text in it!
    
        Parameters:
            pos (tuple or Coord2D): top-left position for text box, including margins
            content (any): text to be written out to the screen
            font (Font): font object for text
            bgColor (list): the rgb values for the color of the box
            margin (int): margin of box around text, all sides
            borderRadius (int): size of corner radius, all corners, straight edge default'''
    
    def __init__(self, pos: Tuple[int, int] | Coord2D, content: Any | Callable, font: Font, bgColor: list[int], margin: int=5, borderRadius: int=-1):
        # set pos based
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
            textPos = (pos[0] + margin, pos[1] + margin)
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
            textPos = Coord2D(lambda : pos.get()[0] + margin, lambda : pos.get()[1] + margin)
        
        # set other text-related variables like text obj, colors, margin, and border radii
        self.text = Text(textPos, content, font)
        self.bgColor = bgColor
        self.margin = margin
        self.borderRad = borderRadius

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # get text image
        textImg = self.text.getTextImg()
        # draw background rectangle, including rounded corners
        pygame.draw.rect(surface, self.bgColor, (self.pos()[0], self.pos()[1], textImg.get_size()[0] + (self.margin * 2), textImg.get_size()[1] + (self.margin * 2)), border_radius=self.borderRad)
        # blit text onto surface
        self.text.draw(surface)

### Buttons

class Button:
    '''Make a button! Exactly like a text box, but with the functionality of calling a providable function to call on click
    
        Parameters:
            pos (tuple or Coord2D): top-left position for text box, including margins
            content (any): text to be written out to the screen
            font (Font): font object for text
            bgColor (list): the rgb values for the color of the box
            margin (int): margin of box around text, all sides
            borderRadius (int): size of corner radius, all corners, straight edge default'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, text: Any | Callable, font: Font, margin: int=5, borderRadius: int=-1):
        # set pos
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
            textPos = (pos[0] + margin, pos[1] + margin)
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
            textPos = Coord2D(lambda : pos.get()[0] + margin, lambda : pos.get()[1] + margin)
        
        self.textObj = Text(textPos, text, font)   # text obj
        self.bgColor = consts.BUTTON.BG            # colors
        self.hlColor = consts.BUTTON.BG_HIGHLIGHT
        self.clColor = consts.BUTTON.BG_ACTIVE
        self.margin = margin                       # margin
        self.borderRad = borderRadius              # border radii
        
        # function to call on click
        self.clickFunc = lambda : None

        # mouse state variables
        self.mouseHovering = False
        self.mouseClicked = False
    
    def onClick(self, toCall: Callable):
        '''Assign a function to call when clicked
        
            Parameters:
                toCall (Callable): function to call when clicked'''
        self.clickFunc = toCall
    
    def setColors(self, background: list[int], highlight: list[int], clicked: list[int]):
        '''Set colors for buttons
            
            Parameters:
                background, highlight, and clicked (list): rgb values for those colors'''
        self.bgColor = background
        self.hlColor = highlight
        self.clicked = clicked
    
    def getButtonRect(self):
        '''Return pygame Rect object for entire button'''
        textImg = self.textObj.getTextImg()
        return pygame.Rect(self.pos()[0], self.pos()[1], textImg.get_size()[0] + (self.margin * 2), textImg.get_size()[1] + (self.margin * 2))

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # check if mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # is is a left click?
                if pygame.mouse.get_pressed()[0]:
                    # check for collision with button
                    if self.getButtonRect().collidepoint(mousePos):
                        # collision, set clicked to true
                        self.mouseClicked = True
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # no more left click held?
                if not pygame.mouse.get_pressed()[0]:
                    # call function if previous mouse state was pressed
                    if self.mouseClicked:
                        self.clickFunc()
                    # no left click, set clicked to False
                    self.mouseClicked = False
    
    def update(self):
        # get mouse pos
        mousePos = pygame.mouse.get_pos()
        # set hovering to true if mouse hovering, else false
        if self.getButtonRect().collidepoint(mousePos):
            self.mouseHovering = True
        else:
            self.mouseHovering = False

    def draw(self, surface):
        # get text image to blit and get size from
        textImg = self.textObj.getTextImg()
        # define color to draw button of
        if self.mouseClicked:
            color = self.clColor
        elif self.mouseHovering:
            color = self.hlColor
        else:
            color = self.bgColor
        # draw outside of button
        pygame.draw.rect(surface, color, self.getButtonRect(), border_radius=self.borderRad)
        # draw text
        self.textObj.draw(surface)

### Scroll bars

class HScrollBar:
    '''Make a (horizontal) scroll bar! Define some poses and sizes, along with min & max values, and you'll get an adjustable, dynamic scroll bar
    
        Paramters:
            pos (tuple or Coord2D): top-left pos of scroll bar
            borderRadius (int): size in pixels of roundness of corners
            width (int or Callable): width of entire scroll bar
            height (int or Callable): height of entire scroll bar
            minVal (int or Callable): minimum value for value range
            maxVal (int or Callable): maximum value for value range
            valWindow (int or Callable): value for how much of the range can be seen'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, borderRadius: int | str, width: int | Callable, height: int | Callable, minVal: int | Callable, maxVal: int | Callable, valWindow: int | Callable):
        # top-left pos
        if isinstance(pos, Tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
        
        # width
        if isinstance(width, int):
            self.width = lambda : width
        elif isinstance(width, Callable):
            self.width = lambda : width()
        
        # height
        if isinstance(height, int):
            self.height = lambda : height
        elif isinstance(height, Callable):
            self.height = lambda : height()

        # min val
        if isinstance(minVal, int):
            self.minVal = lambda : minVal
        elif isinstance(minVal, Callable):
            self.minVal = lambda : minVal()

        # max val
        if isinstance(maxVal, int):
            self.maxVal = lambda : maxVal
        elif isinstance(maxVal, Callable):
            self.maxVal = lambda : maxVal()

        # val window
        if isinstance(valWindow, int):
            self.valWindow = lambda : valWindow
        elif isinstance(valWindow, Callable):
            self.valWindow = lambda : valWindow()

        # scrollbar width getter
        self.barWidth = lambda : self.getBarWidth()

        # border radius
        if isinstance(borderRadius, int):
            self.borderRad = lambda : int(min(borderRadius, self.height()/2))
        elif isinstance(borderRadius, str):
            if borderRadius == "max":
                self.borderRad = lambda : int(self.height()/2)
            elif borderRadius == "half max":
                self.borderRad = lambda : int(self.height()/4)
            else:
                self.borderRad = lambda : 0
        
        # colors
        self.colorFG = consts.SCROLLBAR.FG
        self.colorBG = consts.SCROLLBAR.BG

        # mouse interaction variables
        self.mouseDragging = False
        self.mouseXPosOffset = 0
        self.barXPos = self.pos()[0]  # default value, far left
    
    def setColors(self, colorBG: list[int], colorFG: list[int]):
        '''Set scroll bar colors. Takes in lists of rgb values, as ints'''
        self.colorBG = colorBG
        self.colorFG = colorFG

    def getValue(self):
        '''Returns, as a float, the value the scroll bar is currently outputting, given min and max val range, and it's position'''

        # get pos percentage
        barPosPercent = self.getPercent()

        # get zero offset for easy value range finding
        toZeroOffset = min(self.minVal(), self.maxVal())
        # calculate range
        valueRange = (self.maxVal()-toZeroOffset) - (self.minVal()-toZeroOffset)
        # scale range by percentage
        value = barPosPercent * valueRange
        # offset back from zero
        value += toZeroOffset

        # return
        return value

    def getValueStr(self):
        '''Returns, as a string, the value the scroll bar is currently outputting, given min and max val range, and it's position'''
        return str(self.getValue())

    def getPercent(self):
        '''Returns the percentage from left-to-right, of how far along the scroll bar is currently'''

        # get distance to left
        toLeft = self.pos()[0]
        # half of bar width for centering
        halfBar = self.barWidth() / 2
        # left, offset by half bar ("center")
        leftCtr = halfBar
        # center of bar, offset by to-left amount
        barCtr = (self.barXPos + halfBar) - toLeft
        # right, offset by half bar ("center")
        rightCtr = self.width() - halfBar
        
        # calculate value based on position ratio and min/maxes
        try:
            percent = (barCtr - leftCtr) / (rightCtr - leftCtr)
        # catch zero division error by defaulting to 0
        except ZeroDivisionError:
            percent = 0

        # return
        return percent

    def getBarWidth(self):
        '''Returns, as a float or int, the width of the draggable scroll bar'''

        try:
            # base width off of percentage/ratio
            width = self.width() * (self.valWindow() / (self.maxVal() - self.minVal()))
        except ZeroDivisionError:
            # max width
            width = self.width()
        
        # also max width
        if width > self.width():
            width = self.width()

        # return
        return width

    def getEntireRect(self):
        '''Returns a pygame Rect of the entire scroll bar'''

        # left-top by width by height
        return pygame.Rect(self.pos()[0], self.pos()[1], self.width(), self.height())

    def getBarRect(self):
        '''Returns a pygame Rect of the draggable part of the scroll bar'''

        # xpos-top by barWidth() by height
        return pygame.Rect(self.barXPos, self.pos()[1], self.barWidth(), self.height())

    def clampBar(self):
        '''Make sure draggable part of the scroll bar is within its bounds'''

        # target pos past left bounds
        if (self.barXPos) < self.pos()[0]:
            self.barXPos = self.pos()[0]
        # target pos past right bounds
        elif (self.barXPos + self.barWidth()) > (self.pos()[0] + self.width()):
            self.barXPos = (self.pos()[0] + self.width()) - self.getBarWidth()
        # within bounds, do nothing
        else:
            pass

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # check if mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # is is a left click?
                if pygame.mouse.get_pressed()[0]:
                    # check for collision with little bar
                    if self.getBarRect().collidepoint(mousePos):
                        # collision, set dragging to true
                        self.mouseDragging = True
                        # offset set to mouse offset from bar, for intuitive dragging
                        self.mouseXPosOffset = pygame.mouse.get_pos()[0] - self.barXPos
                    # check for collision with entire bar
                    elif self.getEntireRect().collidepoint(mousePos):
                        # collision, set dragging values
                        self.mouseDragging = True
                        # offset set to half of bar, bar will jump to mouse pos (acts like most scrollbars)
                        self.mouseXPosOffset = self.barWidth() / 2
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # no more left click held?
                if not pygame.mouse.get_pressed()[0]:
                    # no left click, set dragging to False
                    self.mouseDragging = False

    def update(self):
        # check for mouse dragging
        if self.mouseDragging:
            # set self x pos to clamped values based on mouse position
            newX = pygame.mouse.get_pos()[0]
            
            # set variable
            self.barXPos = newX - self.mouseXPosOffset

        # always clamp bar pos
        self.clampBar()

    def draw(self, surface):
        # draw outer, inactive rect
        pygame.draw.rect(surface, self.colorBG, self.getEntireRect(), border_radius=self.borderRad())

        # draw inner, active rect (draggable part)
        pygame.draw.rect(surface, self.colorFG, self.getBarRect(), border_radius=self.borderRad())

class VScrollBar:
    '''Make a (vertical) scroll bar! Define some poses and sizes, along with min & max values, and you'll get an adjustable, dynamic scroll bar
    
        Paramters:
            pos (tuple or Coord2D): top-left pos of scroll bar
            borderRadius (int): size in pixels of roundness of corners
            width (int or Callable): width of entire scroll bar
            height (int or Callable): height of entire scroll bar
            minVal (int or Callable): minimum value for value range
            maxVal (int or Callable): maximum value for value range
            valWindow (int or Callable): value for how much of the range can be seen'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, borderRadius: int | str, width: int | Callable, height: int | Callable, minVal: int | Callable, maxVal: int | Callable, valWindow: int | Callable):
        # top-left pos
        if isinstance(pos, Tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
        
        # width
        if isinstance(width, int):
            self.width = lambda : width
        elif isinstance(width, Callable):
            self.width = lambda : width()
        
        # height
        if isinstance(height, int):
            self.height = lambda : height
        elif isinstance(height, Callable):
            self.height = lambda : height()

        # min val
        if isinstance(minVal, int):
            self.minVal = lambda : minVal
        elif isinstance(minVal, Callable):
            self.minVal = lambda : minVal()

        # max val
        if isinstance(maxVal, int):
            self.maxVal = lambda : maxVal
        elif isinstance(maxVal, Callable):
            self.maxVal = lambda : maxVal()

        # val window
        if isinstance(valWindow, int):
            self.valWindow = lambda : valWindow
        elif isinstance(valWindow, Callable):
            self.valWindow = lambda : valWindow()

        # scrollbar width getter
        self.barHeight = lambda : self.getBarHeight()

        # border radius
        if isinstance(borderRadius, int):
            self.borderRad = lambda : int(min(borderRadius, self.width()/2))
        elif isinstance(borderRadius, str):
            if borderRadius == "max":
                self.borderRad = lambda : int(self.width()/2)
            elif borderRadius == "half max":
                self.borderRad = lambda : int(self.width()/4)
            else:
                self.borderRad = lambda : 0
        
        # colors
        self.colorFG = consts.SCROLLBAR.FG
        self.colorBG = consts.SCROLLBAR.BG

        # mouse interaction variables
        self.mouseDragging = False
        self.mouseYPosOffset = 0
        self.barYPos = self.pos()[1]  # default value, very top
    
    def setColors(self, colorBG: list[int], colorFG: list[int]):
        '''Set scroll bar colors. Takes in lists of rgb values, as ints'''
        self.colorBG = colorBG
        self.colorFG = colorFG

    def getValue(self):
        '''Returns, as a float, the value the scroll bar is currently outputting, given min and max val range, and it's position'''
        
        # get pos percentage
        barPosPercent = self.getPercent()

        # get zero offset for easy value range finding
        toZeroOffset = min(self.minVal(), self.maxVal())
        # calculate range
        valueRange = (self.maxVal()-toZeroOffset) - (self.minVal()-toZeroOffset)
        # scale range by percentage
        value = barPosPercent * valueRange
        # offset back from zero
        value += toZeroOffset

        # return
        return value

    def getValueStr(self):
        '''Returns, as a float, the value the scroll bar is currently outputting, given min and max val range, and it's position'''
        
        return str(self.getValue())

    def getPercent(self):
        '''Returns the percentage from top-to-bottom, of how far along the scroll bar is currently'''
        
        # get distance to top
        toTop = self.pos()[1]
        # half of bar width for centering
        halfBar = self.barHeight() / 2
        # top, offset by half bar ("center")
        topCtr = halfBar
        # center of bar, offset by to-top amount
        barCtr = (self.barYPos + halfBar) - toTop
        # bottom, offset by half bar ("center")
        bottomCtr = self.height() - halfBar
        
        # calculate value based on position ratio and min/maxes
        try:
            percent = (barCtr - topCtr) / (bottomCtr - topCtr)
        # catch zero division error by defaulting to 0
        except ZeroDivisionError:
            percent = 0

        # return
        return percent

    def getBarHeight(self):
        '''Returns, as a float or int, the height of the draggable scroll bar'''
        
        try:
            # base width off of percentage/ratio
            height = self.height() * (self.valWindow() / (self.maxVal() - self.minVal()))
        except ZeroDivisionError:
            # max height
            height = self.height()
        
        # also max height
        if height > self.height():
            height = self.height()

        # return
        return height

    def getEntireRect(self):
        '''Returns a pygame Rect of the entire scroll bar'''
        
        # left-top by width by height
        return pygame.Rect(self.pos()[0], self.pos()[1], self.width(), self.height())

    def getBarRect(self):
        '''Returns a pygame Rect of the draggable part of the scroll bar'''
        
        # left-ypos by width by barHeight()
        return pygame.Rect(self.pos()[0], self.barYPos, self.width(), self.barHeight())

    def clampBar(self):
        '''Make sure draggable part of the scroll bar is within its bounds'''
        
        # target pos past left bounds
        if (self.barYPos) < self.pos()[1]:
            self.barYPos = self.pos()[1]
        # target pos past right bounds
        elif (self.barYPos + self.barHeight()) > (self.pos()[1] + self.height()):
            self.barYPos = (self.pos()[1] + self.height()) - self.barHeight()
        # within bounds, do nothing
        else:
            pass

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # check if mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # is it a left click?
                if pygame.mouse.get_pressed()[0]:
                    # check for collision with little bar
                    if self.getBarRect().collidepoint(mousePos):
                        # collision, set dragging to true
                        self.mouseDragging = True
                        # offset set to mouse offset from bar, for intuitive dragging
                        self.mouseYPosOffset = pygame.mouse.get_pos()[1] - self.barYPos
                    # check for collision with entire bar
                    elif self.getEntireRect().collidepoint(mousePos):
                        # collision, set dragging values
                        self.mouseDragging = True
                        # offset set to half of bar, bar will jump to mouse pos (acts like most scrollbars)
                        self.mouseYPosOffset = self.barHeight() / 2
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # no more left click held?
                if not pygame.mouse.get_pressed()[0]:
                    # no left click, set dragging to False
                    self.mouseDragging = False

    def update(self):
        # check for mouse dragging
        if self.mouseDragging:
            # set self x pos to clamped values based on mouse position
            newY = pygame.mouse.get_pos()[1]
            
            # set variable
            self.barYPos = newY - self.mouseYPosOffset

        # always clamp bar pos
        self.clampBar()

    def draw(self, surface):
        # draw outer, inactive rect
        pygame.draw.rect(surface, self.colorBG, self.getEntireRect(), border_radius=self.borderRad())

        # draw inner, active rect (draggable part)
        pygame.draw.rect(surface, self.colorFG, self.getBarRect(), border_radius=self.borderRad())

### Value selector

### Borders (They don't drag/resize/move currently)

class HBorder:
    '''Make a horizontal border! Essentially just a black seperating line
    
        Paramters:
            yPos (int or Callable): y-position for the top of the line
            thickness (int): thickness for the line (extends downward)'''

    def __init__(self, yPos: int | Callable, thickness: int=2):
        # set y pos
        if isinstance(yPos, int):
            self.yPos = lambda : yPos
        elif isinstance(yPos, Callable):
            self.yPos = lambda : yPos()

        # set thickness and height
        self.thickness = thickness
        self.width = None
    
    def setMaxWidth(self, max: int | Callable):
        '''Set max width of the border
        
            Parameters:
                max (int or Callable): max width of the border'''
        
        # set based on type
        if isinstance(max, int):
            self.width = lambda : max
        elif isinstance(max, Callable):
            self.width = lambda : max()
    
    def getYPosInt(self):
        '''Returns, as an int or float, the top y pos of the line'''

        return self.yPos()

    def getYPosStr(self):
        '''Returns, as a string, the top y pos of the line'''

        return str(self.getYPosInt())

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # if width getter is not set, get the width of the surface given
        if self.width == None:
            width = surface.get_size()[0]
        # else, get width
        else:
            width = self.width()
        
        # draw rectangle
        pygame.draw.rect(surface, consts.BORDER.BG, (0, self.yPos(), width, self.thickness))

class VBorder:
    '''Make a vertical border! Essentially just a black seperating line
    
        Paramters:
            xPos (int or Callable): x-position for the left of the line
            thickness (int): thickness for the line (extends rightward)'''

    def __init__(self, xPos: int | Callable, thickness: int=2):
        # set y pos
        if isinstance(xPos, int):
            self.xPos = lambda : xPos
        elif isinstance(xPos, Callable):
            self.xPos = lambda : xPos()

        # set thickness and height
        self.thickness = thickness
        self.width = None
    
    def setMaxWidth(self, max: int | Callable):
        '''Set max width of the border
        
            Parameters:
                max (int or Callable): max width of the border'''
        
        # set based on type
        if isinstance(max, int):
            self.width = lambda : max
        elif isinstance(max, Callable):
            self.width = lambda : max()
    
    def getXPosInt(self):
        '''Returns, as an int or float, the top y pos of the line'''

        return self.xPos()

    def getXPosStr(self):
        '''Returns, as a string, the top y pos of the line'''

        return str(self.getYPosInt())

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # if width getter is not set, get the width of the surface given
        if self.width == None:
            width = surface.get_size()[1]
        # else, get width
        else:
            width = self.width()
        
        # draw rectangle
        pygame.draw.rect(surface, consts.BORDER.BG, (self.xPos(), 0, self.thickness, width))

### Main Display class

class Display:
    '''Main Display class! This will handle most event handling, updating and drawing of the main display as well as any other elements added to it.
    
        Parameters:
            caption (str): title of window
            dispX (int): x resolution of window
            dispY (int): y resolution of window
            isResizable (bool): whether or not to let the user resize the window'''
    
    def __init__(self, caption: str="Pygame GUI Window", dispX: int=1366, dispY: int=768, isResizable: bool=False):
        pygame.init()
        
        # setup pygame display
        self.dispSize = [dispX, dispY]
        if isResizable:
            self.surf = pygame.display.set_mode(self.dispSize, pygame.RESIZABLE)
        else:
            self.surf = pygame.display.set_mode(self.dispSize)
        pygame.display.set_caption(caption)

        # define an empty elements list
        self.elements = []

        # define a running variable to true
        self.running = True
    
    def addElement(self, element):
        '''Add an element to the display to render and handle.
        
            Parameters:
                element: any element to handle. Can by anything as long as it has handleEvents, update, and draw functions to call periodically'''
        
        self.elements.append(element)
    
    def addElements(self, elements: list):
        '''Add some elements to the display to render and handle.
        
            Parameters:
                elements (list): a list of elements to handle. An element can by anything as long as it has handleEvents, update, and draw functions to call periodically'''

        for element in elements:
            self.addElement(element)

    def handleEvents(self, pygameEvents):
        # display-related events
        for event in pygameEvents:
            # print(event)
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.WINDOWRESIZED:
                # resize self display size if window resized
                self.dispSize = self.surf.get_size()
        
        # call handleEvents functions in elements
        for element in self.elements:
            element.handleEvents(pygameEvents)

    def update(self):
        # draw window background
        pygame.draw.rect(self.surf, consts.WINDOW.BG, (0, 0, self.dispSize[0], self.dispSize[1]))

        # update then draw elements
        for element in self.elements:
            element.update()
            element.draw(self.surf)

        # update window surface
        pygame.display.update()
