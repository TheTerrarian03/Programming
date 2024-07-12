import pygame


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("rotateImage2")

clock = pygame.time.Clock()
fps = 30


def returnNewImage(originalList):
    image1 = originalList
    list = []
    list2 = []
    list3 = []

    for item1 in range(len(image1)):
        for item2 in image1[item1]:
            list.append(item2)

    print(list)

    for i in range(-1, len(list) - 1):
        list2.append(list[i])

    print(list2)

    x = 0
    for i in range(len(image1)):
        temp_list = []
        for i2 in range(len(image1[0])):
            temp_list.append(list2[x])
            x += 1
        list3.append(temp_list)

    return(list3)


running = True
pictureContent = [[(255, 0, 0), (62, 255, 0), (243, 140, 140), ()],
                 [[(), (), (), ()],
                 [[(), (), (), ()],
                 [[(), (), (), ()]]
scaleInt = 50
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        """if event.type == pygame.MOUSEBUTTONDOWN:
            pictureContent = returnNewImage(pictureContent)"""
        pictureContent = returnNewImage((pictureContent))

        x = 0
        y = 0
        for i1 in range(len(pictureContent)):
            for i2 in range(len(pictureContent[i1])):
                pygame.draw.rect(win, pictureContent[i1][i2], (x, y, scaleInt, scaleInt))
                x += scaleInt
            x = 0
            y += scaleInt
        pygame.display.update()

        # clock.tick(fps)

pygame.quit()
quit()
