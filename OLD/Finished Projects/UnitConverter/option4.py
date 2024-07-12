import pygame
import processors
import messages


pygame.init()


def main():
    ds = pygame.display.set_mode((590, 301))
    pygame.display.set_caption("Unit Converter - Option 4: LCM")

    clock = pygame.time.Clock()
    fps = 30

    bg = pygame.image.load("option4.png")
    cursor = pygame.image.load("cursor.png")
    cursor2 = pygame.image.load("cursor2.png")

    cursorBlinkCount = 15
    cursorBlinking = False
    selectedBox = 0

    b1Contents = []
    b2Contents = []
    b3Contents = []
    answer = []

    def drawChars(start, toPrint):
        chars = pygame.image.load("chars.png")
        charList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "a", "b", "c", "d", "e", "f", "g", "h", 'i',
                    "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "-"]

        x = start[0]
        y = start[1]

        for char in toPrint:
            for i in range(38):
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
                    if event.key == pygame.K_BACKSPACE:
                        try:
                            b1Contents.pop()
                        except IndexError:
                            pass
                    if event.key == pygame.K_DELETE:
                        b1Contents.clear()
                if selectedBox == 2:
                    if event.key == pygame.K_KP_0 or event.key == pygame.K_0:
                        b2Contents.append("0")
                    if event.key == pygame.K_KP_1 or event.key == pygame.K_1:
                        b2Contents.append("1")
                    if event.key == pygame.K_KP_2 or event.key == pygame.K_2:
                        b2Contents.append("2")
                    if event.key == pygame.K_KP_3 or event.key == pygame.K_3:
                        b2Contents.append("3")
                    if event.key == pygame.K_KP_4 or event.key == pygame.K_4:
                        b2Contents.append("4")
                    if event.key == pygame.K_KP_5 or event.key == pygame.K_5:
                        b2Contents.append("5")
                    if event.key == pygame.K_KP_6 or event.key == pygame.K_6:
                        b2Contents.append("6")
                    if event.key == pygame.K_KP_7 or event.key == pygame.K_7:
                        b2Contents.append("7")
                    if event.key == pygame.K_KP_8 or event.key == pygame.K_8:
                        b2Contents.append("8")
                    if event.key == pygame.K_KP_9 or event.key == pygame.K_9:
                        b2Contents.append("9")
                    if event.key == pygame.K_BACKSPACE:
                        try:
                            b2Contents.pop()
                        except IndexError:
                            pass
                    if event.key == pygame.K_DELETE:
                        b2Contents.clear()
                if selectedBox == 3:
                    if event.key == pygame.K_KP_0 or event.key == pygame.K_0:
                        b3Contents.append("0")
                    if event.key == pygame.K_KP_1 or event.key == pygame.K_1:
                        b3Contents.append("1")
                    if event.key == pygame.K_KP_2 or event.key == pygame.K_2:
                        b3Contents.append("2")
                    if event.key == pygame.K_KP_3 or event.key == pygame.K_3:
                        b3Contents.append("3")
                    if event.key == pygame.K_KP_4 or event.key == pygame.K_4:
                        b3Contents.append("4")
                    if event.key == pygame.K_KP_5 or event.key == pygame.K_5:
                        b3Contents.append("5")
                    if event.key == pygame.K_KP_6 or event.key == pygame.K_6:
                        b3Contents.append("6")
                    if event.key == pygame.K_KP_7 or event.key == pygame.K_7:
                        b3Contents.append("7")
                    if event.key == pygame.K_KP_8 or event.key == pygame.K_8:
                        b3Contents.append("8")
                    if event.key == pygame.K_KP_9 or event.key == pygame.K_9:
                        b3Contents.append("9")
                    if event.key == pygame.K_BACKSPACE:
                        try:
                            b3Contents.pop()
                        except IndexError:
                            pass
                    if event.key == pygame.K_DELETE:
                        b3Contents.clear()
                if event.key == pygame.K_TAB:
                    selectedBox += 1
                if event.key == pygame.K_UP:
                    if selectedBox > 1:
                        selectedBox -= 1
                if event.key == pygame.K_DOWN:
                    selectedBox += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                # << BACK
                if 224 <= event.pos[0] <= 364 and 250 <= event.pos[1] <= 282:
                    return "RETURN_TO_MENU"
                # GO!
                elif 256 <= event.pos[0] <= 333 and 166 <= event.pos[1] <= 198:
                    answer.clear()
                    a = processors.option4(b1Contents, b2Contents, b3Contents)
                    for char in str(a):
                        answer.append(char)
                # HELP! 's
                elif 485 <= event.pos[0] <= 571 and 58 <= event.pos[1] <= 90:
                    messages.option4()
                elif 485 <= event.pos[0] <= 571 and 94 <= event.pos[1] <= 126:
                    messages.option4()
                elif 485 <= event.pos[0] <= 571 and 130 <= event.pos[1] <= 162:
                    messages.option4()
                # CONTROLS
                elif 368 <= event.pos[0] <= 520 and 250 <= event.pos[1] <= 282:
                    messages.controls()
                # RESET
                elif 122 <= event.pos[0] <= 220 and 250 <= event.pos[1] <= 282:
                    b1Contents.clear()
                    b2Contents.clear()
                    b3Contents.clear()
                    answer.clear()
                    selectedBox = 0
                # Selecting boxes
                elif 174 <= event.pos[0] <= 481 and 58 <= event.pos[1] <= 90:
                    cursorBlinking = True
                    selectedBox = 1
                elif 174 <= event.pos[0] <= 481 and 94 <= event.pos[1] <= 126:
                    cursorBlinking = True
                    selectedBox = 2
                elif 174 <= event.pos[0] <= 481 and 130 <= event.pos[1] <= 162:
                    cursorBlinking = True
                    selectedBox = 3
                # Resetting "cursor", no box selected.
                else:
                    cursorBlinking = False
                    selectedBox = 0
                    cursorBlinkCount = 15

        ds.blit(bg, (0, 0))

        if selectedBox > 3:
            selectedBox = 3

        if len(b1Contents) > 15:
            b1Contents.pop()
        if len(b2Contents) > 15:
            b2Contents.pop()
        if len(b3Contents) > 15:
            b3Contents.pop()

        if cursorBlinkCount % 30 >= 15:
            if selectedBox == 1 and len(b1Contents) < 15:
                ds.blit(cursor, (191 + (18 * len(b1Contents)), 64))
            elif selectedBox == 1 and len(b1Contents) == 15:
                ds.blit(cursor2, (191 + (18 * len(b1Contents)), 64))

            if selectedBox == 2 and len(b2Contents) < 15:
                ds.blit(cursor, (191 + (18 * len(b2Contents)), 100))
            elif selectedBox == 2 and len(b2Contents) == 15:
                ds.blit(cursor2, (191 + (18 * len(b2Contents)), 100))

            if selectedBox == 3 and len(b3Contents) < 15:
                ds.blit(cursor, (191 + (18 * len(b3Contents)), 136))
            elif selectedBox == 3 and len(b3Contents) == 15:
                ds.blit(cursor2, (191 + (18 * len(b3Contents)), 136))

        drawChars((191, 64), b1Contents)
        drawChars((191, 100), b2Contents)
        drawChars((191, 136), b3Contents)
        drawChars((144, 208), answer)

        pygame.display.update()

        if cursorBlinking:
            cursorBlinkCount += 1

        clock.tick(fps)


if __name__ == '__main__':
    print("PLEASE RUN MAIN.PY")
