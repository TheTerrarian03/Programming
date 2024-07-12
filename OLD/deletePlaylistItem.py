from os import times
import pynput, time

timesDeleted = 0

def deletePlaylistItem(mouseObj):
    print("Current position:", mouseObj.position)
    startPos = mouseObj.position

    print("-- STARTING --")

    print("Pressing down")
    mouseObj.press(pynput.mouse.Button.left)

    print("Moving mouse")
    for _ in range(20):
        mouseObj.move(-10, 0)

    print("UnPressing down")
    mouseObj.release(pynput.mouse.Button.left)

    print("Returning to original position")
    mouse.position = startPos

    print("Pausing for safety")
    time.sleep(0.125)

    print("Pressing down and then releasing")
    mouseObj.press(pynput.mouse.Button.left)
    mouseObj.release(pynput.mouse.Button.left)

    print("Returning to original position")
    mouseObj.position = startPos

    print("-- ENDING --")

    global timesDeleted
    timesDeleted += 1

def kPress(key):
    global running
    if key == pynput.keyboard.Key.space:
        deletePlaylistItem(mouse)
    if key == pynput.keyboard.Key.esc:
        running = False

running = True

mouse = pynput.mouse.Controller()

kListen = pynput.keyboard.Listener(on_press=kPress)
kListen.start()

while running:
    pass

print("Done with the script, exiting")
print("Deleted a playlist item", timesDeleted, "times! :D")
