# Note: Add some features such as Bug Test Averaging and more menu asthetics.
# Add time.sleep functions to spin() to add a more realistic spin. [ time.sleep(3) ] and when viewing bugs.
# finish spin() --> spun_result() --> removeBug()

# bug1 is a square, purple, small bug.
# bug2 is a circle, blue, big bug.
# bug3 is a circle, orange, big bug.
# bug4 is a triangle, red, small bug.
# bug5 is a triangle, green, small bug.
# bug6 is a square, yellow, big bug.

import random
import time

bug1 = 1
bug2 = 1
bug3 = 1
bug4 = 1
bug5 = 1
bug6 = 1
sbug1 = 0
sbug2 = 0
sbug3 = 0
x = 0


def neccessaryStartFunction():
    global bugAssetToSpinFor
    print("")
    print("Welcome To The Bug-In-A-Rug Game!")
    print("Made by Logan")
    print("Would you like to spin for shapes, colors, or size?")
    bugAssetToSpinFor = input("No capitalization: ")
    if bugAssetToSpinFor == "shapes" or bugAssetToSpinFor == "colors" or bugAssetToSpinFor == "size":
        print("Ok then,", bugAssetToSpinFor, "it is.")
        print("")

        b1 = bug1
        b2 = bug2
        b3 = bug3
        b4 = bug4
        b5 = bug5
        b6 = bug6

        sb1 = sbug1
        sb2 = sbug2
        sb3 = sbug3

        go(b1, b2, b3, b4, b5, b6, sb1, sb2, sb3, bugAssetToSpinFor)
    else:
        print("Please try again...")
        time.sleep(.5)
        neccessaryStartFunction()


def go(b1, b2, b3 ,b4, b5, b6, sb1, sb2, sb3, bugAssetToSpinFor):
    # here is the options section, at the start of func on purpose...
    whichBugToRemove = input("Which bug would you like to remove? ")
    print("bug", whichBugToRemove, "will be removed")
    time.sleep(1)
    print("Done")
    if whichBugToRemove == 1 and b1 != 0:
        bug1 = b1 - 1
        print(bug1)


'''
b1 = bug1
b2 = bug2
b3 = bug3
b4 = bug4
b5 = bug5
b6 = bug6
sb1 = sbug1
sb2 = sbug2
sb3 = sbug3
go(b1, b2, b3, b4, b5, b6, sb1, sb2, sb3)
'''

neccessaryStartFunction()
