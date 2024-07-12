
def number(number):
    if number == "1":
        pass
        

def symbol(symbol):
    if symbol == ".":
        for _ in range(5):
            print("")
        print(" ██  ")
        print(" ██  ")
        
    elif symbol == "!":
        for _ in range(4):
            print("  █")
        print("")
        print("  █")
        print("  █")
        
    elif symbol == ":":
        print("")
        print(" ██")
        print(" ██")
        print("")
        print(" ██")
        print(" ██")
        print("")
        
    elif symbol == "<":
        print("   ██")
        print("  ██")
        print(" ██")
        print("██")
        print(" ██")
        print("  ██")
        print("   ██")
        
    elif symbol == ">":
        print("██")
        print(" ██")
        print("  ██")
        print("   ██")
        print("  ██")
        print(" ██")
        print("██")
        
    elif symbol == "<=":
        print("    █")
        print("  ██")
        print("██")
        print("  ██")
        print("    █")
        print("")
        print("█████")
        
    elif symbol == ">=":
        print("█")
        print(" ██")
        print("   ██")
        print(" ██")
        print("█")
        print("")
        print("█████")
        
    elif symbol == "%":
        print(" ██")
        print(" ██ █")
        print("   █")
        print("  █")
        print(" █")
        print("█ ██")
        print("  ██")
        
    elif symbol == "(":
        print("  █")
        print(" █")
        for _ in range(3):
            print("█")
        print(" █")
        print("  █")
    
    elif symbol == ")":
        print("█")
        print(" █")
        for _ in range(3):
            print("  █")
        print(" █")
        print("█")
        
    elif symbol == "[":
        print("██")
        for _ in range(5):
            print(" █")
        print("██")
        
    elif symbol == "]":
        print("██")
        for _ in range(5):
            print("█")
        print("██")
        
    elif symbol == "{":
        print("  ██")
        print(" █")
        print(" █")
        print("█")
        print(" █")
        print(" █")
        print("  ██")
        
    elif symbol == "}":
        print("██")
        print("  █")
        print("  █")
        print("   █")
        print("  █")
        print("  █")
        print("██")
        
    elif symbol == "+":
        print("")
        print("  █")
        print("  █")
        print("█████")
        print("  █")
        print("  █")
        print("")
        
    elif symbol == "-":
        for _ in range(3):
            print("")
        print("█████")
        for _ in range(3):
            print("")
            
    elif symbol == "*":
        print("")
        print("  █")
        print("█ █ █")
        print(" ███")
        print("█ █ █")
        print("  █")
        print("")
        
    elif symbol == "/":
        print("")
        print("    █")
        print("   █")
        print("  █")
        print(" █")
        print("█")
        print("")


def letter(letter):
    if letter == "A":
        print(" ███")
        print("█   █")
        print("█   █")
        print("█████")
        print("█   █")
        print("█   █")
        print("█   █")

    elif letter == "B":
        print("████")
        print("█   █")
        print("█   █")
        print("████")
        print("█   █")
        print("█   █")
        print("████")

    elif letter == "C":
        print(" ███")
        print("█   █")
        print("█")
        print("█")
        print("█")
        print("█   █")
        print(" ███")

    elif letter == "D":
        print("████")
        for _ in range(5):
            print("█   █")
        print("████")

    elif letter == "E":
        print("█████")
        print("█")
        print("█")
        print("████")
        print("█")
        print("█")
        print("█████")

    elif letter == "F":
        print("█████")
        print("█")
        print("█")
        print("████")
        for _ in range(3):
            print("█")

    elif letter == "G":
        print(" ███")
        print("█   █")
        print("█")
        print("█ ███")
        print("█   █")
        print("█   █")
        print(" ████")

    elif letter == "H":
        for _ in range(3):
            print("█   █")
        print("█████")
        for _ in range(3):
            print("█   █")

    elif letter == "I":
        print("█████")
        for _ in range(5):
            print("  █")
        print("██████")

    elif letter == "J":
        print("  ███")
        for _ in range(4):
            print("   █")
        print("█  █")
        print(" ██")

    elif letter == "K":
        print("█   █")
        print("█  █")
        print("█ █")
        print("██")
        print("█ █")
        print("█  █")
        print("█   █")

    elif letter == "L":
        for _ in range(6):
            print("█")
        print("█████")

    elif letter == "M":
        print("█   █")
        print("██ ██")
        print("█ █ █")
        print("█ █ █")
        for _ in range(3):
            print("█   █")

    elif letter == "N":
        print("█   █")
        print("█   █")
        print("██  █")
        print("█ █ █")
        print("█  ██")
        print("█   █")
        print("█   █")

    elif letter == "O":
        print(" ███")
        for _ in range(5):
            print("█   █")
        print(" ███")

    elif letter == "P":
        print("████")
        print("█   █")
        print("█   █")
        print("████")
        for _ in range(3):
            print("█")

    elif letter == "Q":
        print(" ███")
        for _ in range(3):
            print("█   █")
        print("█ █ █")
        print("█  █")
        print(" ██ █")

    elif letter == "R":
        print("████")
        print("█   █")
        print("█   █")
        print("████")
        print("█ █")
        print("█  █")
        print("█   █")

    elif letter == "S":
        print(" ████")
        print("█")
        print("█")
        print(" ███")
        print("    █")
        print("    █")
        print("████")

    elif letter == "T":
        print("█████")
        for _ in range(6):
            print("  █")

    elif letter == "U":
        for _ in range(6):
            print("█   █")
        print(" ███")

    elif letter == "V":
        for _ in range(5):
            print("█   █")
        print(" █ █")
        print("  █")

    elif letter == "W":
        for _ in range(3):
            print("█   █")
        for _ in range(3):
            print("█ █ █")
        print(" █ █")

    elif letter == "X":
        print("█   █")
        print("█   █")
        print(" █ █")
        print("  █")
        print(" █ █")
        print("█   █")
        print("█   █")

    elif letter == "Y":
        for _ in range(3):
            print("█   █")
        print(" █ █")
        for _ in range(3):
            print("  █")

    elif letter == "Z":
        print("█████")
        print("    █")
        print("   █")
        print("  █")
        print(" █")
        print("█")
        print("█████")