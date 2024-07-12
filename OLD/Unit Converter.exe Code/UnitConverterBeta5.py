from tkinter import *
import tkinter.messagebox


def open_window():
    def quit_exit():
        tkinter.messagebox.showinfo("Exiting Program", "Exiting Unit Converter.exe...")
        quit()

    intro_win = Tk()
    intro_win.title("Unit Converter.exe --/-- Made By Logan S. Meyers")

    # create frames
    frame1 = Frame(intro_win)
    frame2 = Frame(intro_win)
    frame3 = Frame(intro_win)
    frame4 = Frame(intro_win)
    frame5 = Frame(intro_win)

    # frame packing
    frame1.pack(side=TOP)
    frame2.pack(side=TOP)
    frame3.pack(side=TOP)
    frame4.pack(side=TOP)
    frame5.pack(side=TOP)

    # messages in frames
    welcome = Label(frame1, text="Welcome to my Unit Converter/Number information program!")
    mess_up = Label(frame2, text="If you mess up, you will see an error message..."
                                 "\nand have to explain why you think you messed up. :)")
    start_msg = Label(frame3, text="You may click the \"Start\" button to start.")
    intro_separator = Label(frame4, text="--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--/--")
    close_now = Label(frame5, text="You can close this window at any time.")

    # messages packing
    welcome.pack(padx=5, pady=1)
    mess_up.pack(padx=5, pady=1)
    start_msg.pack(padx=5, pady=1)
    intro_separator.pack(padx=5, pady=1)
    close_now.pack(padx=5, pady=1)

    intro_win.mainloop()

    giant_convert_win = Tk()
    giant_convert_win.title("Giant convert Window /--/ Unit Converter.exe")

    intro_win.mainloop()

    def sep_func(sep_row_start, sep_column_start, height):
        # loop
        for loop_time in range(height):
            row_num = sep_row_start + loop_time
            separator = Label(giant_convert_win, text="/--/")
            separator.grid(row=row_num, column=sep_column_start)

    def distance_area_making():
        def dist_help():
            tkinter.messagebox.showinfo("Help / Distance", "Boxes labeled \"Unit\" take a unit such as:"
                                                           "\n\nmm, cm, m, km, inches, feet, yards, miles,"
                                                           " or ly.\n\n\"ly\" stnds for \"lightyears.\""
                                                           "\nYes, I included lightyears.\n:D")

        def check():
            b = dist_b_entry.get()
            c_unfloated = dist_c_entry.get()
            d = dist_d_entry.get()

            def clear_all():
                dist_b_entry.delete(0, END)
                dist_c_entry.delete(0, END)
                dist_d_entry.delete(0, END)
                dist_answer_entry.delete(0, END)

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
                dist_answer_entry.delete(0, END)

            clear_text()
            dist_answer_entry.insert(0, str(answer) + d)

        # title creating
        dist_title = Label(giant_convert_win, text="Distance Converter")

        # guide labels
        dist_guide1 = Label(giant_convert_win, text="Unit   -->")
        dist_guide2 = Label(giant_convert_win, text="Number -->")
        dist_guide3 = Label(giant_convert_win, text="Unit   -->")

        # entry fields creating
        dist_b_entry = Entry(giant_convert_win)
        dist_c_entry = Entry(giant_convert_win)
        dist_d_entry = Entry(giant_convert_win)

        # check box and help creating
        dist_check_button = Button(giant_convert_win, text="Check", command=check, width=10)
        dist_help_button = Button(giant_convert_win, text="Help", command=dist_help, width=10)

        # answer entry field creating
        dist_answer_entry = Entry(giant_convert_win, width=35)

        # packing... I mean grid
        dist_title.grid(row=0, column=0, columnspan=2)
        dist_guide1.grid(row=1, column=0)
        dist_guide2.grid(row=2, column=0)
        dist_guide3.grid(row=3, column=0)
        dist_b_entry.grid(row=1, column=1)
        dist_c_entry.grid(row=2, column=1)
        dist_d_entry.grid(row=3, column=1)
        dist_check_button.grid(row=4, column=0)
        dist_help_button.grid(row=4, column=1)
        dist_answer_entry.grid(row=5, column=0, columnspan=2)

    def temp_area_making():
        def temp_help():
            tkinter.messagebox.showinfo("Help / Temperature", "Boxes labeled \"Unit\" take a unit such as:"
                                                              "\n\nc, f, or k"
                                                              "\n\nthey stand for temperature measurements.")

        def check():
            f = temp_f_entry.get()
            g_unfloated = temp_g_entry.get()
            h = temp_h_entry.get()

            def clear_all():
                temp_f_entry.delete(0, END)
                temp_g_entry.delete(0, END)
                temp_h_entry.delete(0, END)
                temp_answer_entry.delete(0, END)

            try:
                g = float(g_unfloated)
            except ValueError:
                tkinter.messagebox.showinfo("ERROR", "BAD")
                clear_all()

            try:
                if f == "c" and h == "c":
                    answer = g
                if f == "c" and h == "f":
                    answer = (g * 9 / 5) + 32
                if f == "c" and h == "k":
                    answer = g + 273.15
                if f == "f" and h == "c":
                    answer = (g - 32) * 5 / 9
                if f == "f" and h == "f":
                    answer = g
                if f == "f" and h == "k":
                    answer = ((g - 32) * 5 / 9) + 273.15
                if f == "k" and h == "c":
                    answer = g - 273.15
                if f == "k" and h == "f":
                    answer = ((g - 273.15) * 9 / 5) + 32
                if f == "k" and h == "k":
                    answer = g
            except UnboundLocalError:
                tkinter.messagebox.showinfo("ERROR", "You may try again.")

            def clear_text():
                temp_answer_entry.delete(0, END)

            clear_text()
            temp_answer_entry.insert(0, str(answer) + h)

        # title creating
        temp_title = Label(giant_convert_win, text="Temperature Converter")

        # guide labels
        temp_guide1 = Label(giant_convert_win, text="Unit   -->")
        temp_guide2 = Label(giant_convert_win, text="Number -->")
        temp_guide3 = Label(giant_convert_win, text="Unit   -->")

        # entry fields creating
        temp_f_entry = Entry(giant_convert_win)
        temp_g_entry = Entry(giant_convert_win)
        temp_h_entry = Entry(giant_convert_win)

        # check box and help creating
        temp_check_button = Button(giant_convert_win, text="Check", command=check)
        temp_help_button = Button(giant_convert_win, text="Help", command=temp_help)

        # answer entry field creating
        temp_answer_entry = Entry(giant_convert_win, width=35)

        # placing
        temp_title.grid(row=0, column=3, columnspan=2)
        temp_guide1.grid(row=1, column=3)
        temp_guide2.grid(row=2, column=3)
        temp_guide3.grid(row=3, column=3)
        temp_f_entry.grid(row=1, column=4)
        temp_g_entry.grid(row=2, column=4)
        temp_h_entry.grid(row=3, column=4)
        temp_check_button.grid(row=4, column=3)
        temp_help_button.grid(row=4, column=4)
        temp_answer_entry.grid(row=5, column=3, columnspan=2)

    distance_area_making()
    sep_func(0, 2, 6)
    temp_area_making()
    sep_func(0, 5, 6)

    giant_convert_win.mainloop()


open_window()
