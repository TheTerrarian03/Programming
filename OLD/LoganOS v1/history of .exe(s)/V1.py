from tkinter import *
import tkinter.messagebox


main_win = Tk()
main_win.title("LoganOS, v1")


# temporary functions
def af():
    tkinter.messagebox.showinfo("Add Folder", "Adding Folder...")


def ai():
    tkinter.messagebox.showinfo("Add Image", "Adding Image...")


def ap():
    tkinter.messagebox.showinfo("Add Program", "Adding Program...")


main_win_menu = Menu(main_win)
main_win.config(menu=main_win_menu)
add_menu = Menu(main_win_menu)
add_menu.add_command(label="Add Folder...", command=af)
add_menu.add_command(label="Add Image...", command=ai)
add_menu.add_command(label="Add Program...", command=ap)
main_win_menu.add_cascade(label="Add...", menu=add_menu)

main_win.mainloop()
