from tkinter import *
import tkinter.messagebox


def simple_mode():
    class CreateEnemy:
        def __init__(self, name, health):
            self.name = name
            self.health = health


    root = Tk()
    root.title("FIGHT!")

    n_entry = Entry(root, width=40)
    h_entry = Entry(root, width=40)

    n_entry.grid(row=0, column=0)
    h_entry.grid(row=1, column=0)

    n_entry.insert(0, "Name")
    h_entry.insert(0, "Health")

    def run_enemy_creation():
        name_var = n_entry.get()
        health_var = h_entry.get()
        enemy = CreateEnemy(name_var, health_var)

        def he_questions():
            tkinter.messagebox.showinfo("Enemy-", "He questions why you are still there."
                                                  "\nHe says, \"You should be running.\"")

        enemy_win = Tk()
        enemy_win.title("Enemy Created!")

        label1 = Label(enemy_win, text="An enemy called \"" + enemy.name + "\" appeared!")
        label2 = Label(enemy_win, text="They have " + enemy.health + "hp")
        label3 = Label(enemy_win, text="Oh no!")
        ok_button = Button(enemy_win, text="Ok.", command=he_questions)
        leave_button = Button(enemy_win, text="Ok. It's fine. Let's leave.", command=quit)

        label1.grid(row=0)
        label2.grid(row=1)
        label3.grid(row=2)
        ok_button.grid(row=3, ipadx=52)
        leave_button.grid(row=4)

        enemy_win.mainloop()

    run_button = Button(root, text="Run Creation", command=run_enemy_creation)
    run_button.grid(row=2, ipadx=20)

    root.mainloop()


def game_mode():
    pass


choice_win = Tk()
choice_win.title("Choose-One Window.exe")

simple_button = Button(choice_win, text="Simple Mode", command=simple_mode)
game_button = Button(choice_win, text="Game Mode", command=game_mode)

simple_button.pack(ipadx=50, ipady=20, padx=20, pady=20)
game_button.pack(ipadx=50, ipady=20, padx=20, pady=20)

choice_win.mainloop()
