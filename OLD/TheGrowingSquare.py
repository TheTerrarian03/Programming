import time


def ready():
    print("Are you ready?")
    YesOrNo = input()
    if YesOrNo == "yes":
        GrowingSquareCommence()
    else:
        print("Try again.")
        ready()


def GrowingSquareCommence():
    time.sleep(1)
    print("[]")
    time.sleep(.1)
    for _ in range(2):
        print("+-+")
    time.sleep(.1)
    print("+----+")
    print("|    |")
    print("+----+")
    time.sleep(.1)
    print("+-------+")
    for _ in range(2):
        print("|       |")
    print("+-------+")
    time.sleep(.1)
    print("+----------+")
    for _ in range(3):
        print("|          |")
    print("+----------+")
    time.sleep(.1)
    print("+-------------+")
    for _ in range(4):
        print("|             |")
    print("+-------------+")
    time.sleep(.1)
    print("+----------------+")
    for _ in range(5):
        print("|                |")
    print("+----------------+")
    time.sleep(.1)
    print("+-------------------+")
    for _ in range(6):
        print("|                   |")
    print("+-------------------+")
    time.sleep(.1)
    print("+----------------------+")
    for _ in range(7):
        print("|                      |")
    print("+----------------------+")
    time.sleep(.1)
    print("+-------------------------+")
    for _ in range(8):
        print("|                         |")
    print("+-------------------------+")
    time.sleep(.1)
    print("+-------------------------+")
    for _ in range(9):
        print("|                         |")
    print("+-------------------------+")
    time.sleep(.1)
    print("+----------------------------+")
    for _ in range(10):
        print("|                            |")
    print("+----------------------------+")
    time.sleep(.1)
    print("+-------------------------------+")
    for _ in range(11):
        print("|                               |")
    print("+-------------------------------+")
    time.sleep(.1)
    print("+----------------------------------+")
    for _ in range(12):
        print("|                                  |")
    print("+----------------------------------+")
    time.sleep(.1)
    print("+-------------------------------------+")
    for _ in range(13):
        print("|                                     |")
    print("+-------------------------------------+")
    time.sleep(.1)
    print("+----------------------------------------+")
    for _ in range(14):
        print("|                                        |")
    print("+----------------------------------------+")
    time.sleep(.1)
    print("+-------------------------------------------+")
    for _ in range(15):
        print("|                                           |")
    print("+-------------------------------------------+")


ready()