import convert


def ps():
    print()


def main():
    print("Hello, user! Welcome to my program.")
    print("This program will remove any spaces in the text file(s) you provide.")
    ps()
    print("For instructions on where to place the text file, type \"/i\".")
    print("Otherwise, type \"/go\".")
    print("To quit the program within the program, type \"-1\".")
    ps()

    while True:
        ui1 = input()

        if ui1.lower() == "/i":
            ps()
            print("Okay, so all you have to do is put the file(s) into the folder \"input\".")
            print("Then, some back here and type \"/go\".")
            print("Also, the end files will be put into the \"output\" folder.")
            print("If there are any files with the same name, they will be overwritten.")
            ps()
        elif ui1.lower() == "/go":
            ps()
            convert.go()
        elif ui1.lower() == "-1":
            quit()
        else:
            main()


main()
