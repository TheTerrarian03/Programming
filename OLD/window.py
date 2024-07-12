# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window
theLabel = Label(root, text="this is too easy") # Creating some text (where, text="[what text do you want there?]")
theLabel.pack() # pack = just pack it in there, wherever you can fit it.
root.mainloop() # To keep it there until you exit it out. Constantly displays it.