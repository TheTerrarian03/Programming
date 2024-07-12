# Options: translate point, rotate point, reflect point, dilate point, vertical/horixontal stretch/compression


def option_algorithms(option):
    pass


def choose_options(bop=False):  # bop = beginning of program
    while True:
        if bop:
            print("Welcome to my 9th Grade Geometry Equation thingy I made! Enjoy!")
        print("\nWhat would you like to?\n")
        print('"1" - Translate Point\n"2" - Rotate Point About Origin\n"3" - Reflect Point Across Line\n'
              '"4" - Dilate Point About Origin\n"5" - Vertical Stretch/Compression\n'
              '"6" - Horizonal Stretch/Compression')
        chosen_option = input("\nChoice: ")
        print(chosen_option)

        try:
            if int(chosen_option) <=6 and int(chosen_option) >=1:
                print(option_algorithms(chosen_option))
            else:
                print("\nPlease try again. You need to enter a number.\n")
            break
        except ValueError:
            print("\nPlease try again. You need to enter a number.\n")


choose_options(bop=True)
