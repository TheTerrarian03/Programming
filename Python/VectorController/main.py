import anki_vector, time, pygame
import classes as cs
from PIL import Image


args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial, enable_nav_map_feed=True) as robot:
    # nav map experimental function
    def navMapWriteData(navMap):
        f = open("VectorNavMapData.txt", "w")

        dataMap = []

        for y in range(642):
            row = []
            for x in range(642):
                row.append(navMap.get_content(y-321, x-321))
            dataMap.append(row)
        
        # print(dataMap)
        f.write(str(dataMap))
        f.close()
        return dataMap
    
    gui = cs.GUI("Anki Vector Dashboard - LM", res=[800, 600])

    keys = {
        "Forward":   cs.keyboardKey(pygame.K_w, (50,  gui.res[1]-100), (50, 50), additionalValue=100),
        "Left":      cs.keyboardKey(pygame.K_a, (0,   gui.res[1]-50),  (50, 50), additionalValue=100),
        "Backward":  cs.keyboardKey(pygame.K_s, (50,  gui.res[1]-50),  (50, 50), additionalValue=100),
        "Right":     cs.keyboardKey(pygame.K_d, (100, gui.res[1]-50),  (50, 50), additionalValue=100),

        "Lift Up":   cs.keyboardKey(pygame.K_r, (150, gui.res[1]-100), (50, 50), additionalValue=2),
        "Lift Down": cs.keyboardKey(pygame.K_f, (150, gui.res[1]-50),  (50, 50), additionalValue=2),

        "Head Up":   cs.keyboardKey(pygame.K_t, (200, gui.res[1]-100), (50, 50), additionalValue=2),
        "Head Down": cs.keyboardKey(pygame.K_g, (200, gui.res[1]-50),  (50, 50), additionalValue=2),
    }

    running = True

    while running:
        ### keys
        for event in pygame.event.get():
            # quit window
            if event.type == pygame.QUIT:
                running = False
            # key presses
            if event.type == pygame.KEYDOWN:
                for key in keys:
                    keys[key].eventPressed(event.key)
                if event.key == pygame.K_SPACE:
                    navMapWriteData(robot.nav_map.latest_nav_map)
            if event.type == pygame.KEYUP:
                for key in keys:
                    keys[key].eventReleased(event.key)
        
        ### graphics
        gui.draw()

        for key in keys:
            keys[key].draw(gui.display)
        
        gui.updateDisplay()

        ### moving Vector
        ## calculating
        # wheels
        wheels = [0, 0]
        wheels[0] += (keys["Forward"].getValue() - keys["Backward"].getValue())  # straight left
        wheels[1] += (keys["Forward"].getValue() - keys["Backward"].getValue())  # straight right
        
        wheels[0] += (-keys["Left"].getValue() + keys["Right"].getValue())  # left turning
        wheels[1] += (keys["Left"].getValue() - keys["Right"].getValue())  # right turning
        # lift
        lift = 0
        lift += (keys["Lift Up"].getValue() - keys["Lift Down"].getValue())
        # head
        head = 0
        head += (keys["Head Up"].getValue() - keys["Head Down"].getValue())

        print(wheels, lift, head)

        ## setting movement
        robot.motors.set_wheel_motors(wheels[0], wheels[1])
        robot.motors.set_lift_motor(lift)
        robot.motors.set_head_motor(head)

        """### experimental
        latest_nav_map = robot.nav_map.latest_nav_map
        content = latest_nav_map.get_content(0, 100)
        print(content)"""

    robot.disconnect()