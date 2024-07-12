import time
s = " "


def main():
    def check(string):
        if not string.isdecimal():
            print("Good job, that is a correct palindrome. I am not advanced enough\n"
                  "to figure out the next one though, because this one doesn't have numbers.\n"
                  "Sorry!")
        elif string.isdecimal():
            list = []
            listRev = []
            for item in string:
                list.append(item)
            for num in range(len(list)):
                listRev.append(list[-(num + 1)])
            if list == listRev:
                return True
            else:
                print("Sorry, that is not a correct palindrome. Try again!")


    def findNext(string):
        list = []
        listRev = []
        num = int(string)
        while True:
            num += 1
            if showNums:
                print(num)
            for item in str(num):
                list.append(item)
            for item in range(len(list)):
                listRev.append(list[-(item + 1)])
            if list == listRev:
                print(*list, sep="")
                print("The difference was " + str((num - int(string))))
                if num - int(string) > 10000:
                    print("That was a lot!")
                break
            else:
                list.clear()
                listRev.clear()

    userInput = input("Enter your palindrome: ")
    print("You entered: " + userInput)
    if check(userInput):
        print("Good job. Here is the next palindrome:")
        print(s)
        findNext(userInput)

    print(s)
    c = input("Would you like to do it again? (y/n): ")
    if c.lower() == "y":
        main()
    else:
        print("Okay, thanks for using my program! :)")
        time.sleep(1)
        print(s)
        print("Exiting in 3...")
        time.sleep(1)
        print("           2...")
        time.sleep(1)
        print("           1...")
        time.sleep(1)
        print("           Bye!")
        time.sleep(.25)
        quit()


showNums = input("Would you like to see all of the numbers? (y/n): ")
print("Just an FYI: Larger numbers take longer.")
showNums = showNums.lower()
if showNums == "y":
    showNums = True
else:
    showNums = False
main()
