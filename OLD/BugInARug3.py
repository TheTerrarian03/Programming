# Note: Add some features such as Bug Test Averaging and more menu asthetics.
# Add time.sleep functions to spin() to add a more realistic spin. [ time.sleep(3) ] and when viewing bugs.
# finish spin() --> spun_result() --> removeBug()

# bug1 is a square, purple, small bug.
# bug2 is a circle, blue, big bug.
# bug3 is a circle, orange, big bug.
# bug4 is a triangle, red, small bug.
# bug5 is a triangle, green, small bug.
# bug6 is a square, yellow, big bug.
# Colors: red, orange,  yellow, green, blue, purple
# Shapes: square, circle, triangle
# Eye Sizes: small, med, big

import random
import time
from tkinter import *
import tkinter.messagebox


properties = [["square", "circle", "circle", "triangle", "triangle", "square"]
              ["purple", "blue", "orange", "red", "green", "yellow"]
              ["small", "big", "big", "small", "small", "big"]]


def main():
    class Bug:
        def __init__(self, num):
            for var in range(6):
                self.shape = properties[var][num]

    bug1 = Bug(1)
    bug2 = Bug(2)
    bug3 = Bug(3)
    bug4 = Bug(4)
    bug5 = Bug(5)
    bug6 = Bug(6)

    mainw = Tk()

    mainw.title("Bug in a Rug V3!")
    print(1, bug1.shape, bug1.color, bug1.eye_size)
    print(2, bug2.shape, bug2.color, bug2.eye_size)
    print(3, bug3.shape, bug3.color, bug3.eye_size)
    print(4, bug4.shape, bug4.color, bug4.eye_size)
    print(5, bug5.shape, bug5.color, bug5.eye_size)
    print(6, bug6.shape, bug6.color, bug6.eye_size)
    print(1, sbug1.is_sbug, sbug1.color, sbug1.shape, sbug1.eye_size)
    print(2, sbug2.is_sbug, sbug2.color, sbug2.shape, sbug2.eye_size)

    print(3, sbug3.is_sbug, sbug3.color, sbug3.shape, sbug3.eye_size)


    mainw.mainloop()
def error():
    tkinter.messagebox.showerror("ERROR", "There was an ERROR. Sorry.")




main()
