s = " "


def check(inp):
    fwd = []
    rvs = []
    for i in inp:
        fwd.append(i)
    for i in fwd:
        rvs.insert(0, i)
    if fwd == rvs:
        return True
    else:
        return False


userInput = input("Enter a phrase/word: ")
userInput = userInput.lower()
checked = check(userInput)
if checked:
    print("That (\"" + userInput + "\") is a correct palindrome! Good job.")
else:
    print("Sorry, \"" + userInput + "\" is not a correct palindrome.")
