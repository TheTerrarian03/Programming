from tkinter import *
import tkinter.messagebox
import time

def create_win():

    root = Tk()
    root.title("UC_TEST")

    def check():
        b = b_entry.get()
        c_unfloated = c_entry.get()
        d = d_entry.get()

        def clear_all():
            b_entry.delete(0, END)
            c_entry.delete(0, END)
            d_entry.delete(0, END)
            answer_entry.delete(0, END)

        if len(c_entry.get()) == 0:
            c_unfloated = 1
            c_entry.insert(0, "1")

        try:
            c = float(c_unfloated)
        except ValueError:
            tkinter.messagebox.showinfo("ERROR", "BAD")
            clear_all()

        try:
            if b == 'mm' and d == 'mm':
                answer = c
            if b == 'mm' and d == 'cm':
                answer = c / 10
            if b == 'mm' and d == 'm':
                answer = c / 1000
            if b == 'mm' and d == 'km':
                answer = c / 1000000
            if b == 'mm' and d == 'inches':
                answer = c / 25.4
            if b == 'mm' and d == 'feet':
                answer = c / 304.8
            if b == 'mm' and d == 'yards':
                answer = c / 914.4
            if b == 'mm' and d == 'miles':
                answer = c / 1609344
            if b == 'cm' and d == 'mm':
                answer = c * 10
            if b == 'cm' and d == 'cm':
                answer = c
            if b == 'cm' and d == 'm':
                answer = c / 100
            if b == 'cm' and d == 'km':
                answer = c / 100000
            if b == 'cm' and d == 'inches':
                answer = c / 2.54
            if b == 'cm' and d == 'feet':
                answer = c / 30.48
            if b == 'cm' and d == 'yards':
                answer = c / 91.44
            if b == 'cm' and d == 'miles':
                answer = c / 160934.4
            if b == 'm' and d == 'mm':
                answer = c * 1000
            if b == 'm' and d == 'cm':
                answer = c * 100
            if b == 'm' and d == 'm':
                answer = c
            if b == 'm' and d == 'km':
                answer = c / 1000
            if b == 'm' and d == 'inches':
                answer = c * 39.3701
            if b == 'm' and d == 'feet':
                answer = c * 3.28084
            if b == 'm' and d == 'yards':
                answer = c * 1.094
            if b == 'm' and d == 'miles':
                answer = c / 1609
            if b == 'km' and d == 'mm':
                answer = c * 1000000
            if b == 'km' and d == 'cm':
                answer = c * 100000
            if b == 'km' and d == 'm':
                answer = c * 1000
            if b == 'km' and d == 'km':
                answer = c
            if b == 'km' and d == 'inches':
                answer = c * 39370.1
            if b == 'km' and d == 'feet':
                answer = c * 3281
            if b == 'km' and d == 'yards':
                answer = c * 1094
            if b == 'km' and d == 'miles':
                answer = c / 1.609
            if b == 'inches' and d == 'mm':
                answer = c * 25.4
            if b == 'inches' and d == 'cm':
                answer = c * 2.54
            if b == 'inches' and d == 'm':
                answer = c / 39.37
            if b == 'inches' and d == 'km':
                answer = c / 39370
            if b == 'inches' and d == 'inches':
                answer = c
            if b == 'inches' and d == 'feet':
                answer = c / 12
            if b == 'inches' and d == 'yards':
                answer = c / 36
            if b == 'inches' and d == 'miles':
                answer = c / 63360
            if b == 'feet' and d == 'mm':
                answer = c * 304.8
            if b == 'feet' and d == 'cm':
                answer = c * 30.48
            if b == 'feet' and d == 'm':
                answer = c / 3.281
            if b == 'feet' and d == 'km':
                answer = c / 3281
            if b == 'feet' and d == 'inches':
                answer = c * 12
            if b == 'feet' and d == 'feet':
                answer = c
            if b == 'feet' and d == 'yards':
                answer = c / 3
            if b == 'feet' and d == 'miles':
                answer = c / 5280
            if b == 'yards' and d == 'mm':
                answer = c * 914.4
            if b == 'yards' and d == 'cm':
                answer = c * 91.44
            if b == 'yards' and d == 'm':
                answer = c / 1.094
            if b == 'yards' and d == 'km':
                answer = c / 1094
            if b == 'yards' and d == 'inches':
                answer = c * 36
            if b == 'yards' and d == 'feet':
                answer = c * 3
            if b == 'yards' and d == 'yards':
                answer = c
            if b == 'yards' and d == 'miles':
                answer = c / 1760
            if b == 'miles' and d == 'mm':
                answer = c * 1609344
            if b == 'miles' and d == 'cm':
                answer = c * 160934.4
            if b == 'miles' and d == 'm':
                answer = c / 1609.344
            if b == 'miles' and d == 'km':
                answer = c / 1.609344
            if b == 'miles' and d == 'inches':
                answer = c * 63360
            if b == 'miles' and d == 'feet':
                answer = c * 5280
            if b == 'miles' and d == 'yards':
                answer = c * 1760
            if b == 'miles' and d == 'miles':
                answer = c
        except UnboundLocalError:
            tkinter.messagebox.showinfo("ERROR", "You may try again.")

        def clear_text():
            answer_entry.delete(0, END)

        clear_text()
        answer_entry.insert(0, str(answer) + d)

    b_entry = Entry(root, width=30)
    c_entry = Entry(root, width=30)
    d_entry = Entry(root, width=30)
    start_button = Button(root, text="Check", command=check, width=25)
    answer_entry = Entry(root, width=30)

    b_entry.grid()
    c_entry.grid(row=1)
    d_entry.grid(row=2)
    start_button.grid(row=3)
    answer_entry.grid(row=4)

    answer_entry.insert(0, "       Answer will appear here")

    root.mainloop()


create_win()
