from pathlib import Path
import time


def ps():
    print()


def t(length=.25):
    time.sleep(length)


def go():
    for file in Path("input/").iterdir():
        print("Full name:")
        print(file)
        ps()
        t()
        print("Name:")
        print(file.name)
        ps()
        t()
        print("Contents:")
        f = open(file, "r")
        print(f.read())
        ps()
        t()
        print("- - - - - - - - - - - - -")
        ps()
        t()

    # actual converting process
    for file in Path("input/").iterdir():
        endResult = []
        spacesCut = 0
        f = open(file, "r")
        for char in f.read():
            if char == " " or char == "\n":
                spacesCut += 1
            else:
                endResult.append(char)

        fileName = file.name.split(".")
        # try looking for existing file
        fileFound = None
        try:
            f = open(Path("output/" + fileName[0] + "_NoSpaces." + fileName[1]), "r")
            fileFound = True
        except FileNotFoundError:
            fileFound = False

        print("Debugging: fileFound = " + str(fileFound))

        if fileFound:
            print("A file with the same name has been found. Continue (y/n)?")
            ui2 = input()
            if ui2.lower() == "y":
                print("Continuing...")
                f = open(Path("output/" + fileName[0] + "_NoSpaces." + fileName[1]), "w")
                for char in endResult:
                    f.write(char)
                f.close()
            else:
                print("Okay, moving on.")
        elif not fileFound:
            print("No file with same name found, continuing...")
            f = f = open(Path("output/" + fileName[0] + "_NoSpaces." + fileName[1]), "w")
            for char in endResult:
                f.write(char)
            f.close()
        print("\"" + str(file.name) + "\" has been converted. Moving on.")
        ps()
        t()
    t()
    print("Okey dokey, Files have been converted.")
