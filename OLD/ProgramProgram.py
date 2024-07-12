from tkinter import *
import tkinter.messagebox


def hi():
    tkinter.messagebox.showinfo("Message", "Hi")


def matthew_message():
    tkinter.messagebox.showinfo("Matthew's Message", "RATS!")


def quiz_1():
    tkinter.messagebox.showinfo("Quiz 1", "This will soon be Quiz #1.")


def exit_program():
    exit_program_confirm = tkinter.messagebox.askquestion("Exiting Program",
                                                          "You knew you could just click the X, right?"
                                                          "\nRIGHT?")
    if exit_program_confirm == "yes":
        tkinter.messagebox.showinfo("Exit Program", "Good job.")
        tkinter.messagebox.showinfo("Exit Program", "Exiting Program...\nClick OK...")
        quit()
    elif exit_program_confirm == "no":
        tkinter.messagebox.showinfo("Exit Program", "...")
        tkinter.messagebox.showinfo("Exit Program", "Make sure to click the \"Hell\" button next time.")
        tkinter.messagebox.showinfo("Exit Program", "Exiting Program...\nClick OK...")
        quit()


def draw_circle():
    tkinter.messagebox.showinfo("Drawing Circle...", "*Draws a circle*")


def choose_diff_button():
    tkinter.messagebox.showinfo("Exit Program", "Please select the right button.\nThanks!")


def choose_diff_button2():
    tkinter.messagebox.showinfo("Exit Program", "LOL\n:D")


def error():
    error_win = Tk()
    error_win.title("ERROR!")
    error_win.geometry("300x200")

    error_text_statement = Label(error_win, text="You messed up.")
    error_text_statement.grid(row=0, sticky=E)
    error_text_statement = Label(error_win, text="What is your reasoning?")
    error_text_statement.grid(row=0, column=1, sticky=W)

    error_text_box = Entry(error_win)
    error_text_box.delete(0, END)
    error_text_box.insert(0, "Reasoning...")
    error_text_box.grid(row=1, columnspan=3, sticky=W)

    def submit_reasoning():
        reasoning_for_error = error_text_box.get()
        tkinter.messagebox.askquestion("ERROR", "Reason:\n" + reasoning_for_error + "\nCorrect?")
        tkinter.messagebox.showinfo("ERROR", "To confirm you are human, press \"Yes\"")
        tkinter.messagebox.showinfo("ERROR", "Good job.")
        error_win.quit()

    enter_button = Button(error_win, text="Submit", command=submit_reasoning)
    enter_button.grid(padx=5, pady=5, row=4)

    error_win.mainloop()


def password_win():
    pw_continue = tkinter.messagebox.askquestion("Password", "Continue?")

    if pw_continue == "no":
        tkinter.messagebox.showinfo("Password", "Good choice")
    elif pw_continue == "yes":
        tkinter.messagebox.showinfo("The Vault", "Welcome to the Vault.")

        password_window = Tk()
        password_window.geometry("200x200")
    else:
        pass


root = Tk()
root.geometry("640x360")

# Menu drop down section:
menu = Menu(root)
root.config(menu=menu)

# make the "File" menu list
file = Menu(menu)
menu.add_cascade(label="File", menu=file)

file.add_command(label="Start Quiz...", command=quiz_1)
file.add_separator()
file.add_command(label="Error", command=error)

# make the "Imagery" menu list
imagery = Menu(menu)
menu.add_cascade(label="Imagery", menu=imagery)

imagery.add_command(label="Draw Circle", command=draw_circle)

# make the "Programs" menu list
programs = Menu(menu)
menu.add_cascade(label="Programs", menu=programs)

programs.add_command(label="Mysterious Program...", command=hi)
programs.add_command(label="Matthew", command=matthew_message)

# Add "Exit" menu on menu
exit_menu = Menu(menu)
menu.add_cascade(label="Exit Program", menu=exit_menu)

exit_menu.add_command(label="Press this button to exit", command=choose_diff_button)
for _ in range(7):
    exit_menu.add_command(label="No, this button, silly!", command=choose_diff_button)

exit_exit_menu = Menu(exit_menu)
exit_menu.add_cascade(label="No, this button, silly!", menu=exit_exit_menu)

exit_exit_menu.add_command(label="Press this button to exit", command=choose_diff_button2)
exit_exit_menu.add_command(label="Button to press", command=exit_program)

for _ in range(6):
    exit_menu.add_command(label="No, this button, silly!", command=choose_diff_button)

exit_menu.add_command(label="No, Press THIS ONE!", command=choose_diff_button2)

# create a button leading to password_win
password_button = Button(root, text="The Vault", command=password_win)
password_button.pack(fill="both", padx=10, pady=7)

root.title("My Program Program!")
root.mainloop()
