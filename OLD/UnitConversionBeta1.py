def main1():
    print("Choices: mm, cm, m, km, inches, feet, yards, and miles")
    print("NOTE: YOU CAN ONLY CONVERT MM TO CM RIGHT NOW")
    b = input("Choose a unit to convert FROM: ")
    c = int(input("Choose HOW MANY: "))
    d = input("Choose a unit to convert TO: ")
    if b == "mm" and d == "cm":
        answer = c / 10

    print("Your answer is:", answer, d)

def main():
    print("Welcome to my Unit Conversion Program!!!")
    print("-- Made By Logan  S. Meyers --")
    print("distance = 1, temperature = 2")
    print("NOTE: YOU CAN USE DISTANCE RIGHT NOW")
    a = int(input("Enter a number: "))

    if a == 1:
        main1()
    else:
        print("!USER ERROR!")
        main()

main()