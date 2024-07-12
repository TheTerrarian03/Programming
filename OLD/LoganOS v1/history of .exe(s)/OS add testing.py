from tkinter import *
import tkinter.messagebox


main = Tk()
main.title("Hello There!")


def create():
    class ObC:
        def __init__(self, name, active_yn, r, c):
            self.name_p = name
            self.active_yn = active_yn
            self.r = r
            self.c = c

            def place():
                self.name_o = Label(main)
                self.grid(row=self.r + 3, column=self.c)

    ob1cname = ObC(ob1ent.get(), True, 0, 0)
    ob2cname = ObC(ob2ent.get(), True, 0, 1)


ob1lab = Label(main, text="Object 1")
ob2lab = Label(main, text="Object 2")
ob1ent = Entry(main)
ob2ent = Entry(main)
ob1go = Button(main, text="Create", command=create)
ob2go = Button(main, text="Create", command=create)
ob1lab.grid()
ob1ent.grid(row=1)
ob1go.grid(row=2)
ob2lab.grid(row=0, column=1)
ob2ent.grid(row=1, column=1)
ob2go.grid(row=2, column=1)

main.mainloop()
