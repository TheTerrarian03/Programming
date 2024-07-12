import pygame


def drawChars(string, surface, startX=0, startY=0, charSize=1):
    print(charSize)
    sheetOriginal = pygame.image.load("Chars_Font=1.png")
    sheet = pygame.transform.scale(sheetOriginal, (480 * charSize, 7 * charSize))
    x = startX
    print(x)
    y = startY
    print(y)
    charList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "-", ",", "\"",
                "'", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "[", "]",
                "{", "}", ";", ":", "\\", "|", "<", ">", ".", "/", "?", "=", "+"]
    print(charList)
    print("For loop:")
    for char in string:
        for i in range(len(charList)):
            try:
                print("TRY #" + str(i))
                if char == charList[i]:
                    print("IF")
                    surface.blit(sheet, (x, y), ((i * (5 * charSize)), 0, (5 * charSize), (7 * charSize)))
                    break
                elif char == " ":
                    print("IF SPACE")
                    x += (5 * charSize)
                    break
            except IndexError:
                print("EXCEPT INDEX_ERROR")
                break
        x += (6 * charSize)
        print("x is now: " + str(x))
    pygame.display.update()
