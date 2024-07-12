def returnFNRC(string):  # returnFirstNonRepeatingCharacter
    charList = []
    for cursor in string:
        charList.append(cursor)
    charList.sort()
    for var in charList:
        count = charList.count(var)
        if count > 1 and var != " ":
            continue
        elif count == 1 and var != " ":
            return var
    return "_"


print(returnFNRC(input("Enter string: ")))
