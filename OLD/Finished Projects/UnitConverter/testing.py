list = []


def again():
    print("RESET")
    list = []
    while True:
        a = input("Character: ")
        if a == "-1":
            break
        elif a == "-2":
            again()
        else:
            list.append(a)

    print(list)


while True:
    a = input("Character: ")
    if a == "-1":
        break
    elif a == "-2":
        again()
    else:
        list.append(a)

print(list)
