from random import choice as rc
from time import sleep as s


def roll():
    _8ballChoices = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                     "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                     "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                     "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
                     "My sources say no.", "Outlook not so good.", "Very doubtful."]  # from best to worst, btw
    return rc(_8ballChoices)


def think():
    for _ in range(4):
        print(".")
        s(.25)
        print("..")
        s(.25)
        print("...")
        s(.25)
    print()
    s(.5)


def askQ():
    print("Here you can enter your question for the 8-ball to answer to.")
    ui1 = input("Your question: ")
    think()
    print("8 Ball says: \"" + roll() + "\"")
    print()

    while True:
        uiCont = input("Continue? (\"y\"/\"n\" (quit)): ")
        if uiCont.lower() == "y":
            break
        elif uiCont.lower() == "n":
            quit()
        else:
            continue
    print()
    askQ()


def intro():
    print("Welcome to Logan's 8-ball program, just ask it a question and get an answer!")
    print()
    askQ()


intro()
