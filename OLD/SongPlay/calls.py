import os

def play(songFile):
    for line in songFile:
        if line.endswith("\n"):
            print(line[:-1])
        else:
            print(line)

def getCommand():
    while True:
        print("\nPlease enter a command below:\n"
              "(Use \"help\" for a list of commands)")
        command = input("$ ").lower()
        if command == "help":  # command #1
            print("\nCommands that can be used:\n"
                  "    help  - print this list\n"
                  "    play  - play a song\n"  # not implemented
                  "    close - close the program\n"
                  "    print - print out the contents of a given music piece")
        elif command == "play":  # command #2
            while True:
                print("\nPlease enter the name of the piece, "
                      "Capitalization matters.")
                name = input("$ ").lower()
                try:
                    f = open(("Saves/" + name + ".song"), "r")
                    play(f)
                    f.close()
                    break
                except FileNotFoundError:
                    print("\nERROR: Song File not found! Would you like to"
                          "Enter a different one? (y/n)")
                    tryAgain = input("$ ").lower()
                    if tryAgain == "y":
                        continue
                    else:
                        break
        elif command == "close":  # command #3
            return (3, "close")
        elif command == "print":  # command #4
            while True:
                print("\nPlease enter the name of the piece, "
                      "Capitalization matters.")
                name = input("$ ").lower()
                try:
                    songFile = open(("Saves/" + name + ".song"), "r")
                    print("\n-- Song Start --")
                    for line in songFile:
                        if line.endswith("\n"):
                            print(line[:-1])
                        else:
                            print(line)
                    print("-- Song End --")
                    songFile.close
                    break
                except FileNotFoundError:
                    print("\nERROR: Song File not found! Would you like to"
                          "Enter a different one? (y/n)")
                    tryAgain = input("$ ").lower()
                    if tryAgain == "y":
                        continue
                    else:
                        break
                print()
                print("\nSong File done reading")
            print("\nINFO: Exiting")
            return (4, "print")

