from tkinter import *
import tkinter.messagebox


def create_choice_window():
    uc = Tk()
    uc.title("Unit Converter.exe --/-- Made by Logan S. Meyers")

    # create frames
    frame1 = Frame(uc)
    frame2 = Frame(uc)
    frame3 = Frame(uc)
    frame4 = Frame(uc)
    frame5 = Frame(uc)
    frame6 = Frame(uc)

    # pack frames
    frame1.pack(side=TOP)
    frame2.pack(side=TOP)
    frame3.pack(side=TOP)
    frame4.pack(side=TOP)
    frame5.pack(side=TOP)
    frame6.pack(side=TOP)

    # welcome messages
    welcome_msg = Label(frame1, text="Welcome to my Unit Converter / Number Information program!")
    welcome_msg2 = Label(frame2, text="If you mess up, you will see an error message"
                                      "\n and have to explain why you messed up :)")
    welcome_msg3 = Label(frame3, text="You may click one of the buttons below to start.")
    welcome_msg4 = Label(frame4, text="--/--/--/--/--/--/--/--/--/--/--/--/--/--/--")

    # welcome messages packing
    welcome_msg.pack(padx=5, pady=1)
    welcome_msg2.pack(padx=5, pady=1)
    welcome_msg3.pack(padx=5, pady=1)
    welcome_msg4.pack(padx=5, pady=1)

    # button creating and binding
    dist_convt_button = Button(frame5, text="Distance Converter", command=create_distance_convert_window)
    temp_convt_button = Button(frame5, text="Temperature Converter", command=create_temperature_convert_window)

    # button packing
    dist_convt_button.pack(side=LEFT, ipadx=15, padx=5)
    temp_convt_button.pack(side=LEFT, ipadx=15, padx=5)

    uc.mainloop()


def create_distance_convert_window():
    uc_dc = Tk()
    uc_dc.title("Distance Converter / Unit Converter.exe")

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
            if b == 'mm' and d == 'ly':
                answer = c / 9460730472580800000
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
            if b == 'cm' and d == 'ly':
                answer = c / 946073047258080000
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
            if b == 'm' and d == 'ly':
                answer = c / 9460730472580800
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
            if b == 'km' and d == 'ly':
                answer = c / 9460730472580.8
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
            if b == 'inches' and d == 'ly':
                answer = c / 372469703644913408
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
            if b == 'feet' and d == 'ly':
                answer = c / 31039141970409448
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
            if b == 'yards' and d == 'ly':
                answer = c / 10346380656803150
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
            if b == 'miles' and d == 'ly':
                answer = c / 5878625373183.6074219
            if b == 'ly' and d == 'mm':
                answer = c * 9460730472580800000
            if b == 'ly' and d == 'cm':
                answer = c * 946073047258080000
            if b == 'ly' and d == 'm':
                answer = c * 9460730472580800
            if b == 'ly' and d == 'km':
                answer = c * 9460730472580.8
            if b == 'ly' and d == 'inches':
                answer = c * 372469703644913408
            if b == 'ly' and d == 'feet':
                answer = c * 31039141970409448
            if b == 'ly' and d == 'yards':
                answer = c * 10346380656803150
            if b == 'ly' and d == 'miles':
                answer = c * 5878625373183.6074219
            if b == 'ly' and d == 'ly':
                answer = c
        except UnboundLocalError:
            tkinter.messagebox.showinfo("ERROR", "You may try again.")

        def clear_text():
            answer_entry.delete(0, END)

        clear_text()
        answer_entry.insert(0, str(answer) + d)

    # guidance labels creating
    from_label = Label(uc_dc, text="Unit -->")
    from_num_label = Label(uc_dc, text="Number -->")
    to_label = Label(uc_dc, text="Unit -->")
    unit_label1 = Label(uc_dc, text="<-- mm, cm, m, km, inches, feet, yards, miles, ly (for lightyears)")
    unit_label2 = Label(uc_dc, text="<-- A Number")
    unit_label3 = Label(uc_dc, text="<-- mm, cm, m, km, inches, feet, yards, miles, ly (for lightyears)")
    answer_label = Label(uc_dc, text="Answer -->")

    # entry fields creating
    b_entry = Entry(uc_dc, width=30)
    c_entry = Entry(uc_dc, width=30)
    d_entry = Entry(uc_dc, width=30)

    # answer entry field creating
    answer_entry = Entry(uc_dc, width=70)

    # Check button creating
    check_button = Button(uc_dc, text="/-- Check --/", command=check)

    # guidance labels, entry fields, and convert button placing (grid)
    from_label.grid(sticky=E)
    b_entry.grid(row=0, column=1)
    unit_label1.grid(row=0, column=2)

    from_num_label.grid(row=1, sticky=E)
    c_entry.grid(row=1, column=1, sticky=E)
    unit_label2.grid(row=1, column=2, sticky=W)

    to_label.grid(row=2, sticky=E)
    d_entry.grid(row=2, column=1, sticky=E)
    unit_label3.grid(row=2, column=2)

    check_button.grid(row=3, columnspan=2)

    answer_label.grid(row=4, column=0)
    answer_entry.grid(row=4, column=1, columnspan=2)

    uc_dc.mainloop()


def create_temperature_convert_window():
    tkinter.messagebox.showinfo("", "Temperature")


create_choice_window()
