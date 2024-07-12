import time


def timer():
    for countdown in range(10):
        print(10 - countdown)
        time.sleep(1)
    print("Go!")
    time.sleep(1)
    s = 0
    m = 0
    for _ in range(31536000):
        print(str(m) + "m : " + str(s) + "s")
        s += 1
        time.sleep(1)
        if s == 60:
            s -= 60
            m += 1


def stupid():
    print("█████      █████  █████")
    print("█   █  ██  █   █  █   █")
    print("█   █      █   █  █   █")
    print("█   █  ██  █   █  █   █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████    █")
    print("█   █  ██  █   █   ██")
    print("█   █      █   █    █")
    print("█   █  ██  █   █    █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █      █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █  █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █      █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █      █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████  █   █")
    print("█   █  ██  █   █  █   █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █      █")
    print("█████      █████      █")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █  █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █      █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █  █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █  █   █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █      █")
    print("█   █      █   █    ███")
    print("█   █  ██  █   █      █")
    print("█████      █████      █")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █  █   █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █  █   █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("█████      █████  █████")
    print("█   █  ██  █   █  █   █")
    print("█   █      █   █  █████")
    print("█   █  ██  █   █      █")
    print("█████      █████      █")
    print("")

    time.sleep(1)

    print("█████        █    █████")
    print("█   █  ██   ██    █   █")
    print("█   █        █    █   █")
    print("█   █  ██    █    █   █")
    print("█████      █████  █████")
    print("")

    time.sleep(1)

    print("   ██   ██")
    print("")
    print("██         ██")
    print("  █████████")
    print("hehehehehehe You're Welcome!")
    time.sleep(1)
    Assurance()


def Assurance():
    print("Ready to start countdown?")
    start = input()
    if start == "y" or start == "yes" or start == "Yes":
        print("Ok.")
        time.sleep(1)
        print("Here we go:")
        time.sleep(1)
        timer()
    elif start == "stupid":
        stupid()
    else:
        Assurance()


'''
def time_jumper(seconds_in_future):
'''


Assurance()