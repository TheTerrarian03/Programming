from tkinter import *
import tkinter.messagebox


def doNothing():
    print("ok ok I won't...")


def is_sky_blue_question_popup():
    is_sky_blue = tkinter.messagebox.askquestion("Question:", "Is the sky blue?")
    if is_sky_blue == "yes":
        tkinter.messagebox.showinfo("Grade", "Correct!")
    elif is_sky_blue == "no":
        while is_sky_blue == "no":
            try_again_q_1 = tkinter.messagebox.askquestion("Grade", "Incorrect! Try again?")
            if try_again_q_1 == "yes":
                is_sky_blue = tkinter.messagebox.askquestion("Question:", "Is the sky blue?")
                if is_sky_blue == "yes":
                    tkinter.messagebox.showinfo("Grade", "Correct!")
            elif try_again_q_1 == "no":
                tkinter.messagebox.showinfo("Try Again?", "Ok.")
                is_sky_blue = "yes"


root = Tk()  # root = blank window

# The main menu

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=is_sky_blue_question_popup)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# The toolbar section

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X) # side=TOP means it goes below the menu

# The status bar section

status = Label(root, text="Preparing to do Nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.title("This is my ROOT Window!")
root.mainloop()

# where.geometry("") with dim as #x# for win size default.
# tkinter.messagebox.askquestion(title, yes_or_no_question) # you can store the answer in a variable.
# tkinter.messagebox.showinfo(title, info)
# Frame(where, bg="", width=#, height=#)
# .grid(row=#, column=#, sticky=N/S/E/W)
# .pack(where, side="", padx=#, pady=#)
# Button(where, text="", command=(function, no "()")) command binds a function to a widget
# Label(where, text, bd=#, relief=SUNKEN, anchor=N/S/E/W) # last 3 parameters are opt.
# Entry(where)
# NSEW  for sticky
# .mainloop() make the window keep open
# .bind(event, function_when_event_occurs) event syntax: "<>" MB event: "<Button-#>"

# Menu bar explanation:
"""
menu_bar = Menu(root)  # create a variable for a drop-down bar
root.config(menu=menu_bar)  # makes the menu_bar variable an actual menu bar
drop_down_1_menu = Menu(menu_bar)  # makes a variable drop_down_1_menu a menu in menu_bar
menu_bar.add_cascade(label="Drop-down 1", menu=drop_down_1_menu)  # adds a cascading menu with a label and menu
drop_down_1_menu.add_command(label="Command 1", command=(function))  # adds a menu choice in drop_down_1_menu
drop_down_1_menu.add_seperator()  # creates a separator between menu items. Menu items are clickable.
"""

# Toolbar section explanation:
"""
toolbar = Frame(root, bg="blue") this makes a toolbar section where we can add buttons.
insertButton = Button(toolbar, text="Button 1", command=doNothing) makes a button (w/ variable) in the toolbar frame.
insertButton.pack(side=LEFT, padx=5, pady=2) shows the button in the toolbar frame, aligned to the left and padding.
toolbar.pack(side=TOP, fill=X) puts the toolbar below the menu bar, and spans the width of the window.
"""

# Status bar section explanation:
"""
status = Label(root, text="Preparing to do Nothing...", bd=1, relief=SUNKEN, anchor=W)
# bd sets a border of 1px, relief=SUNKEN sinks the label into the screen, anchor=W makes it justify WEST
status.pack(side=BOTTOM, fill=X) actually shows the status bar me made above.
"""