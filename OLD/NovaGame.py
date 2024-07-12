import random
import time
s = ""
se = "                      "
cardList = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cardColor = "Blue"
suck = "You Suck at entering words! Try again."


class Person:
    def __init__(self, name):
        self.name = name
        self.c_card = None
        self.card1 = None
        self.card2 = None
        self.card3 = None
        self.score = 0

    def draw_card(self):
        self.c_card = random.choice(cardList)

    def draw_more_cards(self):
        self.card1 = random.choice(cardList)
        self.card2 = random.choice(cardList)
        self.card3 = random.choice(cardList)

    def add_point(self):
        self.score += 1


def print_cards(one, two):
    tl = []
    tl.append(str(one.c_card))
    tl.append(s)
    tl.append(str(two.c_card))
    print(tl)
    print(*tl)

    pl = []
    row = 1
                    # add quotes around "sym" numbers!
    while row < 18:
        for sym in tl:
            if sym == "2":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██            ██    ██")
                elif row == 8:
                    pl.append("██            ██    ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██    ██            ██")
                elif row == 11:
                    pl.append("██    ██            ██")
                elif row == 12:
                    pl.append("██    ██████████    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "3":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██            ██    ██")
                elif row == 8:
                    pl.append("██            ██    ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██            ██    ██")
                elif row == 11:
                    pl.append("██            ██    ██")
                elif row == 12:
                    pl.append("██    ██████████    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "4":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██      ██    ██")
                elif row == 7:
                    pl.append("██    ██      ██    ██")
                elif row == 8:
                    pl.append("██    ██      ██    ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██            ██    ██")
                elif row == 11:
                    pl.append("██            ██    ██")
                elif row == 12:
                    pl.append("██            ██    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "5":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██    ██            ██")
                elif row == 8:
                    pl.append("██    ██            ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██            ██    ██")
                elif row == 11:
                    pl.append("██            ██    ██")
                elif row == 12:
                    pl.append("██    ██████████    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "6":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██    ██            ██")
                elif row == 8:
                    pl.append("██    ██            ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██    ██      ██    ██")
                elif row == 11:
                    pl.append("██    ██      ██    ██")
                elif row == 12:
                    pl.append("██    ██████████    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "7":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██            ██    ██")
                elif row == 8:
                    pl.append("██            ██    ██")
                elif row == 9:
                    pl.append("██            ██    ██")
                elif row == 10:
                    pl.append("██            ██    ██")
                elif row == 11:
                    pl.append("██            ██    ██")
                elif row == 12:
                    pl.append("██            ██    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "8":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██    ██      ██    ██")
                elif row == 8:
                    pl.append("██    ██      ██    ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██    ██      ██    ██")
                elif row == 11:
                    pl.append("██    ██      ██    ██")
                elif row == 12:
                    pl.append("██    ██████████    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "9":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██    ██      ██    ██")
                elif row == 8:
                    pl.append("██    ██      ██    ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██            ██    ██")
                elif row == 11:
                    pl.append("██            ██    ██")
                elif row == 12:
                    pl.append("██            ██    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "10":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██  ██    ██████    ██")
                elif row == 7:
                    pl.append("██  ██  ██      ██  ██")
                elif row == 8:
                    pl.append("██  ██  ██    ████  ██")
                elif row == 9:
                    pl.append("██  ██  ██  ██  ██  ██")
                elif row == 10:
                    pl.append("██  ██  ████    ██  ██")
                elif row == 11:
                    pl.append("██  ██  ██      ██  ██")
                elif row == 12:
                    pl.append("██  ██    ██████    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "11":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██████████    ██")
                elif row == 7:
                    pl.append("██          ██      ██")
                elif row == 8:
                    pl.append("██          ██      ██")
                elif row == 9:
                    pl.append("██          ██      ██")
                elif row == 10:
                    pl.append("██          ██      ██")
                elif row == 11:
                    pl.append("██    ██    ██      ██")
                elif row == 12:
                    pl.append("██      ████        ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "12":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██      ██████      ██")
                elif row == 7:
                    pl.append("██    ██      ██    ██")
                elif row == 8:
                    pl.append("██    ██      ██    ██")
                elif row == 9:
                    pl.append("██    ██      ██    ██")
                elif row == 10:
                    pl.append("██    ██  ██  ██    ██")
                elif row == 11:
                    pl.append("██    ██    ██      ██")
                elif row == 12:
                    pl.append("██      ████  ██    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "13":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██    ██      ██    ██")
                elif row == 7:
                    pl.append("██    ██    ██      ██")
                elif row == 8:
                    pl.append("██    ██  ██        ██")
                elif row == 9:
                    pl.append("██    ████          ██")
                elif row == 10:
                    pl.append("██    ██  ██        ██")
                elif row == 11:
                    pl.append("██    ██    ██      ██")
                elif row == 12:
                    pl.append("██    ██      ██    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == "20":
                if row == 1:
                    pl.append("  ██████████████████  ")
                elif row == 2:
                    pl.append("████████        ██████")
                elif row == 3:
                    pl.append("██████            ████")
                elif row == 4:
                    pl.append("████                ██")
                elif row == 5:
                    pl.append("██                  ██")
                elif row == 6:
                    pl.append("██      ██████      ██")
                elif row == 7:
                    pl.append("██    ██      ██    ██")
                elif row == 8:
                    pl.append("██    ██      ██    ██")
                elif row == 9:
                    pl.append("██    ██████████    ██")
                elif row == 10:
                    pl.append("██    ██      ██    ██")
                elif row == 11:
                    pl.append("██    ██      ██    ██")
                elif row == 12:
                    pl.append("██    ██      ██    ██")
                elif row == 13:
                    pl.append("██                  ██")
                elif row == 14:
                    pl.append("██                ████")
                elif row == 15:
                    pl.append("████            ██████")
                elif row == 16:
                    pl.append("██████        ████████")
                elif row == 17:
                    pl.append("  ██████████████████")
            if sym == " ":
                pl.append(se)
            print(*pl)
            row += 1
            pl = []


def game(one, two):
    time.sleep(1)
    points_found = False
    while not points_found:
        one.draw_card()
        two.draw_card()
        print_cards(one, two)
        who = input("Who won?\n")
        who = who.capitalize()
        if who == one.name:
            if one.c_card > two.c_card:
                print("Correct! One point added to " + one.name)
            else:
                print("Incorrect! " + two.name + " won! One point added to " + two.name)
        elif who == two.name:
            if two.c_card > one.c_card:
                print("Correct! One pint added to " + two.name)
            else:
                print("Incorrect! " + one.name + " won! One point added to " + one.name)
        else:
            print(suck)
            if one.c_card > two.c_card:
                print(one.name + " won! One point added to " + one.name)
            else:
                print(two.name + " won! One point added to " + two.name)

        if one.c_card > two.c_card:
            one.add_point()
        else:
            two.add_point()

        if one.score == 1:
            print(one.name + " has " + str(one.score) + " point!")
        else:
            print(one.name + " has " + str(one.score) + " points!")
        if two.score == 1:
            print(two.name + " has " + str(two.score) + " point!")
        else:
            print(two.name + " has " + str(two.score) + " points!")

        time.sleep(.5)


def main():
    print("This game is called War.")
    print("Made by Nova and Logan")

    name1 = input("The first player's name:  ")
    name2 = input("The second player's name: ")
    name1 = name1.capitalize()
    name2 = name2.capitalize()

    one = Person(name1)
    two = Person(name2)

    print(s)
    print("First person:  " + one.name + " with " + str(one.score) + " points.")
    print("Second person: " + two.name + " with " + str(two.score) + " points.")
    print(s)

    go = None
    while True:
        go = input("Would you like to start the game? Answer y/n: ")
        go = go.lower()
        if go == "y":
            game(one, two)
            break
        elif go == "n":
            print("Okay, quitting game.")
            time.sleep(1)
            break
        else:
            print(suck)


main()
