# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X) # We wont to fill it as long as the x value is.
three = Label(root, text="three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) # We wont to fill it as long as the y value is.

root.mainloop() # To keep it there until you exit it out. Constantly displays it.