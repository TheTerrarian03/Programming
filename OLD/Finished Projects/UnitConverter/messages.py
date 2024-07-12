from tkinter import *


def option1(box):
    if box == 1:
        help = Tk()
        help.title("UnitConverter - Option 1: Distance Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the unit you want to convert FROM.\n"
                                 "These units are: \n\n"
                                 "mm, cm, m, km, inches, feet, yards, miles, and also lightyears/light-years/ly.\n\n"
                                 "You may notice you cannot enter numbers. That is for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()
    elif box == 2:
        help = Tk()
        help.title("UnitConverter - Option 1: Distance Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the number of units you want to convert.\n\n"
                                 "You enter a number. \n"
                                 "This can be a whole number or one with decimals.\n\n"
                                 "You may notice you can only enter numbers and decimal points. That is\n"
                                 "for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()
    elif box == 3:
        help = Tk()
        help.title("UnitConverter - Option 1: Distance Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the unit you want to convert TO.\n"
                                 "These units are: \n\n"
                                 "mm, cm, m, km, inches, feet, yards, miles, and also lightyears/light-years.\n\n"
                                 "You may notice you cannot enter numbers. That is for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()


def option2(box):
    if box == 1:
        help = Tk()
        help.title("UnitConverter - Option 2: Temperature Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the unit you want to convert FROM.\n"
                                 "These units are: \n\n"
                                 "f, c, and k. Also known as Fahrenheit, Celcius, and Kelvin.\n\n"
                                 "You may notice you cannot enter numbers. That is for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()
    elif box == 2:
        help = Tk()
        help.title("UnitConverter - Option 2: Temperature Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the number of units you want to convert.\n\n"
                                 "You enter a number. \n"
                                 "This can be a whole number or one with decimals.\n\n"
                                 "You may notice you can only enter numbers and decimal points. That is\n"
                                 "for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()
    elif box == 3:
        help = Tk()
        help.title("UnitConverter - Option 2: Temperature Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the unit you want to convert TO.\n"
                                 "These units are: \n\n"
                                 "f, c, and k. Also known as Fahrenheit, Celcius, and Kelvin.\n\n"
                                 "You may notice you cannot enter numbers. That is for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()


def option3(box):
    if box == 1:
        help = Tk()
        help.title("UnitConverter - Option 3: Time Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the unit you want to convert FROM.\n"
                                 "These units are: \n\n"
                                 "ms, s, m, h, d, w, y, dec., and cent.\n"
                                 "Also known as milliseconds, seconds, minutes, hours, days, weeks,\n"
                                 "years, decades, and centuries.\n\n"
                                 "You may notice you cannot enter numbers. That is for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()
    elif box == 2:
        help = Tk()
        help.title("UnitConverter - Option 3: Time Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the number of units you want to convert.\n\n"
                                 "You enter a number. \n"
                                 "This can be a whole number or one with decimals.\n\n"
                                 "You may notice you can only enter numbers and decimal points. That is\n"
                                 "for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()
    elif box == 3:
        help = Tk()
        help.title("UnitConverter - Option 3: Time Converter - HELP!")

        def close():
            help.destroy()

        iBox1 = Label(help, text="This box is for entering the unit you want to convert TO.\n"
                                 "These units are: \n\n"
                                 "ms, s, m, h, d, w, y, dec., and cent.\n"
                                 "Also known as milliseconds, seconds, minutes, hours, days, weeks,\n"
                                 "years, decades, and centuries.\n\n"
                                 "You may notice you cannot enter numbers. That is for a reason.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        help.mainloop()


def option4():
    help = Tk()
    help.title("UnitConverter - Option 3: Time Converter - HELP!")

    def close():
        help.destroy()

    iBox1 = Label(help, text="This box is for entering the first number.\n\n"
                             "You may notice you cannot enter decimals. That is for a reason.")
    contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

    iBox1.grid()
    contButton.grid(row=1)

    help.mainloop()


def option7(box):
    if box == 1:
        win = Tk()
        win.title("UnitConverter - Option 7: Palindrome Finder - HELP!")

        def close():
            win.destroy()

        iBox1 = Label(help, text="This box is for entering the your palindrome.\n\n"
                                 "This time, you can enter decimals.\n"
                                 "This program finds the next palindrome for you.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        win.mainloop()
    elif box == 2:
        win = Tk()
        win.title("UnitConverter - Option 7: Palindrome Finder - HELP!")

        def close():
            win.destroy()

        iBox1 = Label(help, text="This is the next palindrome in sequence,\n"
                                 "based on what you entered above.")
        contButton = Button(help, text="Ok, Thanks! (Click this to close this window)", command=close)

        iBox1.grid()
        contButton.grid(row=1)

        win.mainloop()


def controls():
    win = Tk()
    win.title("UnitConverter - Controls")

    def close():
        win.destroy()

    iBox1 = Label(win, text="Controls:\n\n"
                            "Use your keyboard to enter data, such as units and numbers.\n"
                            "You can use TAB to go down the list of boxes you can enter data in,\n"
                            "as well as use the DOWN ARROW for that.\n"
                            "UP ARROW goes up in the list of boxes you can enter data in.\n"
                            "Of course, use BACKSPACE to do what BACKSPACE does,\n"
                            "and use DELETE to clear that specific box that you've selected.\n"
                            "You may also click on a box to select it.\n"
                            "Click \"GO!\" to calculate the result,\n"
                            "Click \"CONTROLS\" for this box to pop up again,\n"
                            "Click \"RESET\" to reset all of the boxes,\n"
                            "Click \"<< BACK\" to go back to the menus.\n"
                            "Finally, Click on one of the \"HELP!\" boxes to get help for that specific box.")
    contButton = Button(win, text="Click me to close this window!", command=close)

    iBox1.grid()
    contButton.grid(row=1)

    win.mainloop()


def lcmQMark():
    win = Tk()
    win.title("UnitConverter")

    def close():
        win.destroy()

    iBox1 = Label(win, text="\"LCM\" stands for \"Lowest Common Multiple\".\n\n"
                            "Look it up. :)")
    contButton = Button(win, text="Click me to close this window!", command=close)

    iBox1.grid()
    contButton.grid(row=1)

    win.mainloop()
