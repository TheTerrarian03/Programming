import pygame
import processors
import messages


def main():
    ds = pygame.display.set_mode((590, 301))
    pygame.display.set_caption("Unit Converter - Option 5: Number Sorter")

    clock = pygame.time.Clock()
    fps = 30

    bg = pygame.image.load("option2.png")
    cursor = pygame.image.load("cursor.png")
    cursor2 = pygame.image.load("cursor2.png")

    cursorBlinkCount = 15
    cursorBlinking = False

    enteredInfo = []
    temp_box = []
    answer = []

    def drawChars(start, toPrint):
        chars = pygame.image.load("chars.png")
        charList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                # << BACK
                if 224 <= event.pos[0] <= 364 and 250 <= event.pos[1] <= 282:
                    return "RETURN_TO_MENU"
                # GO!
                elif 256 <= event.pos[0] <= 333 and 166 <= event.pos[1] <= 198:
                        a = processors.option5(enteredInfo)
                        for char in str(a):
                            answer.append(char)
                # HELP! 's
                elif 485 <= event.pos[0] <= 571 and 58 <= event.pos[1] <= 90:
                    messages.option2(1)
                elif 485 <= event.pos[0] <= 571 and 94 <= event.pos[1] <= 126:
                    messages.option2(2)
                elif 485 <= event.pos[0] <= 571 and 130 <= event.pos[1] <= 162:
                    messages.option2(3)
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
                elif 158 <= event.pos[0] <= 481 and 58 <= event.pos[1] <= 90:
                    cursorBlinking = True
                    selectedBox = 1
                elif 185 <= event.pos[0] <= 481 and 94 <= event.pos[1] <= 126:
                    cursorBlinking = True
                    selectedBox = 2
                elif 185 <= event.pos[0] <= 481 and 130 <= event.pos[1] <= 162:
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

