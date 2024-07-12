import pygame
import variables as v
import thinkrs as t


def main(res):
    v.floorTopY = res[1] - 100
    v.sideSpeed = 0
    v.vertSpeed = 0

    pygame.init()
    game = pygame.display.set_mode(res)
    pygame.display.set_caption("Square - Level 1!")

    v.X = 50
    v.Y = v.floorTopY - v.blockSize

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    v.up_down = True
                if event.key == pygame.K_a:
                    v.a_down = True
                if event.key == pygame.K_d:
                    v.d_down = True
                if event.key == pygame.K_s:
                    v.down_down = True
                if event.key == pygame.K_r:
                    main(res)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    v.up_down = False
                if event.key == pygame.K_a:
                    v.a_down = False
                if event.key == pygame.K_d:
                    v.d_down = False
                if event.key == pygame.K_s:
                    v.down_down = False

        # four-direction movement
        if v.a_down:
            v.sideSpeed -= v.acc
        if v.d_down:
            v.sideSpeed += v.acc
        if v.up_down:
            v.vertSpeed = v.topSpeed
        if v.down_down:
            v.vertSpeed -= v.acc

        # friction/gravity affects
        if not v.a_down and v.sideSpeed < 0:
            v.sideSpeed += 2
        elif not v.d_down and v.sideSpeed > 0:
            v.sideSpeed -= 2
        if v.Y + v.blockSize + 100 < v.floorTopY:
            v.vertSpeed -= v.gravity

        # speed monitoring
        # horizontal
        if v.sideSpeed > v.topSpeed:
            v.sideSpeed = v.topSpeed
        elif v.sideSpeed < -v.topSpeed:
            v.sideSpeed = -v.topSpeed
        # vertical
        if v.vertSpeed > v.topSpeed:
            v.vertSpeed = v.topSpeed
        elif v.vertSpeed < -v.topSpeed:
            v.vertSpeed = -v.topSpeed

        # variable changing
        v.X += v.sideSpeed
        v.Y -= v.vertSpeed

        # boundary monitoring
        if v.X <= 0:
            v.sideSpeed = -v.sideSpeed
            v.X = 0
        elif v.X + v.blockSize >= v.resX:
            v.sideSpeed = -v.sideSpeed
            v.X = v.resX - v.blockSize
        if v.Y <= 0:
            v.vertSpeed = -v.vertSpeed
            v.Y = 0
        elif v.Y + v.blockSize + 100 >= v.resY:
            v.vertSpeed = 0
            v.Y = v.resY - v.blockSize - 100

        game.fill(v.colors["blueLight"])
        game.blit(v.floor, (0, v.floorTopY))
        game.blit(v.s, (v.X, v.Y))

        pygame.display.update()

        v.clock.tick(v.fps)
