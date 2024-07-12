import random


def main():
    tests = input("How many times is the bug tested? (THere can be no more than 100 times) ")
    for time in range(1, (int(tests)) + 1):
        if time == 1:
            timeGrammarCorrected = "1st"
        if time == 2:
            timeGrammarCorrected = "2nd"
        if time == 21:
            timeGrammarCorrected = "21st"
        if time == 31:
            timeGrammarCorrected = "31st"
        if time == 41:
            timeGrammarCorrected = "41st"
        if time == 51:
            timeGrammarCorrected = "51st"
        if time == 61:
            timeGrammarCorrected = "61st"
        if time == 71:
            timeGrammarCorrected = "71st"
        if time == 81:
            timeGrammarCorrected = "81st"
        if time == 91:
            timeGrammarCorrected = "91st"
        if time == 22:
            timeGrammarCorrected = "22nd"
        if time == 32:
            timeGrammarCorrected = "32nd"
        if time == 42:
            timeGrammarCorrected = "42nd"
        if time == 52:
            timeGrammarCorrected = "52nd"
        if time == 62:
            timeGrammarCorrected = "62nd"
        if time == 72:
            timeGrammarCorrected = "72nd"
        if time == 82:
            timeGrammarCorrected = "82nd"
        if time == 92:
            timeGrammarCorrected = "92nd"
        if time == 23:
            timeGrammarCorrected = "23rd"
        if time == 33:
            timeGrammarCorrected = "33rd"
        if time == 43:
            timeGrammarCorrected = "43rd"
        if time == 53:
            timeGrammarCorrected = "53rd"
        if time == 63:
            timeGrammarCorrected = "63rd"
        if time == 73:
            timeGrammarCorrected = "73rd"
        if time == 83:
            timeGrammarCorrected = "83rd"
        if time == 93:
            timeGrammarCorrected = "93rd"
        else:
            timeGrammarCorrected = str(time) + "th"


        print("The bug was", (random.choice([" Alive          ", " Dead           ", " Maybe Alive    ",\
" Probably Alive ", " Probably Dead  "])),"When tested the", timeGrammarCorrected, "time")


main()