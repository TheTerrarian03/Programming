import pygame
import processors
import messages


pygame.init()


def main():
    ds = pygame.display.set_mode((590, 301))
    pygame.display.set_caption("Unit Converter - Option 1: Distance Converter")

    clock = pygame.time.Clock()
    fps = 30

    bg = pygame.image.load("option1.png")
    cursor = pygame.image.load("cursor.png")
    cursor2 = pygame.image.load("cursor2.png")

    cursorBlinkCount = 15
    cursorBlinking = False
    selectedBox = 0

    b1Contents = []
    b2Contents = []
    b3Contents = []
    answer = []

    lyList1 = ['l', 'i', 'g', 'h', 't', '-', 'y', 'e', 'a', 'r', 's']
    lyList2 = ['l', 'i', 'g', 'h', 't', 'y', 'e', 'a', 'r', 's']
    lyList3 = ["l", "y"]

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
                    if event.key == pygame.K_a:
                        b1Contents.append("a")
                    if event.key == pygame.K_b:
                        b1Contents.append("b")
                    if event.key == pygame.K_c:
                        b1Contents.append("c")
                    if event.key == pygame.K_d:
                        b1Contents.append("d")
                    if event.key == pygame.K_e:
                        b1Contents.append("e")
                    if event.key == pygame.K_f:
                        b1Contents.append("f")
                    if event.key == pygame.K_g:
                        b1Contents.append("g")
                    if event.key == pygame.K_h:
                        b1Contents.append("h")
                    if event.key == pygame.K_i:
                        b1Contents.append("i")
                    if event.key == pygame.K_j:
                        b1Contents.append("j")
                    if event.key == pygame.K_k:
                        b1Contents.append("k")
                    if event.key == pygame.K_l:
                        b1Contents.append("l")
                    if event.key == pygame.K_m:
                        b1Contents.append("m")
                    if event.key == pygame.K_n:
                        b1Contents.append("n")
                    if event.key == pygame.K_o:
                        b1Contents.append("o")
                    if event.key == pygame.K_p:
                        b1Contents.append("p")
                    if event.key == pygame.K_q:
                        b1Contents.append("q")
                    if event.key == pygame.K_r:
                        b1Contents.append("r")
                    if event.key == pygame.K_s:
                        b1Contents.append("s")
                    if event.key == pygame.K_t:
                        b1Contents.append("t")
                    if event.key == pygame.K_u:
                        b1Contents.append("u")
                    if event.key == pygame.K_v:
                        b1Contents.append("v")
                    if event.key == pygame.K_w:
                        b1Contents.append("w")
                    if event.key == pygame.K_x:
                        b1Contents.append("x")
                    if event.key == pygame.K_y:
                        b1Contents.append("y")
                    if event.key == pygame.K_z:
                        b1Contents.append("z")
                    if event.key == pygame.K_MINUS:
                        b1Contents.append("-")
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
                    if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                        b2Contents.append(".")
                    if event.key == pygame.K_BACKSPACE:
                        try:
                            b2Contents.pop()
                        except IndexError:
                            pass
                    if event.key == pygame.K_DELETE:
                        b2Contents.clear()
                if selectedBox == 3:
                    if event.key == pygame.K_a:
                        b3Contents.append("a")
                    if event.key == pygame.K_b:
                        b3Contents.append("b")
                    if event.key == pygame.K_c:
                        b3Contents.append("c")
                    if event.key == pygame.K_d:
                        b3Contents.append("d")
                    if event.key == pygame.K_e:
                        b3Contents.append("e")
                    if event.key == pygame.K_f:
                        b3Contents.append("f")
                    if event.key == pygame.K_g:
                        b3Contents.append("g")
                    if event.key == pygame.K_h:
                        b3Contents.append("h")
                    if event.key == pygame.K_i:
                        b3Contents.append("i")
                    if event.key == pygame.K_j:
                        b3Contents.append("j")
                    if event.key == pygame.K_k:
                        b3Contents.append("k")
                    if event.key == pygame.K_l:
                        b3Contents.append("l")
                    if event.key == pygame.K_m:
                        b3Contents.append("m")
                    if event.key == pygame.K_n:
                        b3Contents.append("n")
                    if event.key == pygame.K_o:
                        b3Contents.append("o")
                    if event.key == pygame.K_p:
                        b3Contents.append("p")
                    if event.key == pygame.K_q:
                        b3Contents.append("q")
                    if event.key == pygame.K_r:
                        b3Contents.append("r")
                    if event.key == pygame.K_s:
                        b3Contents.append("s")
                    if event.key == pygame.K_t:
                        b3Contents.append("t")
                    if event.key == pygame.K_u:
                        b3Contents.append("u")
                    if event.key == pygame.K_v:
                        b3Contents.append("v")
                    if event.key == pygame.K_w:
                        b3Contents.append("w")
                    if event.key == pygame.K_x:
                        b3Contents.append("x")
                    if event.key == pygame.K_y:
                        b3Contents.append("y")
                    if event.key == pygame.K_z:
                        b3Contents.append("z")
                    if event.key == pygame.K_MINUS:
                        b3Contents.append("-")
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
                    if (len(b1Contents) and len(b2Contents) and len(b3Contents)) >= 1:
                        answer.clear()
                        if b1Contents == lyList1 or b1Contents == lyList2:
                            b1Contents = lyList3
                        if b3Contents == lyList1 or b3Contents == lyList2:
                            b3Contents = lyList3
                        a = processors.option1(b1Contents, b2Contents, b3Contents)
                        for char in str(a):
                            answer.append(char)
                # HELP! 's
                elif 485 <= event.pos[0] <= 571 and 58 <= event.pos[1] <= 90:
                    messages.option1(1)
                elif 485 <= event.pos[0] <= 571 and 94 <= event.pos[1] <= 126:
                    messages.option1(2)
                elif 485 <= event.pos[0] <= 571 and 130 <= event.pos[1] <= 162:
                    messages.option1(3)
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
