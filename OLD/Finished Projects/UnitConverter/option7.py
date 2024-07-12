import pygame
import processors
import messages


pygame.init()


def main():
    ds = pygame.display.set_mode((426, 217))
    pygame.display.set_caption("Unit Converter - Option 7: Palindrome Finder")

    clock = pygame.time.Clock()
    fps = 30

    bg = pygame.image.load("option7.png")
    cursor = pygame.image.load("cursor.png")
    cursor2 = pygame.image.load("cursor2.png")

    cursorBlinkCount = 15
    cursorBlinking = False
    selectedBox = 0

    b1Contents = []
    answer = []

    def drawChars(start, toPrint):
        chars = pygame.image.load("chars.png")
        charList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

        x = start[0]
        y = start[1]

        for char in toPrint:
            for i in range(11):
                try:
                    if char == charList[i]:
                        ds.blit(chars, (x, y), ((i * 15), 0, 15, 21))
                        break
                except IndexError:
                    break
            x += 18

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "EXIT"
                if selectedBox == 1:
                    if event.key == pygame.K_KP_0 or event.key == pygame.K_0:
                        b1Contents.append("0")
                    if event.key == pygame.K_KP_1 or event.key == pygame.K_1:
                        b1Contents.append("1")
                    if event.key == pygame.K_KP_2 or event.key == pygame.K_2:
                        b1Contents.append("2")
                    if event.key == pygame.K_KP_3 or event.key == pygame.K_3:
                        b1Contents.append("3")
                    if event.key == pygame.K_KP_4 or event.key == pygame.K_4:
                        b1Contents.append("4")
                    if event.key == pygame.K_KP_5 or event.key == pygame.K_5:
                        b1Contents.append("5")
                    if event.key == pygame.K_KP_6 or event.key == pygame.K_6:
                        b1Contents.append("6")
                    if event.key == pygame.K_KP_7 or event.key == pygame.K_7:
                        b1Contents.append("7")
                    if event.key == pygame.K_KP_8 or event.key == pygame.K_8:
                        b1Contents.append("8")
                    if event.key == pygame.K_KP_9 or event.key == pygame.K_9:
                        b1Contents.append("9")
                    if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                        b1Contents.append(".")
                    if event.key == pygame.K_BACKSPACE:
                        try:
                            b1Contents.pop()
                        except IndexError:
                            pass
                    if event.key == pygame.K_DELETE:
                        b1Contents.clear()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # << BACK
                if 115 <= event.pos[0] <= 255 and 166 <= event.pos[1] <= 198:
                    return "RETURN_TO_MENU"
                # GO!
                elif 174 <= event.pos[0] <= 251 and 94 <= event.pos[1] <= 126:
                    answer.clear()
                    a = processors.option7(b1Contents)
                    for char in str(a):
                        answer.append(char)
                # HELP!
                elif 321 <= event.pos[0] <= 407 and 58 <= event.pos[1] <= 90:
                    messages.option7(1)
                elif 393 <= event.pos[0] <= 407 and 130 <= event.pos[1] <= 162:
                    messages.option7(2)
                # CONTROLS
                elif 259 <= event.pos[0] <= 499 and 166 <= event.pos[1] <= 198:
                    messages.controls()
                # RESET
                elif 13 <= event.pos[0] <= 111 and 166 <= event.pos[1] <= 198:
                    b1Contents.clear()
                    answer.clear()
                    selectedBox = 0
                # Selecting boxes
                elif 141 <= event.pos[0] <= 317 and 58 <= event.pos[1] <= 90:
                    cursorBlinking = True
                    selectedBox = 1
                # Resetting "cursor", no box selected.
                else:
                    cursorBlinking = False
                    selectedBox = 0
                    cursorBlinkCount = 15

        ds.blit(bg, (0, 0))

        if len(b1Contents) > 15:
            b1Contents.pop()

        if cursorBlinkCount % 30 >= 15:
            if selectedBox == 1 and len(b1Contents) < 15:
                ds.blit(cursor, (147 + (18 * len(b1Contents)), 64))
            elif selectedBox == 1 and len(b1Contents) == 15:
                ds.blit(cursor2, (147 + (18 * len(b1Contents)), 64))

        drawChars((147, 64), b1Contents)
        drawChars((147, 136), answer)

        pygame.display.update()

        if cursorBlinking:
            cursorBlinkCount += 1

        clock.tick(fps)


if __name__ == '__main__':
    print("PLEASE RUN MAIN.PY")
