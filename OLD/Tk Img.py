from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox

root = Tk()
root.title("Images Example")
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("super_mario_plumber_new.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)

root.mainloop()
