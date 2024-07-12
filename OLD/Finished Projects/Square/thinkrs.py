from tkinter import *
import time


def res(old):
    if old == 1:
        return 800, 450
    elif old == 2:
        return 1080, 720
    elif old == 3:
        return 1600, 900


def size(old):
    if old == 1:
        return 50
    elif old == 2:
        return 100
    elif old == 3:
        return 150


def error():
    errorWin = Tk()
    errorWin.title("ERROR")

    def close():
        errorWin.destroy()
        return "\"errorWin\" has been closed"

    infoBox1 = Label(errorWin, text="An error occurred")
    butt = Button(errorWin, text="Acknowledged. Close Window", command=close)

    infoBox1.pack()
    butt.pack(side=BOTTOM)

    errorWin.mainloop()
