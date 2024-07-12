from random import randint


def main():
    y = ""
    list = []
    length = int(input("Enter number of digits: "))
    for _ in range(1, (length + 1)):
        x = randint(1, 26)
        if x == "1":
            y = "a"
        if x == "2":
            y = "b"
        if x == "3":
            y = "c"
        if x == "4":
            y = "d"
        if x == "5":
            y = "e"
        if x == "6":
            y = "f"
        if x == "7":
            y = "g"
        if x == "8":
            y = "h"
        if x == "9":
            y = "i"
        if x == "10":
            y = "j"
        if x == "11":
            y = "k"
        if x == "12":
            y = "l"
        if x == "13":
            y = "m"
        if x == "14":
            y = "n"
        if x == "15":
            y = "o"
        if x == "16":
            y = "p"
        if x == "17":
            y = "q"
        if x == "18":
            y = "r"
        if x == "19":
            y = "s"
        if x == "20":
            y = "t"
        if x == "21":
            y = "u"
        if x == "22":
            y = "v"
        if x == "23":
            y = "w"
        if x == "24":
            y = "x"
        if x == "25":
            y = "y"
        if x == "26":
            y = "z"
        print(x)
        print(y)



main()

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*():;"'|\}]{[<>?,./~` = 90 char.