import time
import sys


def spc():
    print("")


def options_for_user():
    spc()
    time.sleep(0.5)
    print("Welcome to my interactive Turtle Controller!")
    print("We will go through things slowly, at your pace.")
    # print("First, let's name your turtle:")
    # t_name = input("What is their name? ")
    print("Okay, let's go through the options you have at each turn:")
    time.sleep(1)
    spc()
    print("'r' is for restart, to restart the whole program.")
    time.sleep(1)
    spc()
    print("Writing 'forward()' will move the turtle forwards.")
    print("Writing 'backward()' will move the turtle backwards.")
    print("Inside the parenthesis, put the number of pixels you want him to move.")
    time.sleep(1)
    spc()
    print("Writing 'right()' will turn the turtle right.")
    print("Writing 'left()' will turn the turtle left.")
    print("Inside the parenthesis, put the number of degrees you want the turtle to turn.")
    time.sleep(1)
    spc()
    print("For now, let's stick with the basics of Turtle.")
    print("In future versions of this program, there will be functions to change colors and thicknesses.")
    time.sleep(1)


def options_loop():
    spc()
    print("To start, we need a screen.")
    time.sleep(0.5)
    print("Type 'getscreen(")


def beginning():
    print("Welcome to my interactive Turtle Controller!")
    print("We will go through things slowly, at your pace.")
    # print("First, let's name your turtle:")
    # t_name = input("What is their name? ")
    print("Okay, let's go through the options you have at each turn:")
    time.sleep(1)
    spc()
    print("'r' is for restart, to restart the whole program.")
    time.sleep(1)
    spc()
    print("Writing 'forward()' will move the turtle forwards.")
    print("Writing 'backward()' will move the turtle backwards.")
    print("Inside the parenthesis, put the number of pixels you want him to move.")
    time.sleep(1)
    spc()
    print("Writing 'right()' will turn the turtle right.")
    print("Writing 'left()' will turn the turtle left.")
    print("Inside the parenthesis, put the number of degrees you want the turtle to turn.")
    time.sleep(1)
    spc()
    print("For now, let's stick with the basics of Turtle.")
    print("In future versions of this program, there will be functions to change colors and thicknesses.")
    time.sleep(1)
    spc()
    ready_or_not = input("Are you ready to move on to the actual programming? (y/n): ")
    if ready_or_not.lower() == "y":
        spc()
        print("Okay, here we go!")
        options_loop()
    else:
        spc()
        print("Okay, exiting program.")
        time.sleep(1)
        sys.exit()

beginning()