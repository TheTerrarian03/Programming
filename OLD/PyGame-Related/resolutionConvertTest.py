uInput = input("Enter a resolution: ")
firstLen = 0
secondLen = 0
i = 0

while True:
    if uInput[i] == "x":
        firstLen = i
        print("i = " + str(i))
        break
    else:
        i += 1

secondLen = len(uInput) - firstLen - 1

print("")
print(str(uInput[:firstLen]) + ": " + str(firstLen))
print(str(uInput[firstLen + 1:]) + ": " + str(secondLen))
