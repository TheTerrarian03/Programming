import pygame


list = []

totalCount = 1
running = True

r = 0
g = 0
b = 0

while running:
    b = totalCount
    while True:
        if b > 255:
            b -= 255
            g += 1
        else:
            break
    while True:
        if g > 255:
            g -= 255
            r += 1
        else:
            break

    list.append([r, g, b])
    print(r, g, b)

    if r == 255 and g == 255 and b == 255:
        break

    totalCount += 1

    r = 0
    g = 0
    b = 0
