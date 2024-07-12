# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window


def printName():
    print("Chello my name is Bucky")

button_1 = Button(root, text="Print my name", command=printName) # command makes the button do a certain function. DONT HAVE THE EXTRA PARAMETER PARETHESIS FOR THE FUNCTION
button_1.pack()

root.mainloop() # To keep it there until you exit it out. Constantly displays it.