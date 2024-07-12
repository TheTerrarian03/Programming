from tkinter import *
import tkinter.messagebox
import time
from random import choice


def create_win():
    # create variables:
    used_letters = []
    used_letters_bad = []
    words_to_pick = ["Apple", "Stick Man", "Music", "Sister", "Pictures", "Computer"]
    word = ""
    word_picked = 0

    def help():
        knowledge_1 = tkinter.messagebox.askquestion("HELP", "Do you know how to play Hang Man?")
        if knowledge_1 == "yes":
            knowledge_2 = tkinter.messagebox.askquestion("HELP", "Good. This is pretty much "
                                                                 "just like Traditional Hang Man.\nGood?")
            if knowledge_2 == "yes":
                tkinter.messagebox.showinfo("HELP", "Ok, Have Fun!")
            elif knowledge_2 == "no":
                tkinter.messagebox.showinfo("HELP", "You'll figure it out!")
        elif knowledge_1 == "no":
            # Spruce up this message box by making an entry the user can copy instead?
            tkinter.messagebox.showinfo("HELP", "Visit this website:"
                                                "\nhttps://www.wikihow.com/Play-Hangman")
            knowledge_3 = tkinter.messagebox.askquestion("HELP", "Good?")
            if knowledge_3 == "yes":
                tkinter.messagebox.showinfo("HELP", "Ok, Have Fun!")
            elif knowledge_3 == "no":
                tkinter.messagebox.showinfo("HELP", "You'll figure it out!")

    pick_word = lambda : return choice(words_to_pick) if (word_picked == 0) else tkinter.messagebox.showinfo("Your"
                                                                                                      "word"
                                                                                                      "is"
                                                                                                      "still\n"
                                                                                                      "" + word)

    win = Tk()
    win.title("Hang Man!")

    guide_label_1 = Label(win, text="This is the MAIN OPTIONS WINDOW."
                                    "\n\\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/")
    guide_label_1.grid()

    help_button = Button(win, text="/-- HELP --/", width=25, command=help)
    help_button.grid(row=1)

    show_hangman_button = Button(win, text="Show Hang Man", width=25)
    show_hangman_button.grid(row=2)

    pick_button = Button(win, text="Pick word", width=25, command=pick_word)
    pick_button.grid(row=3)

    win.mainloop()




create_win()
