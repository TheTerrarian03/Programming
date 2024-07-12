import random
s = " "


def mainloop():
    while True:
        userInput = input("Enter some text:\n")

        if userInput.lower() == "break" or userInput.lower() == "stop":
            break

        choices = ["I am depressed", "I hate my life", "I'm sad", "I'm ugly", "I just got ran over by a car",
                   "my dog left me...", "there is only one potato chip left"]
        numChoices = [0, 1, 2, 3, 4, 5, 6]
        endText = []
        lenVar = 0
        while True:
            if lenVar <= len(userInput):
                randNum = random.choice(numChoices)
                endText.append(choices[randNum])
                lenVar += len(choices[randNum])
                if lenVar <= len(userInput):
                    endText.append("and")
                    lenVar += 3
            else:
                endText.append(":(")
                break
        print(s)
        print(*endText)
        print(s)


mainloop()
