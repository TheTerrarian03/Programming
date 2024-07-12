import time
import random


seeds = {
    "main": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"],
    "main2": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z", "0", "1", '2', "3", "4", "5", "6", "7", "8", "9"],
    "1": ["T", "S", "R", "Z", "M", "K", "E", "Y", "N", "O", "L", "H", "I", "V", "W", "U", "D", "C", "B", "P", "Q",
             "X", "A", "G", "F", "J"],
    "2": ["O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A", "Z", "Y", "X", "W", "V", "U",
             "T", "S", "R", "Q", "P"],
    "3": ["Q", "R", "A", "B", "C", "D", "E", "M", "N", "U", "P", "Z", "Y", "U", "V", "W", "G", "I", "H", "T", "S",
             "F", "J", "K", "L", "X"],
    "4": ["R", "F", "O", "P", "Q", "Y", "X", "W", "7", "E", "G", "H", "T", "J", "0", "U", "V", "K", "L", "B", "A",
             "6", "8", "I", "S", "D", "C", "M", "N", "1", "2", "9", "5", "Z", "3", "4"],
    "5": ["M", "N", "O", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "U", "O", "Z", "4", "3", "1", "2", "P",
             "V", "W", "8", "X", "A", "F", "6", "R", "Q", "T", "S", "5", "9", "Y", "7"],
}
seedsChoices = ["1", "2", "3", "4", "5"]


def run(uStr, uSeed):
    pass


def main():
    while True:
        f = input("Sending or receiving? (s/r): ")
        if f.lower() == "s":
            sending()
            break
        elif f.lower() == "r":
            receiving()
            break
        else:
            print("Please try again.")
    convAgain = input("Would you like to go again?")
    if convAgain.lower() == "y":
        main()
    elif convAgain.lower() == "n":
        print("Okay. Thank you for using my Enigma Machine program!")
        time.sleep(1)
        print("Bye!")
        time.sleep(.25)
        print("Exiting... 0%")
        time.sleep(.25)
        print("Exiting... 25%")
        time.sleep(.5)
        print("Exiting... 50%")
        time.sleep(.5)
        print("Exiting... 75%")
        time.sleep(.5)
        print("Exiting... 99%")
        time.sleep(1)
        print("Exiting... 100%!")
        time.sleep(.5)
        quit()
    else:
        print("I'll take that as a \"no\".")
        time.sleep(1)
        print("Thank you for using my Enigma Machine program!")
        time.sleep(1)
        print("Bye!")
        time.sleep(.25)
        print("Exiting... 0%")
        time.sleep(.25)
        print("Exiting... 25%")
        time.sleep(.5)
        print("Exiting... 50%")
        time.sleep(.5)
        print("Exiting... 75%")
        time.sleep(.5)
        print("Exiting... 99%")
        time.sleep(1)
        print("Exiting... 100%!")
        time.sleep(.5)
        quit()


def sending():
    uInput = input("Enter your message here: ")
    uS = input("Is there a certain seed you would like to use? (a number for seed, \"no\" for no seed): ")
    if uS.lower() == "no":



def receiving():
    pass


main()
