# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window

topFrame = Frame(root) # Make an invisible container, going in the main root
topFrame.pack() # Place it somewhere in our main program
bottomFrame = Frame(root) # Make an invisible container, going in the main root
bottomFrame.pack(side=BOTTOM) # side=BOTTOM means it goes on the bottom

button1 = Button(topFrame, text="Button 1", fg="red") # parameters: (which frame?, What is on the button?, fg="(what color?)") fg is optional
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT) # parameter: (where?)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM) # Doesn't matter because it's the only button/widget in the bottom Frame

root.mainloop() # To keep it there until you exit it out. Constantly displays it.