# Window built using Tkinter

from tkinter import *

root = Tk() #creating a blank window : root = blank window

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root) # Give me a blank field. (Where)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) # Where? (row=#, column=#, sticky=(N,S,E,W for North, South, East, West))
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in") # Make checkbox in variable c (True or False)
c.grid(columnspan=2) # puts is in two cells

root.mainloop() # To keep it there until you exit it out. Constantly displays it.