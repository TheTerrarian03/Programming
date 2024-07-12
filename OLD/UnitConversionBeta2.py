# UnitConversionBeta2:

import time


def main():
    print("Welcome to my Unit Conversion Program!!!")

    time.sleep(1)

    print("-- Made By Logan  S. Meyers --")

    time.sleep(1)

    print("If something breaks, it's your fault.")

    time.sleep(1)

    print("distance = 1, temperature = 2")

    time.sleep(1)

    print("NOTE: YOU CAN ONLY USE DISTANCE RIGHT NOW")

    a = int(input("Enter a number: "))
    if a == 1:
        main1()
    else:
        print("USER ERROR!")
        print("Let's Try AGAIN:")
        main()


def main1():
    print("Choices: mm, cm, m, km, inches, feet, yards, and miles")
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
    if b == 'km' and d =='mm':
        answer = c * 1000000
    if b == 'km' and d =='cm':
        answer = c * 100000
    if b == 'km' and d =='m':
        answer = c * 1000
    if b == 'km' and d =='km':
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

    time.sleep(2)

    e = (input("Do you want to convert again? (y/n): "))

    if (e == "y"):
        main()
    if (e == "n"):
        print("Ok. Bye. :)")
        time.sleep(5)


def main3():
    print("USER ERROR! TRY AGIAN! Were your measurements all lowercase, or spelled correctly?")
    main1()


def main4():
    print("USER ERROR! TRY AGIAN! Were your measurements all lowercase?")
    main2()

main()

# https://www.google.com/search?q=unit+converter&oq=unit+converter&aqs=chrome..69i57j0l6j69i60.1815j0j7&sourceid=chrome&ie=UTF-8- Unit Converter from Google.