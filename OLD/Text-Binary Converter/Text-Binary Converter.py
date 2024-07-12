import time

# first, some variables
conversionList = {
    " ": "00100000",
    "!": "00100001",
    "\"": "00100010",
    "#": "00000011",
    "$": "00100100",
    "%": "00100101",
    "&": "00100110",
    "'": "00100111",
    "(": "00101000",
    ")": "00101001",
    "*": "00101010",
    "+": "00101011",
    ",": "00101100",
    "-": "00101101",
    ".": "00101110",
    "/": "00101111",
    "0": "00110000",
    "1": "00110001",
    "2": "00110010",
    "3": "00110011",
    "4": "00110100",
    "5": "00110101",
    "6": "00110110",
    "7": "00110111",
    "8": "00111000",
    "9": "00111001",
    ":": "00111010",
    ";": "00111011",
    "<": "00111100",
    "=": "00111101",
    ">": "00111110",
    "?": "00111111",
    "@": "01000000",
    "A": "01000001",
    "B": "01000010",
    "C": "01000011",
    "D": "01000100",
    "E": "01000101",
    "F": "01000110",
    "G": "01000111",
    "H": "01001000",
    "I": "01001001",
    "J": "01001010",
    "K": "01001011",
    "L": "01001100",
    "M": "01001101",
    "N": "01001110",
    "O": "01001111",
    "P": "01010000",
    "Q": "01010001",
    "R": "01010010",
    "S": "01010011",
    "T": "01010100",
    "U": "01010101",
    "V": "01010110",
    "W": "01010111",
    "X": "01011000",
    "Y": "01011001",
    "Z": "01011010",
    "[": "01011011",
    "\\": "01011100",
    "]": "01011101",
    "^": "01011110",
    "_": "01011111",
    "`": "01100000",
    "a": "01100001",
    "b": "01100010",
    "c": "01100011",
    "d": "01100100",
    "e": "01100101",
    "f": "01100110",
    "g": "01100111",
    "h": "01101000",
    "i": "01101001",
    "j": "01101010",
    "k": "01101011",
    "l": "01101100",
    "m": "01101101",
    "n": "01101110",
    "o": "01101111",
    "p": "01110000",
    "q": "01110001",
    "r": "01110010",
    "s": "01110011",
    "t": "01110100",
    "u": "01110101",
    "v": "01110110",
    "w": "01110111",
    "x": "01111000",
    "y": "01111001",
    "z": "01111010",
    "{": "01111011",
    "|": "01111100",
    "}": "01111101",
    "~": "01111110",
    "/enter/": "00001010"
}

# somethingNiceForLogan = "Logan is a very handsome young man with a studly mustache ;)"


def t(l=.25):
    time.sleep(l)


def get_input():
    uIList = []
    print()
    t()
    print("Okay, now please enter what you want to convert:")
    t()
    print("When you are done, type \"-1\", and \"/r\" to restart.")
    t()
    print("Type here:")
    t()
    print()
    done = False

    while not done:
        uI_temp = input()

        if uI_temp == "-1":
            done = True
        elif uI_temp == "/r":
            t()
            print()
            t()
            print("*/ RESTARTED */")
            t()
        else:
            split = list(uI_temp)
            for i in split:
                uIList.append(i)
            uIList.append("/enter/")

    return uIList


def tob():
    t()
    print()
    t()
    print("Are you converting text (1) or binary (2)?")
    t()
    user_input = input("Please enter one: ")
    if user_input == "1":
        ConvertText()
    elif user_input == "2":
        ConvertBinary()
    else:
        print()
        t()
        print("It looks like you have typed something wrong. Let's restart:")
        tob()


def sp():
    t()
    print()
    t()
    spaces_present = input("Enter whether there are spaces present (y/n): ")
    if spaces_present.lower() == "y":
        return True
    elif spaces_present.lower() == "n":
        return False
    else:
        print()
        t()
        print("It looks like you have typed something wrong. Let's restart:")
        sp()


def ConvertText():
    uI = get_input()
    end_product = []

    for i in uI:
        for e in conversionList:
            if i == e:
                end_product.append(conversionList.get(e))

    print()
    t()
    print("Here is your text, converted:")
    t()
    print()
    t()
    print("With out spaces:")
    t()
    print(*end_product, sep="")
    t()
    print()
    t()
    print("With spaces:")
    t()

    # adds spaces every 8 characters to end_product2
    end_product2 = []
    for i in range(len(end_product)):
        end_product2.append(end_product[i])

    print(*end_product2)
    t()
    print()
    t()
    print("Done!")
    askRestart()


def ConvertBinary():
    def convert(list):
        new = ""
        for x in list:
            new += x
        return new

    uI1 = get_input()
    end_product = []

    spaces_present = sp()

    i = 0
    while i <= len(uI1):
        try:
            temp_list = []
            for _ in range(8):
                temp_list.append(uI1[i])
                i += 1
            if spaces_present:
                i += 1

            for key, value in conversionList.items():
                if convert(temp_list) == value:
                    if key == "/enter/":
                        end_product.append("\n")
                    else:
                        end_product.append(key)
        except IndexError:
            break

    print()
    t()
    print("Here is your text, converted:")
    t()
    print(*end_product, sep="")

    t()
    print("Done!")
    askRestart()


def welcomeMessage():
    print("Well hello there!")
    t()
    print("Welcome to my Text-To-Binary Converter (and vice versa)")
    t()
    print("First, you'll need to enter whether you're converting text or binary.")

    tob()


def askRestart():
    t()
    print()
    t()
    restartAnswer = input("Do you want to start again? (y/n): ")
    if restartAnswer.lower() == "y":
        t()
        print()
        t()
        welcomeMessage()
    else:
        quit()


welcomeMessage()
