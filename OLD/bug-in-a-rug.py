# Note: Add some features such as Bug Test Averaging and more menu asthetics.
# Add time.sleep functions to spin() to add a more realistic spin. [ time.sleep(3) ] and when viewing bugs.
# finish spin() --> spun_result() --> removeBug()

# bug1 is a square, purple, small bug.
# bug2 is a circle, blue, big bug.
# bug3 is a circle, orange, big bug.
# bug4 is a triangle, red, small bug.
# bug5 is a triangle, green, small bug.
# bug6 is a square, yellow, big bug.

import random
import time

bug1 = True
bug2 = True
bug3 = True
bug4 = True
bug5 = True
bug6 = True
sbug1 = False
sbug2 = False
sbug3 = False


def quit():
    print("")
    print("Bye!")
    time.sleep(2)


def BugInARug_Game():
    global bugAssetToSpinFor
    print("")
    print("Welcome To The Bug-In-A-Rug Game!")
    print("Made by Logan")
    print("Would you like to spin for shapes, colors, or size?")
    bugAssetToSpinFor = input("No capitalization: ")
    if bugAssetToSpinFor == "shapes" or bugAssetToSpinFor == "colors" or bugAssetToSpinFor == "size":
        print("Ok then,", bugAssetToSpinFor, "it is.")
        print("")
    else:
        print("Please try again...")
        time.sleep(.5)
        BugInARug_Game()


    def spin():
        print("")
        print("Spinning...")
        if bugAssetToSpinFor == "shapes":
            spunAsset = random.choice(["square", "circle", "triangle"])
        elif bugAssetToSpinFor == "colors":
            spunAsset = random.choice(["purple", "blue", "orange", "red", "green", "yellow"])
        elif bugAssetToSpinFor == "size":
            spunAsset = random.choice(["small", "medium", "large"])
        print("")
        print("You got", spunAsset)
        #this next area is where when you spin it shows you the numbers and asset each bug has, except much smaller.
        bugsLeftSmallScale = []
        if bugAssetToSpinFor == "shapes":
            if bug1:
                print("1 - □")
            if bug2:
                print("2 - ○")
            if bug3:
                print("3 - ○")
            if bug4:
                print("4 - △")
            if bug5:
                print("5 - △")
            if bug6:
                print("6 - □")
        if bugAssetToSpinFor == "colors":
            if bug1:
                print("1 - PURPLE")
            if bug2:
                print("2 - BLUE")
            if bug3:
                print("3 - ORANGE")
            if bug4:
                print("4 - RED")
            if bug5:
                print("5 - GREEN")
            if bug6:
                print("6 - YELLOW")
        if bugAssetToSpinFor == "size":
            if bug1:
                print("1 - SMALL")
            if bug2:
                print("2 - BIG")
            if bug3:
                print("3 - BIG")
            if bug4:
                print("4 - SMALL")
            if bug5:
                print("5 - SMALL")
            if bug6:
                print("6 - BIG")
        whichBugToRemove = input("Which bug would you like to remove? ")
        print("bug", whichBugToRemove, "will be removed")
        time.sleep(1)
        print("Done")
        if whichBugToRemove == 1:
            bool(bug1)
        if whichBugToRemove == 2:
            bug2 == False
        if whichBugToRemove == 3:
            bug3 == False
        if whichBugToRemove == 4:
            bug4 == False
        if whichBugToRemove == 5:
            bug5 == False
        if whichBugToRemove == 6:
            bug6 == False
        print(bug3)
        globalOptions()


    def viewBugs():
        if bugAssetToSpinFor == "shapes":

            print("")

            if bug1 and bug2:
                print("+-----------+         |||||")
                print("|           |       ||     ||")
                print("|     1     |     ||    2    ||")
                print("|           |       ||     ||")
                print("+-----------+         |||||")

            if bug1 and bug2 == False:
                print("+-----------+")
                print("|           |")
                print("|     1     |")
                print("|           |")
                print("+-----------+")

            if bug1 == False and bug2:
                print("    |||||")
                print("  ||     ||")
                print("||    2    ||")
                print("  ||     ||")
                print("    |||||")

            print("")

            if bug3 and bug4:
                print("    |||||               |")
                print("  ||     ||            |||")
                print("||    3    ||        || 4 ||")
                print("  ||     ||        ||       ||")
                print("    |||||         |||||||||||||")

            if bug3 and bug4 == False:
                print("    |||||")
                print("  ||     ||")
                print("||    3    ||")
                print("  ||     ||")
                print("    |||||")

            if bug3 == False and bug4:
                print("      |")
                print("     |||")
                print("   || 4 ||")
                print(" ||       ||")
                print("|||||||||||||")

            print("")

            if bug5 and bug6:
                print("      |           +-----------+")
                print("     |||          |           |")
                print("   || 5 ||        |     6     |")
                print(" ||       ||      |           |")
                print("|||||||||||||     +-----------+")

            time.sleep(1)

            if bug5 == False and bug6:
                print("+-----------+")
                print("|           |")
                print("|     6     |")
                print("|           |")
                print("+-----------+")

            if bug5 and bug6 == False:
                print("      ")
                print("     |||")
                print("   || 5 ||")
                print(" ||       ||")
                print("|||||||||||||")

        if bugAssetToSpinFor == "colors":
            if bug1 and bug2:
                print("1 --> PURPLE")
                print("2 --> BLUE")

            if bug1 == False and bug2:
                print("2 --> BLUE")

            if bug1 and bug2 == False:
                print("1 --> PURPLE")

            print("")

            if bug3 and bug4:
                print("3 --> ORANGE")
                print("4 --> RED")

            if bug3 == False and bug4:
                print("4 --> RED")

            if bug3 and bug4 == False:
                print("3 --> ORANGE")

            print("")

            if bug5 and bug6:
                print("5 --> GREEN")
                print("6 --> YELLOW")

            if bug5 == False and bug6:
                print("6 --> YELLOW")

            if bug5 and bug6 == False:
                print("5 --> GREEN")

        if bugAssetToSpinFor == "size":
            if bug1 and bug2:
                print("1 --> SMALL")
                print("2 --> BIG")

            if bug1 == False and bug2:
                print("2 --> BIG")

            if bug1 and bug2 == False:
                print("1 --> SMALL")

            print("")

            if bug3 and bug4:
                print("3 --> BIG")
                print("4 --> SMALL")

            if bug3 == False and bug4:
                print("4 --> SMALL")

            if bug3 and bug4 == False:
                print("3 --> BIG")

            print("")

            if bug5 and bug6:
                print("5 --> SMALL")
                print("6 --> BIG")

            if bug5 == False and bug6:
                print("6 --> BIG")

            if bug5 and bug6 == False:
                print("5 --> SMALL")

        print("")
        print("Where would you like to go next?")
        print("")
        globalOptions()


    def viewStinkBugs():
        if sbug1:
            print("    ||||||||")
            print("  |||      |||")
            print("|||    11    |||")
            print("|||    11    |||")
            print("  |||      |||")
            print("    ||||||||")
        if sbug2:
            print("    ||||||||")
            print("  |||      |||")
            print("|||    22    |||")
            print("|||    22   |||")
            print("  |||      |||")
            print("    ||||||||")
        if sbug3:
            print("    ||||||||")
            print("  |||      |||")
            print("|||    33    |||")
            print("|||    33    |||")
            print("  |||      |||")
            print("    ||||||||")
        else:
            print("You're doing GREAT so far! You don't have ANY stink bugs!")
        print("")
        viewStinkBugsContinue = input("Continue? ")
        if viewStinkBugsContinue == "y":
            globalOptions()
        else:
            print("Well you were going to have to continue anyways, so...")
            print("")
            time.sleep(0.5)
            globalOptions()


    def globalOptions():
        print("You have 5 total options:")
        print("spin,")
        print("view bugs,")
        print("view stink bugs,")
        print("quit,")
        print("Or help (instructions - currently not an actual feature).")
        globalOptionsChoice = input("Which one? ")
        if globalOptionsChoice == "spin":
            spin()
        elif globalOptionsChoice == "view bugs":
            print("")
            viewBugs()
        elif globalOptionsChoice == "view stink bugs":
            print("")
            viewStinkBugs()
        elif globalOptionsChoice == "quit":
            quit()
        elif globalOptionsChoice == "help":
            print("Sorry, help is not yet a feature in this version of Bug In A Rug."
                  " If you need assistance, please email"
                  " TheTerrarian03@gmail.com. Thanks!")
            helpContinue = input("Continue on in game?\n")
            if helpContinue == "y" or helpContinue == "yes":
                globalOptions()
            elif helpContinue == "n":
                print("Sorry, there is nothing to do for you here. Sending you on in 10 seconds.")
                time.sleep(12)
                globalOptions()
            else:
                print("Invalid answer.")
                time.sleep(.5)
                globalOptions()
        else:
            print("")
            print("Try Again:")
            BugInARug_Game()

    '''
    def removeBug():
    def addStinkBug():
    def win():
    def lose():
    def playAgain():
    '''

    globalOptions()


def atStartUp():
    print("")
    print("Would you like to run an Alive Or Dead Test? Or play the actual Game?")
    print("Your choices are: 'Test' or 'Game'")
    choice1 = input()
    if choice1 == "Test" or choice1 == "test":
        print("Ok, Test it is!")
        aliveOrDeadTest()
    if choice1 == "Game" or choice1 == "game":
        print("Ok, Game it is!")
        BugInARug_Game()
    else:
        print("")
        print("Try Again...")
        atStartUp()


def aliveOrDeadTest():
    print("")
    tests = input("How many times is the bug tested? ")
    for time in range(1,(int(tests))+1):
        print("The bug was determined as", (random.choice([" Alive          ", " Dead           ", " Maybe Alive    ", \
            " Probably Alive ", " Probably Dead  "])), "When tested on test", time)


atStartUp()