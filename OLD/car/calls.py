import pygame
import variables as v


def resetGrid(defImgNum):
    v.grid = []
    for row in range(v.tiles):
        row = []
        for _ in range(v.tiles):
            row.append([defImgNum, 0, False])
        v.grid.append(row)
    return v.grid


def checkIntGT0(value, name="number"):
    # 0=good, 1=notInt, 2=lt0
    try:
        value = int(value)
        if value > 0:
            return int(value)
        else:
            raise Exception(str(name) + " must be greater than 0.")
    except ValueError:
        raise Exception(str(name) + " must be an integer.")


def resizeDisplay(tiles=None):
    if tiles:
        try:
            tiles = int(tiles)
            v.tiles = tiles
        except ValueError:
            print("new tile amount needs to be an integer")
    if v.tiles*v.scale > 140:
        v.dispWid = v.tiles*v.scale
    else:
        v.dispWid = 140
    v.dispHi = (v.tiles*v.scale) + 60
    v.display = pygame.display.set_mode((v.dispWid, v.dispHi))


def drawGraphics(surface, startx=0, starty=0):
    # main grid drawing
    for row in range(len(v.grid)):
        for col in range(len(v.grid[row])):
            surface.blit(v.images[v.grid[row][col][0]], ((col*v.scale)+startx, 
                                                         (row*v.scale)+starty))
    
    # selection drawing
    for row in range(len(v.grid)):
        for col in range(len(v.grid)):
            if v.grid[row][col][2] == True:
                # top border
                pygame.draw.rect(surface,
                                 (v.selCol),
                                 ((col*v.scale)+startx,
                                  (row*v.scale)+starty,
                                  v.scale, 4))
                # bottom border
                pygame.draw.rect(surface,
                                 (v.selCol),
                                 ((col*v.scale)+startx,
                                  (row*v.scale)+starty+v.scale-4,
                                  v.scale, 4))
                # left border
                pygame.draw.rect(surface,
                                 (v.selCol),
                                 ((col*v.scale)+startx,
                                  (row*v.scale)+starty,
                                  4, v.scale))
                # right border
                pygame.draw.rect(surface,
                                 (v.selCol),
                                 ((col*v.scale)+startx+v.scale-4,
                                  (row*v.scale)+starty,
                                  4, v.scale))
    
    # bottom toolbar drawing
    pygame.draw.rect(surface, (90, 90, 90),
                     (0, v.dispHi-60, v.dispWid, 60))


def changeSelection(mX, mY, mB):
    newColSel = mX // v.scale
    newRowSel = mY // v.scale
    # erasing existing selections
    for row in range(len(v.grid)):
        for col in range(len(v.grid[row])):
            v.grid[row][col][2] = False
    try:
        v.grid[newRowSel][newColSel][2] = True
        # print("Tile at (" + str(newColSel) + ", " + str(newRowSel) + ") selected")
    except IndexError:
        print("*IndexError*")


def changeFillSelect(mX, mY, mB):
    pass


def resizeImages(newRes):
    for imgNum in range(len(v.images)):
        newImg = pygame.transform.scale(v.images[imgNum], (newRes, newRes))
        v.images[imgNum] = newImg


def askCommand():
    print("\nPlease enter a command:\n"
          "load ----- load map from file\n"
          "fill ----- fill map with one of a tile\n"
          "scaleall - scale all images to given res\n"
          "select --- select (2, 2) (TEMPORARY)\n"
          "exit ----- stop game and exit program")
    ui = input("$ ")
    if ui.lower() == "load":
        # not working
        fileName = input("Enter name (.py file): ")
        print(fileName)
    elif ui.lower() == "fill":  # fill the map
        dIN = input("Image Number to fill with:\n$ ")
        try:
            dIN = int(dIN)
            resetGrid(dIN)
        except ValueError:
            print("Default Image Number must be a integer.")
        return 0
    elif ui.lower() == "scaleall":  # scale all v.images images
        newRes = input("Please enter side length of new tiles:\n$ ")
        try:
            newRes = int(newRes)
            resizeWin = input("\nResize window too?\n$ ")
            if resizeWin.lower() == "y" or resizeWin.lower() == "yes":
                resizeWin = True
                print("Yes.")
            else:
                resizeWin = False
                print("No.")
            resizeImages(newRes)
            if resizeWin:
                v.scale = newRes
                resizeDisplay()
        except ValueError:
            print("New side length must be an integer.")
        return 0
    elif ui.lower() == "exit":
        sure = input("\nAre you sure?\n$ ")
        if sure.lower() == "y" or sure.lower() == "yes":
            print("\"Yes\" entered, exiting program.")
            return 1
        else:
            print("\"No\" entered, continuing program.")
            return 0
    elif ui.lower() == "select":
        v.grid[2][2][2] = True
        print("Tile at (2, 2) selected")
        print(v.grid)
        return 0
    else:
        print("invalid command, continuing execution of program")

if __name__ == "__main__":
    print("Please run the `main.py` file instead.")

