s = " "


def findDupesString(uStr):
    pass


def findDupesList(uList):
    pass


def removeDupesString(uStr):
    pass


def removeDupesList(uList):
    pass


itemType = input("What are your items? (\"string\" or \"list\"): ")
if itemType.lower() == "string":
    isCap = input("is your string case-sensitive? (y/n): ")
    if isCap.lower() == "y":
        uString = input("Enter your string here: ")
    else:
        uString = input("Enter your string here:")
        uString = uString.upper()
    print("Your string is: " + uString)
else:
    isCap = input("Are your list items case-sensitive? (y/n): ")
    if isCap.lower() == "y":
        uListLen = int(input("How many items are in your list? (PLEASE ENTER A NUMBER!): "))
        uL = []
        for i in range(uListLen):
            j = input("Enter the data for item #" + str(i + 1) + ": ")
            uL.append(j)
        print(s)
        print("Your list is:")
        print(*uL, sep=", ")
    else:
        uListLen = int(input("How many items are in your list? (PLEASE ENTER A NUMBER!): "))
        uL = []
        for i in range(uListLen):
            j = input("Enter the data for item #" + str(i + 1) + ": ")
            uL.append(j.upper())
        print(s)
        print("Your list is:")
        print(*uL, sep=", ")

if itemType.lower() == "string":
    print(findDupesString(uString))
