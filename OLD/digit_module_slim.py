# possible edit ' to make smaller but IDK
import time


def nls_slim(phrase):
    row_to_print = []
    x = 1
    while x < 8:
        for character in phrase:
            if character == "A":
                if x == 1:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 3 or x == 5 or x == 6 or x == 7:
                    row_to_print.append("█   █")
                elif x == 4:
                    row_to_print.append("█████")

            if character == "B":
                if x == 1 or x == 4 or x == 7:
                    row_to_print.append("████ ")
                elif x == 2 or x == 3 or x == 5 or x == 6:
                    row_to_print.append("█   █")

            if character == "C":
                if x == 1 or x == 7:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 6:
                    row_to_print.append("█   █")
                elif x == 3 or x == 4 or x == 5:
                    row_to_print.append("█    ")

            if character == "D":
                if x == 1 or x == 7:
                    row_to_print.append("████ ")
                elif x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
                    row_to_print.append("█   █")

            if character == "E":
                if x == 1 or x == 7:
                    row_to_print.append("█████")
                elif x == 2 or x == 3 or x == 5 or x == 6:
                    row_to_print.append("█    ")
                elif x == 4:
                    row_to_print.append("████ ")

            if character == "F":
                if x == 1:
                    row_to_print.append("█████")
                elif x == 2 or x == 3 or x == 5 or x == 6 or x == 7:
                    row_to_print.append("█    ")
                elif x == 4:
                    row_to_print.append("████ ")

            if character == "G":
                if x == 1:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 5 or x  == 6:
                    row_to_print.append("█   █")
                elif x == 3:
                    row_to_print.append("█    ")
                elif x == 4:
                    row_to_print.append("█ ███")
                else:
                    row_to_print.append(" ████")

            if character == "H":
                if x == 1 or x == 2 or x == 3 or x == 5 or x == 6 or x == 7:
                    row_to_print.append("█   █")
                elif x == 4:
                    row_to_print.append("█████")

            if character == "I":
                if x == 1 or x == 7:
                    row_to_print.append("█████")
                elif x == 2 or x == 3 or x == 4 or x == 5 or x ==6:
                    row_to_print.append("  █  ")

            if character == "J":
                if x == 1:
                    row_to_print.append("  ███")
                elif x == 2 or x == 3 or x == 4 or x == 5:
                    row_to_print.append("   █ ")
                elif x == 6:
                    row_to_print.append("█  █ ")
                else:
                    row_to_print.append(" ██  ")

            if character == "K":
                if x == 1 or x == 7:
                    row_to_print.append("█   █")
                elif x == 2 or x == 6:
                    row_to_print.append("█  █ ")
                elif x == 3 or x == 5:
                    row_to_print.append("█ █  ")
                elif x == 4:
                    row_to_print.append("██   ")

            if character == "L":
                if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
                    row_to_print.append("█    ")
                else:
                    row_to_print.append("█████")

            if character == "M":
                if x == 1 or x == 5 or x == 6 or x == 7:
                    row_to_print.append("█   █")
                elif x == 2:
                    row_to_print.append("██ ██")
                elif x == 3 or x == 4:
                    row_to_print.append("█ █ █")

            if character == "N":
                if x == 1 or x == 2 or x == 6 or x == 7:
                    row_to_print.append("█   █")
                elif x == 3:
                    row_to_print.append("██  █")
                elif x == 4:
                    row_to_print.append("█ █ █")
                elif x == 5:
                    row_to_print.append("█  ██")

            if character == "O":
                if x == 1 or x == 7:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
                    row_to_print.append("█   █")

            if character == "P":
                if x == 1 or x == 4:
                    row_to_print.append("████ ")
                elif x == 2 or x == 3:
                    row_to_print.append("█   █")
                elif x == 5 or x == 6 or x == 7:
                    row_to_print.append("█    ")

            if character == "Q":
                if x == 1:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 3 or x == 4:
                    row_to_print.append("█   █")
                elif x == 5:
                    row_to_print.append("█ █ █")
                elif x == 6:
                    row_to_print.append("█  █ ")
                else:
                    row_to_print.append(" ██ █")

            if character == "R":
                if x == 1 or x == 4:
                    row_to_print.append("████ ")
                elif x == 2 or x == 3:
                    row_to_print.append("█   █")
                elif x == 5:
                    row_to_print.append("█ █  ")
                elif x == 6:
                    row_to_print.append("█  █ ")
                else:
                    row_to_print.append("█   █")

            if character == "S":
                if x == 1:
                    row_to_print.append(" ████")
                elif x == 2 or x == 3:
                    row_to_print.append("█    ")
                elif x == 4:
                    row_to_print.append(" ███ ")
                elif x == 5 or x == 6:
                    row_to_print.append("    █")
                else:
                    row_to_print.append("████ ")

            if character == "T":
                if x == 1:
                    row_to_print.append("█████")
                elif x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7:
                    row_to_print.append("  █  ")

            if character == "U":
                if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
                    row_to_print.append("█   █")
                else:
                    row_to_print.append(" ███ ")

            if character == "V":
                if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                    row_to_print.append("█   █")
                elif x == 6:
                    row_to_print.append(" █ █ ")
                else:
                    row_to_print.append("  █  ")

            if character == "W":
                if x == 1 or x == 2 or x == 3:
                    row_to_print.append("█   █")
                elif x == 4 or x == 5 or x == 6:
                    row_to_print.append("█ █ █")
                else:
                    row_to_print.append(" █ █ ")

            if character == "X":
                if x == 1 or x == 2 or x == 6 or x == 7:
                    row_to_print.append("█   █")
                elif x == 3 or x == 5:
                    row_to_print.append(" █ █ ")
                elif x == 4:
                    row_to_print.append("  █  ")

            if character == "Y":
                if x == 1 or x == 2 or x == 3:
                    row_to_print.append("█   █")
                elif x == 4:
                    row_to_print.append(" █ █ ")
                elif x == 5 or x == 6 or x == 7:
                    row_to_print.append("  █  ")

            if character == "Z":
                if x == 1 or x == 7:
                    row_to_print.append("█████")
                elif x == 2:
                    row_to_print.append("    █")
                elif x == 3:
                    row_to_print.append("   █ ")
                elif x == 4:
                    row_to_print.append("  █  ")
                elif x == 5:
                    row_to_print.append(" █   ")
                elif x == 6:
                    row_to_print.append("█    ")

            if character == " ":
                if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7:
                    row_to_print.append("  ")

            if character == ".":
                if x == 6 or x == 7:
                    row_to_print.append(" ██  ")
                else:
                    row_to_print.append("     ")

            if character == "!":
                if x == 6:
                    row_to_print.append("     ")
                else:
                    row_to_print.append("  █  ")

            if character == ":":
                if x == 1 or x == 4 or x == 7:
                    row_to_print.append("     ")
                else:
                    row_to_print.append("  █  ")

            if character == ";":
                if x == 1 or x == 4 or x == 7:
                    row_to_print.append("     ")
                elif x == 2 or x == 3 or x == 5:
                    row_to_print.append("  █  ")
                elif x == 6:
                    row_to_print.append(" █   ")

            if character == "|":
                if x < 8:
                    row_to_print.append("  █  ")

            if character == "_":
                if x == 7:
                    row_to_print.append("█████")
                else:
                    row_to_print.append("     ")

            if character == "<":
                if x == 1 or x == 7:
                    row_to_print.append("   ██")
                elif x == 2 or x == 6:
                    row_to_print.append("  ██ ")
                elif x == 3 or x == 5:
                    row_to_print.append(" ██  ")
                elif x == 4:
                    row_to_print.append("██   ")

            if character == ">":
                if x == 1 or x == 7:
                    row_to_print.append("██   ")
                elif x == 2 or x == 6:
                    row_to_print.append(" ██  ")
                elif x == 3 or x == 5:
                    row_to_print.append("  ██ ")
                elif x == 4:
                    row_to_print.append("   ██")

            if character == "%":
                if x == 1:
                    row_to_print.append(" ██  ")
                elif x == 2:
                    row_to_print.append(" ██ █")
                elif x == 3:
                    row_to_print.append("   █ ")
                elif x == 4:
                    row_to_print.append("  █  ")
                elif x == 5:
                    row_to_print.append(" █   ")
                elif x == 6:
                    row_to_print.append("█ ██ ")
                else:
                    row_to_print.append("  ██ ")

            if character == "?":
                if x == 1:
                    row_to_print.append(" ███ ")
                elif x == 2:
                    row_to_print.append("█   █")
                elif x == 3:
                    row_to_print.append("    █")
                elif x == 4:
                    row_to_print.append("   █ ")
                elif x == 5:
                    row_to_print.append("  █  ")
                elif x == 6:
                    row_to_print.append("     ")
                else:
                    row_to_print.append("  █  ")

            if character == "^":
                if x == 1:
                    row_to_print.append("  █  ")
                elif x == 2:
                    row_to_print.append(" █ █ ")
                else:
                    row_to_print.append("     ")

            if character == "&":
                if x == 1 or x == 2:
                    row_to_print.append("     ")
                elif x == 3 or x == 5:
                    row_to_print.append(" █   ")
                elif x == 4:
                    row_to_print.append("█ █  ")
                elif x == 6:
                    row_to_print.append("█ █ █")
                else:
                    row_to_print.append(" █ █ ")

            if character == "$":
                if x == 1 or x == 7:
                    row_to_print.append("  █  ")
                elif x == 2:
                    row_to_print.append(" ████")
                elif x == 3:
                    row_to_print.append("█ █  ")
                elif x == 4:
                    row_to_print.append(" ███ ")
                elif x == 5:
                    row_to_print.append("  █ █")
                elif x == 6:
                    row_to_print.append("████ ")

            if character == "#":
                if x == 1 or x == 7:
                    row_to_print.append("     ")
                elif x == 2 or x == 4 or x == 6:
                    row_to_print.append(" █ █ ")
                elif x == 3 or x == 5:
                    row_to_print.append("█████")

            if character == "`":
                if x == 1:
                    row_to_print.append(" █   ")
                elif x == 2:
                    row_to_print.append("  █  ")
                else:
                    row_to_print.append("     ")

            if character == "~":
                if x == 3:
                    row_to_print.append(" █   ")
                elif x == 4:
                    row_to_print.append("█ █ █")
                elif x == 5:
                    row_to_print.append("   █ ")
                else:
                    row_to_print.append("     ")

            if character == "@":
                if x == 1 or x == 7:
                    row_to_print.append("     ")
                elif x == 2:
                    row_to_print.append(" ██  ")
                elif x == 3:
                    row_to_print.append("█  █ ")
                elif x == 4:
                    row_to_print.append("█ ██ ")
                elif x == 5:
                    row_to_print.append("█    ")
                elif x == 6:
                    row_to_print.append(" ████")

            if character == "(":
                if x == 1 or x == 7:
                    row_to_print.append("  █")
                elif x == 2 or x == 6:
                    row_to_print.append(" █ ")
                elif x == 3 or x == 4 or x == 5:
                    row_to_print.append("█  ")

            if character == ")":
                if x == 1 or x == 7:
                    row_to_print.append("█  ")
                elif x == 2 or x == 6:
                    row_to_print.append(" █ ")
                elif x == 3 or x == 4 or x == 5:
                    row_to_print.append("  █")

            if character == "[":
                if x == 1 or x == 7:
                    row_to_print.append("███")
                else:
                    row_to_print.append("█  ")

            if character == "]":
                if x == 1 or x == 7:
                    row_to_print.append("███")
                else:
                    row_to_print.append("  █")

            if character == "{":
                if x == 1 or x == 7:
                    row_to_print.append("  ██")
                elif x == 4:
                    row_to_print.append("█   ")
                else:
                    row_to_print.append(" █  ")

            if character == "}":
                if x == 1 or x == 7:
                    row_to_print.append("██  ")
                elif x == 4:
                    row_to_print.append("   █")
                else:
                    row_to_print.append("  █ ")

            if character == "+":
                if x == 1 or x == 7:
                    row_to_print.append("     ")
                elif x == 4:
                    row_to_print.append("█████")
                else:
                    row_to_print.append("  █  ")


            if character == "-":
                if x == 4:
                    row_to_print.append("█████")
                else:
                    row_to_print.append("     ")

            if character == "*":
                if x == 1 or x == 7:
                    row_to_print.append("     ")
                elif x == 2 or x == 6:
                    row_to_print.append("  █  ")
                elif x == 3 or x == 5:
                    row_to_print.append("█ █ █")
                elif x == 4:
                    row_to_print.append(" ███ ")

            if character == "=":
                if x == 3 or x == 5:
                    row_to_print.append("█████")
                else:
                    row_to_print.append("     ")

            if character == "/":
                if x == 1 or x == 2:
                    row_to_print.append("    █")
                elif x == 3:
                    row_to_print.append("   █ ")
                elif x == 4:
                    row_to_print.append("  █  ")
                elif x == 5:
                    row_to_print.append(" █   ")
                elif x == 6 or x == 7:
                    row_to_print.append("█    ")

            if character == "\\":
                if x == 1 or x == 2:
                    row_to_print.append("█    ")
                elif x == 3:
                    row_to_print.append(" █   ")
                elif x == 4:
                    row_to_print.append("  █  ")
                elif x == 5:
                    row_to_print.append("   █ ")
                elif x == 6 or x == 7:
                    row_to_print.append("    █")

            if character == ",":
                if x == 5:
                    row_to_print.append(" ██  ")
                elif x == 6:
                    row_to_print.append("  █  ")
                elif x == 7:
                    row_to_print.append(" █   ")
                else:
                    row_to_print.append("     ")

            if character == "'":
                if x == 1 or x == 2:
                    row_to_print.append("  █  ")
                else:
                    row_to_print.append("     ")

            if character == "\"":
                if x == 1 or x == 2:
                    row_to_print.append(" █ █ ")
                else:
                    row_to_print.append("     ")

            if character == "0":
                if x == 1 or x == 7:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 6:
                    row_to_print.append("█   █")
                elif x == 3:
                    row_to_print.append("█  ██")
                elif x == 4:
                    row_to_print.append("█ █ █")
                elif x == 5:
                    row_to_print.append("██  █")

            if character == "1":
                if x == 2:
                    row_to_print.append(" ██  ")
                elif x == 7:
                    row_to_print.append(" ███ ")
                else:
                    row_to_print.append("  █  ")

            if character == "2":
                if x == 1:
                    row_to_print.append(" ███ ")
                elif x == 2:
                    row_to_print.append("█   █")
                elif x == 3:
                    row_to_print.append("    █")
                elif x == 4:
                    row_to_print.append("   █ ")
                elif x == 5:
                    row_to_print.append("  █  ")
                elif x == 6:
                    row_to_print.append(" █   ")
                else:
                    row_to_print.append("█████")

            if character == "3":
                if x == 1:
                    row_to_print.append("█████")
                elif x == 2 or x == 4:
                    row_to_print.append("   █ ")
                elif x == 3:
                    row_to_print.append("  █  ")
                elif x == 5:
                    row_to_print.append("    █")
                elif x == 6:
                    row_to_print.append("█   █")
                else:
                    row_to_print.append(" ███ ")

            if character == "4":
                if x == 1 or x == 2 or x == 3:
                    row_to_print.append("█   █")
                elif x == 4:
                    row_to_print.append("█████")
                else:
                    row_to_print.append("    █")

            if character == "5":
                if x == 1:
                    row_to_print.append("█████")
                elif x == 2:
                    row_to_print.append("█    ")
                elif x == 3:
                    row_to_print.append("████ ")
                elif x == 4 or x == 5:
                    row_to_print.append("    █")
                elif x == 6:
                    row_to_print.append("█   █")
                else:
                    row_to_print.append(" ███ ")

            if character == "6":
                if x == 1:
                    row_to_print.append("  █  ")
                elif x == 2:
                    row_to_print.append(" █   ")
                elif x == 3:
                    row_to_print.append("█    ")
                elif x == 4:
                    row_to_print.append("████ ")
                elif x == 5 or x == 6:
                    row_to_print.append("█   █")
                else:
                    row_to_print.append(" ███ ")

            if character == "7":
                if x == 1:
                    row_to_print.append("█████")
                elif x == 2:
                    row_to_print.append("    █")
                elif x == 3:
                    row_to_print.append("   █ ")
                elif x == 4:
                    row_to_print.append("█████")
                else:
                    row_to_print.append("  █  ")

            if character == "8":
                if x == 1 or x == 4 or x == 7:
                    row_to_print.append(" ███ ")
                else:
                    row_to_print.append("█   █")

            if character == "9":
                if x == 1:
                    row_to_print.append(" ███ ")
                elif x == 2 or x == 3:
                    row_to_print.append("█   █")
                elif x == 4:
                    row_to_print.append(" ████")
                elif x == 5:
                    row_to_print.append("    █")
                elif x == 6:
                    row_to_print.append("   █ ")
                else:
                    row_to_print.append(" ██  ")

        print(*row_to_print, sep="  ")
        x += 1
        row_to_print = []


if __name__ == "__main__":
    print("This module lets the user print out any combination of numbers, letters, and symbols")
    print("by importing this module, then calling the function \"nls()\".")
    print("Inside the parenthesis, goes the string of the \"phrase\".")
    print("Here is a demo: ")
    print("")

    phrase_to_input = input("Enter a phrase: ")
    nls_slim(phrase_to_input)
    time.sleep(10)
