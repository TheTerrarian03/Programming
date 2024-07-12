# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window


def printName(event):
    print("Chello my name is Bucky")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName) # parameters: event, function.
button_1.pack()

root.mainloop() # To keep it there until you exit it out. Constantly displays it.