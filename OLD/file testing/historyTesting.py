import time


def commandHub():
    print("This is the Command Hub. Please enter a command:")
    print()
    print("Enter some History (1)")
    print("View all History (2)")
    print("Delete all History (3)")
    print("exit (/exit/)")

    command = input("command: ")

    if command == "1":
        print()
        print(" -- Enter some History --")
        print()
        historyTitle = input("Please enter a title: ")
        print("Enter some History to be saved:")
        print("Type \"-1\" to save History.")
        print("History:")
        historyList = []
        while True:
            tempInput = input()
            if tempInput == "-1":
                historyList.append("\n")
                break
            else:
                historyList.append(tempInput + "\n")

        f = open("History.log", "a")

        f.write("-- " + historyTitle + " --\n")
        for i in range(len(historyList)):
            f.write(historyList[i])

        f.close()  # REMEMBER TO CLOSE!!!!

        print("-- History has been written. --")
        print()

        commandHub()
    elif command == "2":
        print()
        time.sleep(.5)

        f = open("History.log", "r")
        print(f.read())

        time.sleep(1)
        commandHub()
    elif command == "3":
        print()

        f = open("History.log", "w")
        f.write("")
        f.close()
        print()
        print("All History has been Deleted.")
        print()

        commandHub()


commandHub()
