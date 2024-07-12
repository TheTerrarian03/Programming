from tkinter import *
import v
import game


def main():
    win = Tk()
    win.title(v.name)

    def go():
        game.main(resX=oneE.get(), resY=twoE.get())

    def goF():
        game.main(fs=True)

    one = Label(win, text="Welcome to " + v.name + "!")
    two = Label(win, text="Please enter a resolution:")
    three = Label(win, text="Width:")
    four = Label(win, text="Height:")
    oneE = Entry(win)
    twoE = Entry(win)
    oneB = Button(win, text="GO!", command=go)
    twoB = Button(win, text="Or go full screen!", command=goF)

    one.grid(columnspan=2)
    two.grid(row=1, columnspan=2)
    three.grid(row=2)
    four.grid(row=3)
    oneE.grid(row=2, column=1)
    twoE.grid(row=3, column=1)
    oneB.grid(row=4, columnspan=2)
    twoB.grid(row=5, columnspan=2)

    oneE.insert(0, "1600")
    twoE.insert(0, "900")

    mainloop()
