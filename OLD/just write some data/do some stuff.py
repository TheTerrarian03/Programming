from pathlib import Path
from random import choice as rc


def write(charAmount):
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    with open("SomeDataProbably.txt", "wt") as f:
        for i in range(charAmount):
            f.write(rc(characters))
            print(str((i / charAmount) * 100) + "%")
            if i % 10 == 0:
                f.write("\n")
        print("100.0%")

    print()
    print("Write Successful.")
    print("Going to main menu.")
    print()


def delete():
    with open("SomeDataProbably.txt", "wt") as f:
        f.write("")

    print()
    print("Write (\"Delete\" Data) Successful")
    print("Going to main menu.")
    print()


def exitSign():
    with open("SomeDataProbably.txt", "at") as f:
        f.write(" :)")


def menu():
    print("Commands:\n/write, /delete, and /exit.\nEnter here:")
    command = input()
    if command.lower() == "/write":
        while True:
            aoc = input("Enter a number of characters: ")
            try:
                int(aoc)
                break
            except ValueError:
                continue
        aoc = int(aoc)
        write(aoc)
    elif command.lower() == "/delete":
        delete()
    elif command.lower() == "/exit":
        exitSign()
        quit()
    else:
        menu()

    menu()


menu()
