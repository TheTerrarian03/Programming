import turtle
import time
import random


def commands():
    print("turtle.getscreen()")
    spc()
    print("turtle.bgcolor(color_as_string)")
    spc()
    print("turtle.title(titlestring)")
    spc()
    print(".circle(radius)")
    spc()
    print(".goto(posx, posy)")
    spc()
    print(".home()")
    spc()
    print(".pencolor(color_as_string)")
    spc()
    print(".fillcolor(color_as_string)")
    spc()
    print(".shapesize(stretch_length, strech_width, outline_width)")
    spc()
    print(".circle(radius)")
    spc()
    print(".dot(radius)")
    spc()
    print(".shape(shape_as_string)")
    print("square, arrow, circle, turtle, triangle, and classic")
    spc()
    print(".speed(speed)")
    spc()
    print(".pen(pencolor_as_string, fillcolor_as_string, pensize, speed)")
    spc()
    print(".penup()")
    spc()
    print(".pendown()")
    spc()
    print(".begin_fill()")
    print(".end_fill()")
    spc()
    print(".undo()")
    spc()
    print(".clear()")
    spc()
    print(".stamp() ... IDK")


def spc():
    print("")


turtle.title("My Awesome Turtle Program I Made!")
turtle.bgcolor("orange")
logan = turtle.Turtle()
logan.color("black", "red")
logan.speed(100)

for radius in range(150):
    logan.goto(0, 0 - radius)
    logan.begin_fill()
    logan.circle(radius)
    logan.end_fill()

time.sleep(1)

logan.speed(5)
logan.penup()
logan.home()
logan.pendown()
logan.goto(radius, 0)
logan.home()
logan.goto(0, radius)
logan.home()
logan.goto(-(radius), 0)
logan.home()
logan.goto(0, -(radius))
logan.home()
