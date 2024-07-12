import pygame
import v


win = pygame.display.set_mode((200, 200))
pygame.display.set_caption("File Explorer From Scratch")

while v.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False

    pygame.draw.rect(win, (255, 255, 255), (50, 50, 50, 50))
    pygame.display.update()
