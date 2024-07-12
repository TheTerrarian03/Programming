# UnitConversionBeta2:

import time
import sys


def main():
    print("Welcome to my Unit Conversion Program!!!")

    time.sleep(1)

    print("-- Made By Logan  S. Meyers --")

    time.sleep(1)

    print("If something breaks, it's your fault.")

    time.sleep(1)

    print("Lol JK, but you probably did something wrong XD")

    time.sleep(1)

    print("")

    print("Distance Converter = 1, Temperature Converter = 2, Number Sorter = 3")
    print("Mean + Total Finder = 4, Range Finder = 5, 2 Number Calculator = 6")

    print("")

    a = int(input("Enter a number: "))
    if a == 1:
        main1()
    if a == 2:
        main2()
    if a == 3:
        main3()
    if a == 4:
        main6()
    if a == 5:
        main7()
    if a == 6:
        main8()
    else:
        print("USER ERROR!")
        print("Let's Try Again:")
        main20()


def main1():
    print("")
    print("Choices: mm, cm, m, km, inches, feet, yards, and miles")
    print("These letters have to not be capitalized.")
    print("")
    b = input("Choose a unit of distance to convert FROM: ")
    c = float(input("Choose HOW MANY: "))
    d = input("Choose a unit of distance to convert TO: ")
    if b == 'mm' and d == 'mm':
        answer = c
    if b == 'mm' and d == 'cm':
        answer = c / 10
    if b == 'mm' and d == 'm':
        answer = c / 1000
    if b == 'mm' and d == 'km':
        answer = c / 1000000
    if b == 'mm' and d == 'inches':
        answer = c / 25.4
    if b == 'mm' and d == 'feet':
        answer = c / 304.8
    if b == 'mm' and d == 'yards':
        answer = c / 914.4
    if b == 'mm' and d == 'miles':
        answer = c / 1609344
    if b == 'cm' and d == 'mm':
        answer = c * 10
    if b == 'cm' and d == 'cm':
        answer = c
    if b == 'cm' and d == 'm':
        answer = c / 100
    if b == 'cm' and d == 'km':
        answer = c / 100000
    if b == 'cm' and d == 'inches':
        answer = c / 2.54
    if b == 'cm' and d == 'feet':
        answer = c / 30.48
    if b == 'cm' and d == 'yards':
        answer = c / 91.44
    if b == 'cm' and d == 'miles':
        answer = c / 160934.4
    if b == 'm' and d == 'mm':
        answer = c * 1000
    if b == 'm' and d == 'cm':
        answer = c * 100
    if b == 'm' and d == 'm':
        answer = c
    if b == 'm' and d == 'km':
        answer = c / 1000
    if b == 'm' and d == 'inches':
        answer = c * 39.3701
    if b == 'm' and d == 'feet':
        answer = c * 3.28084
    if b == 'm' and d == 'yards':
        answer = c * 1.094
    if b == 'm' and d == 'miles':
        answer = c / 1609
    if b == 'km' and d == 'mm':
        answer = c * 1000000
    if b == 'km' and d == 'cm':
        answer = c * 100000
    if b == 'km' and d == 'm':
        answer = c * 1000
    if b == 'km' and d == 'km':
        answer = c
    if b == 'km' and d == 'inches':
        answer = c * 39370.1
    if b == 'km' and d == 'feet':
        answer = c * 3281
    if b == 'km' and d == 'yards':
        answer = c * 1094
    if b == 'km' and d == 'miles':
        answer = c / 1.609
    if b == 'inches' and d == 'mm':
        answer = c * 25.4
    if b == 'inches' and d == 'cm':
        answer = c * 2.54
    if b == 'inches' and d == 'm':
        answer = c / 39.37
    if b == 'inches' and d == 'km':
        answer = c / 39370
    if b == 'inches' and d == 'inches':
        answer = c
    if b == 'inches' and d == 'feet':
        answer = c / 12
    if b == 'inches' and d == 'yards':
        answer = c / 36
    if b == 'inches' and d == 'miles':
        answer = c / 63360
    if b == 'feet' and d == 'mm':
        answer = c * 304.8
    if b == 'feet' and d == 'cm':
        answer = c * 30.48
    if b == 'feet' and d == 'm':
        answer = c / 3.281
    if b == 'feet' and d == 'km':
        answer = c / 3281
    if b == 'feet' and d == 'inches':
        answer = c * 12
    if b == 'feet' and d == 'feet':
        answer = c
    if b == 'feet' and d == 'yards':
        answer = c / 3
    if b == 'feet' and d == 'miles':
        answer = c / 5280
    if b == 'yards' and d == 'mm':
        answer = c * 914.4
    if b == 'yards' and d == 'cm':
        answer = c * 91.44
    if b == 'yards' and d == 'm':
        answer = c / 1.094
    if b == 'yards' and d == 'km':
        answer = c / 1094
    if b == 'yards' and d == 'inches':
        answer = c * 36
    if b == 'yards' and d == 'feet':
        answer = c * 3
    if b == 'yards' and d == 'yards':
        answer = c
    if b == 'yards' and d == 'miles':
        answer = c / 1760
    if b == 'miles' and d == 'mm':
        answer = c * 1609344
    if b == 'miles' and d == 'cm':
        answer = c * 160934.4
    if b == 'miles' and d == 'm':
        answer = c / 1609.344
    if b == 'miles' and d == 'km':
        answer = c / 1.609344
    if b == 'miles' and d == 'inches':
        answer = c * 63360
    if b == 'miles' and d == 'feet':
        answer = c * 5280
    if b == 'miles' and d == 'yards':
        answer = c * 1760
    if b == 'miles' and d == 'miles':
        answer = c

    print("Your answer is:", answer, d)

    time.sleep(1)

    e = (input("Do you want to convert again? (y/n): "))

    if e == "y":
        main20()
    if e == "n":
        print("Ok. Bye. :)")
        time.sleep(5)
        print("...")
        time.sleep(1)
        print("You can close the window now...")
        time.sleep(10)
        print("I Love You UwU!")
        time.sleep(24)
        print("Well hey baby, since you're staying now, what're you doing later? ;)")


def main2():
    print("Choices: c, f, or k. These letters can't be capitalized.")
    print("")
    f = input("Choose a unit to convert FROM: ")
    g = float(input("Choose HOW MUCH: "))
    h = input("Choose a unit to convert TO: ")
    if f == "c" and h == "c":
        answer = g
    if f == "c" and h == "f":
        answer = (g * 9/5) + 32
    if f == "c" and h == "k":
        answer = g + 273.15
    if f == "f" and h == "c":
        answer = (g - 32) * 5/9
    if f == "f" and h == "f":
        answer = g
    if f == "f" and h == "k":
        answer = ((g - 32) * 5/9) + 273.15
    if f == "k" and h == "c":
        answer = g - 273.15
    if f == "k" and h == "f":
        answer = ((g - 273.15) * 9/5) + 32
    if f == "k" and h == "k":
        answer = g

    print("Your answer is:", answer, h)

    time.sleep(1)

    e = (input("Do you want to convert again? (y/n): "))

    if e == "y":
        main20()
    if e == "n":
        print("Ok. Bye. :)")
        time.sleep(5)
        print("...")
        time.sleep(1)
        print("You can close the window now...")
        time.sleep(10)
        print("I Love You UwU!")
        time.sleep(24)
        print("Well hey baby, since you're staying now, what're you doing later? ;)")


def main3():
    print("")
    i = input("sort from least to greatest (1) or greatest to least (2)? ")
    if i == "1":
        main4()
    if i == "2":
        main5()
    else:
        print("USER ERROR!")
        print("Let's Try AGAIN:")
        main3()


def main4():
    list = []
    j = int(input("How many numbers will there be? "))
    for k in range(1, (j + 1)):
        print("")
        print("Enter number at location", k, ":")
        item = float(input())
        list.append(item)
    print("Your list is: ", list)
    print("Is this correct? (y/n)")
    l = input()
    if l == "n":
        print("Ok, let's try again.")
        main4()
    if l == "y":
        list.sort()
        print("")
        print("Your final list is: ", list)

        time.sleep(1)

        print("")
        e = (input("Do you want to convert again? (y/n): "))

        if e == "y":
            main20()
        if e == "n":
            print("Ok. Bye. :)")
            time.sleep(5)
            print("...")
            time.sleep(1)
            print("You can close the window now...")
            time.sleep(10)
            print("I Love You UwU!")
            time.sleep(24)
            print("Well hey baby, since you're staying now, what're you doing later? ;)")


def main5():
    list = []
    j = int(input("How many numbers will there be? "))
    for k in range(1, (j + 1)):
        print("")
        print("Enter number at location", k, ":")
        item = float(input())
        list.append(item)
    print("Your list is: ", list)
    print("Is this correct? (y/n)")
    l = input()
    if l == "n":
        print("Ok, let's try again.")
        main3()
    if l == "y":
        list.sort(reverse=True)
        print("Your final list is: ", list)

        time.sleep(1)

        print("")
        e = (input("Do you want to convert again? (y/n): "))

        if e == "y":
            main20()
        if e == "n":
            print("Ok. Bye. :)")
            time.sleep(5)
            print("...")
            time.sleep(1)
            print("You can close the window now...")
            time.sleep(10)
            print("I Love You UwU!")
            time.sleep(24)
            print("Well hey baby, since you're staying now, what're you doing later? ;)")


def main6():
    list = []
    j = int(input("How many numbers will there be? "))
    for k in range(1, (j + 1)):
        print("")
        print("Enter number at location", k, ":")
        item = int(input())
        list.append(item)
    print("Your list is: ", list)
    print("Is this correct? (y/n)")
    l = input()
    if l == "n":
        print("Ok, let's try again.")
        main4()
    if l == "y":
        list.sort()
        total = sum(list)
        print("the total of your is:", total)
        total /= (len(list))
        print("The mean/average of your data is:", total)

        time.sleep(1)

        print("")
        e = (input("Do you want to convert again? (y/n): "))

        if e == "y":
            main20()
        if e == "n":
            print("Ok. Bye. :)")
            time.sleep(5)
            print("...")
            time.sleep(1)
            print("You can close the window now...")
            time.sleep(10)
            print("I Love You UwU!")
            time.sleep(10)
            print("You're still here?")
            time.sleep(14)
            print("Well hey baby, since you're staying now, what're you doing later? ;)")


def main7():
    list = []
    j = int(input("How many numbers will there be?"))
    for k in range(1, (j + 1)):
        print("")
        print("Enter number at location", k, ":")
        item = int(input())
        list.append(item)
    print("Your list is: ", list)
    print("Is this correct? (y/n)")
    l = input()
    if l == "n":
        print("Ok, let's try again.")
        main4()
    if l == "y":
        list.sort()
        firstNum = list[0]
        print("")
        print("The smallest number is: ", firstNum)
        lastNum = list[-1]
        print("")
        print("The largest number is: ", lastNum)
        listRange = lastNum - firstNum
        print("")
        print("The range of your data is: ", listRange)

        time.sleep(1)

        print("")
        e = (input("Do you want to convert again? (y/n): "))

        if e == "y":
            main20()
        if e == "n":
            print("Ok. Bye. :)")
            time.sleep(5)
            print("...")
            time.sleep(1)
            print("You can close the window now...")
            time.sleep(10)
            print("I Love You UwU!")
            time.sleep(10)
            print("You're still here?")
            time.sleep(14)
            print("Well hey baby, since you're staying now, what're you doing later? ;)")


def main8():
    answer = 0
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter second number: "))

    if operation == "+":
        answer = float(num1) + float(num2)
    if operation == "-":
        answer = float(num1) - float(num2)
    if operation == "/":
        answer = float(num1) / float(num2)
    if operation == "*":
        answer = float(num1) * float(num2)
    print(answer)

    time.sleep(1)

    print("")
    e = (input("Do you want to convert again? (y/n): "))

    if e == "y":
        main20()
    if e == "n":
        print("Ok. Bye. :)")
        time.sleep(5)
        print("...")
        time.sleep(1)
        print("You can close the window now...")
        time.sleep(10)
        print("I Love You UwU!")
        time.sleep(10)
        print("You're still here?")
        time.sleep(14)
        print("Well hey baby, since you're staying now, what're you doing later? ;)")
        time.sleep(5)
        sys.exit()


def main20():
    print("")
    print("Distance Converter = 1, Temperature Converter = 2, Number Sorter = 3")
    print("Mean + Total Finder = 4, Range Finder = 5, 2 Number Calculator = 6")

    a = int(input("Enter a number: "))
    if a == 1:
        main1()
    if a == 2:
        main2()
    if a == 3:
        main3()
    if a == 4:
        main6()
    if a == 5:
        main7()
    if a == 6:
        main8()
    else:
        print("")
        print("USER ERROR!")
        print("Let's Try Again:")
        main20()


main()

'''
https://www.google.com/search?q=unit+converter&oq=unit+converter&aqs=chrome..69i57j0l6j69i60.1815j0j7&sourceid=chrome&ie=UTF-8- Unit Converter from Google.
'''