# UnitConversionBeta3

import time


square = "█"


def main_menu():
    # this prints the main menu out, plus choice at end
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█           Welcome to my Unit Conversion Program!!!           █")
    time.sleep(.2)
    print("█                -- Made By: Logan S. Meyers --                █")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█   Distance Converter, Temperature Converter, Number Sorter   █")
    time.sleep(.2)
    print("█     Mean + Total Finder, Range Finder, and 2-Number Calc     █")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█                      Please Enter One                        █")
    main_menu_choice = input("                       ")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    for _ in range(3):
        print("")
    time.sleep(.2)

    # convert main_menu_choice to all lowercase
    main_menu_choice_lower = main_menu_choice.lower()

    # if statements leading to all the different functions
    if main_menu_choice_lower == "distance converter" or main_menu_choice_lower == "distance":
        distance_converter()
    elif main_menu_choice_lower == "temperature converter" or main_menu_choice_lower == "temperature" or main_menu_choice_lower == "temp" or main_menu_choice_lower == "temp.":
        temperature_converter()
    elif main_menu_choice_lower == "number sorter" or main_menu_choice_lower == "sorter" or main_menu_choice_lower == "ns":
        number_sorter()
    elif main_menu_choice_lower == "exit" or main_menu_choice_lower == "quit":
        exit_quit()

    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    print("█               Would You Want To Convert Again?               █")
    time.sleep(.2)
    print("█                     (Yes/yes/y/No/no/n)                      █")
    restart_main_menu = input("                      ")
    restart_main_menu_lower = restart_main_menu.lower()
    if restart_main_menu_lower == "yes" or restart_main_menu_lower == "y":
        print("█                                                              █")
        time.sleep(.2)
        print("████████████████████████████████████████████████████████████████")
        time.sleep(.2)
        for _ in range(3):
            print("")
        main_menu()
    elif restart_main_menu_lower == "no" or restart_main_menu_lower == "n":
        print("█                                                              █")
        time.sleep(.2)
        print("█--------------------------------------------------------------█")
        time.sleep(.2)
        print("█                                                              █")
        time.sleep(.2)
        print("█                          Exiting...                          █")
        time.sleep(.5)
        print("█                                                              █")
        time.sleep(.2)
        print("█                             10%                              █")
        time.sleep(.25)
        print("█                             25%                              █")
        time.sleep(.15)
        print("█                             50%                              █")
        time.sleep(.35)
        print("█                             75%                              █")
        time.sleep(.2)
        for percent_end in range(76, 100):
            print("█                             " + str(percent_end) + "%                              █")
            percent_end + 1
            time.sleep(.05)
        time.sleep(1.25)
        print("█                             100%                             █")
        time.sleep(.2)
        print("█                                                              █")
        time.sleep(.2)
        print("████████████████████████████████████████████████████████████████")

        time.sleep(.15)

        print("")
        print("████   █   █  █████  ███")
        print("█   █  █   █  █      ███")
        print("█   █  █   █  █      ███")
        print("████    █ █   ████   ███")
        print("█   █    █    █       █")
        print("█   █    █    █")
        print("████     █    █████   █")


def distance_converter():
    # this prints out the choices area
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█    Choices: mm, cm, m, km, inches, feet, yards, and miles    █")
    time.sleep(.2)
    print("█               Unit of distance to convert FROM               █")
    b = input("                ")
    print("█                       Chose HOW MANY                         █")
    c = float(input("                "))
    print("█                Unit of distance to convert TO                █")
    d = input("                ")
    print("████████████████████████████████████████████████████████████████")
    for _ in range(3):
        print("")

    # Gigantic list of if statements
    if b == 'mm' and d == 'mm':
        answer = c
    if b == 'mm' and d == 'cm':
        answer = c / 10
    if b == 'mm' and d == 'm':
        answer = c / 1000
    if b == 'mm' and d == 'km':
        answer = c / 1000000
    if b == 'mm' and d == 'inches':
        answer = c / 25.4
    if b == 'mm' and d == 'feet':
        answer = c / 304.8
    if b == 'mm' and d == 'yards':
        answer = c / 914.4
    if b == 'mm' and d == 'miles':
        answer = c / 1609344
    if b == 'cm' and d == 'mm':
        answer = c * 10
    if b == 'cm' and d == 'cm':
        answer = c
    if b == 'cm' and d == 'm':
        answer = c / 100
    if b == 'cm' and d == 'km':
        answer = c / 100000
    if b == 'cm' and d == 'inches':
        answer = c / 2.54
    if b == 'cm' and d == 'feet':
        answer = c / 30.48
    if b == 'cm' and d == 'yards':
        answer = c / 91.44
    if b == 'cm' and d == 'miles':
        answer = c / 160934.4
    if b == 'm' and d == 'mm':
        answer = c * 1000
    if b == 'm' and d == 'cm':
        answer = c * 100
    if b == 'm' and d == 'm':
        answer = c
    if b == 'm' and d == 'km':
        answer = c / 1000
    if b == 'm' and d == 'inches':
        answer = c * 39.3701
    if b == 'm' and d == 'feet':
        answer = c * 3.28084
    if b == 'm' and d == 'yards':
        answer = c * 1.094
    if b == 'm' and d == 'miles':
        answer = c / 1609
    if b == 'km' and d == 'mm':
        answer = c * 1000000
    if b == 'km' and d == 'cm':
        answer = c * 100000
    if b == 'km' and d == 'm':
        answer = c * 1000
    if b == 'km' and d == 'km':
        answer = c
    if b == 'km' and d == 'inches':
        answer = c * 39370.1
    if b == 'km' and d == 'feet':
        answer = c * 3281
    if b == 'km' and d == 'yards':
        answer = c * 1094
    if b == 'km' and d == 'miles':
        answer = c / 1.609
    if b == 'inches' and d == 'mm':
        answer = c * 25.4
    if b == 'inches' and d == 'cm':
        answer = c * 2.54
    if b == 'inches' and d == 'm':
        answer = c / 39.37
    if b == 'inches' and d == 'km':
        answer = c / 39370
    if b == 'inches' and d == 'inches':
        answer = c
    if b == 'inches' and d == 'feet':
        answer = c / 12
    if b == 'inches' and d == 'yards':
        answer = c / 36
    if b == 'inches' and d == 'miles':
        answer = c / 63360
    if b == 'feet' and d == 'mm':
        answer = c * 304.8
    if b == 'feet' and d == 'cm':
        answer = c * 30.48
    if b == 'feet' and d == 'm':
        answer = c / 3.281
    if b == 'feet' and d == 'km':
        answer = c / 3281
    if b == 'feet' and d == 'inches':
        answer = c * 12
    if b == 'feet' and d == 'feet':
        answer = c
    if b == 'feet' and d == 'yards':
        answer = c / 3
    if b == 'feet' and d == 'miles':
        answer = c / 5280
    if b == 'yards' and d == 'mm':
        answer = c * 914.4
    if b == 'yards' and d == 'cm':
        answer = c * 91.44
    if b == 'yards' and d == 'm':
        answer = c / 1.094
    if b == 'yards' and d == 'km':
        answer = c / 1094
    if b == 'yards' and d == 'inches':
        answer = c * 36
    if b == 'yards' and d == 'feet':
        answer = c * 3
    if b == 'yards' and d == 'yards':
        answer = c
    if b == 'yards' and d == 'miles':
        answer = c / 1760
    if b == 'miles' and d == 'mm':
        answer = c * 1609344
    if b == 'miles' and d == 'cm':
        answer = c * 160934.4
    if b == 'miles' and d == 'm':
        answer = c / 1609.344
    if b == 'miles' and d == 'km':
        answer = c / 1.609344
    if b == 'miles' and d == 'inches':
        answer = c * 63360
    if b == 'miles' and d == 'feet':
        answer = c * 5280
    if b == 'miles' and d == 'yards':
        answer = c * 1760
    if b == 'miles' and d == 'miles':
        answer = c

    # Print answer section
    answer_string = "█           Your answer is: " + str(answer) + d + "           █"
    answer_string_len = len(answer_string)
    print(square * answer_string_len)
    time.sleep(.2)
    print(answer_string)
    time.sleep(.2)
    print(square * answer_string_len)
    time.sleep(1)
    for _ in range(3):
        print("")
    time.sleep(.2)


def temperature_converter():
    # this prints out the choices area
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█                     Choices: c, f, or k.                     █")
    time.sleep(.2)
    print("█               Unit of distance to convert FROM               █")
    f = input("                ")
    print("█                       Chose HOW MANY                         █")
    g = float(input("                "))
    print("█                Unit of distance to convert TO                █")
    h = input("                ")
    print("████████████████████████████████████████████████████████████████")
    for _ in range(3):
        print("")

    if f == "c" and h == "c":
        answer = g
    if f == "c" and h == "f":
        answer = (g * 9 / 5) + 32
    if f == "c" and h == "k":
        answer = g + 273.15
    if f == "f" and h == "c":
        answer = (g - 32) * 5 / 9
    if f == "f" and h == "f":
        answer = g
    if f == "f" and h == "k":
        answer = ((g - 32) * 5 / 9) + 273.15
    if f == "k" and h == "c":
        answer = g - 273.15
    if f == "k" and h == "f":
        answer = ((g - 273.15) * 9 / 5) + 32
    if f == "k" and h == "k":
        answer = g

    # Print answer section
    answer_string = "█           Your answer is: " + str(answer) + " degrees " + h + "           █"
    answer_string_len = len(answer_string)
    print(square * answer_string_len)
    time.sleep(.2)
    print(answer_string)
    time.sleep(.2)
    print(square * answer_string_len)
    time.sleep(1)
    for _ in range(3):
        print("")
    time.sleep(.2)


def number_sorter():
    # this prints out the choices area
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█   Sort from least-to-greatest (1) or greatest-to-least (2)   █")
    sorting_direction = input("█   ")
    if sorting_direction == "1":
        list = []
        print("█                                                              █")
        time.sleep(.2)
        print("█                How many numbers will there be?               █")
        j = int(input("█                "))
        for k in range(j):
            if k + 1 < 10:
                print("█                 Enter number at location " + str(k + 1) + ":                  █")
            elif k + 1 < 100:
                print("█                 Enter number at location " + str(k + 1) + ":                 █")
            elif k + 1 < 1000:
                print("█                 Enter number at location " + str(k + 1) + ":                █")
            elif k + 1 < 10000:
                print("█                 Enter number at location " + str(k + 1) + ":               █")
            elif k + 1 < 100000:
                print("█                 Enter number at location " + str(k + 1) + ":              █")
            elif k + 1 < 1000000:
                print("█                 Enter number at location " + str(k + 1) + ":             █")
            list.append(input("                  "))

        print("█                       Did you mess up?                       █")
        did_i_mess_up = input("                        ")
        if did_i_mess_up.lower() == "y" or did_i_mess_up.lower == "yes":
            print("█                    Ok, Let's try again.                      █")
            time.sleep(.2)
            print("█                                                              █")
            time.sleep(.2)
            print("████████████████████████████████████████████████████████████████")
            for _ in range(3):
                print("")
            number_sorter()
        elif did_i_mess_up.lower() == "n" or did_i_mess_up.lower() == "no":
            print("█                     Ok, Let's move on.                       █")
            time.sleep(.2)
        list.sort()
        print(*list, sep=", ")
        time.sleep(.2)
        print("█   I couldn't make this any fancier because of math reasons   █")
        time.sleep(.2)
        print("█                                                              █")
        time.sleep(.2)
        print("████████████████████████████████████████████████████████████████")
        time.sleep(1)
        for _ in range(3):
            print("")
        time.sleep(.2)
    elif sorting_direction == "2":
        pass
    else:
        number_sorter()


def mean_and_total_finder():
    pass

def exit_quit():
    pass


def user_error():
    # USER ERROR section
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.2)
    print("█                                                              █")
    time.sleep(.2)
    print("█                    USER ERROR! TRY AGAIN!                    █")
    time.sleep(.5)
    print("█                                                              █")
    time.sleep(.2)
    print("████████████████████████████████████████████████████████████████")
    time.sleep(.5)


main_menu()
