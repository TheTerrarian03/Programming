# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window

def leftClick(event):
    print("Left")


def middleClick(event):
    print("Middle")


def rightClick(event):
    print("Right")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop() # To keep it there until you exit it out. Constantly displays it.