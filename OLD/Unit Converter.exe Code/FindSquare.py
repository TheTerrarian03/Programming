def find_square(num):
    try:
        number = float(num)
    except UnboundLocalError:
        print("Please try again, with a number this time.")
        print("Thank you!")
        find_square(input("Enter number to find square of: "))
    except ValueError:
        print("Please try again, with a number this time.")
        print("Thanks you")
        find_square(input("Enter number to find square of: "))

    x = 0
    number *= 10

    while True:
        square = x * x
        if square == number:
            number /= 10
            x /= 10
            print(str(x) + " * " + str(x) + " = " + str(number))
            print("True")
            print("----------------")
            print("")
            print("The square of " + str(number) + " = " + str(x))
            print("")
            print("----------------")
            break
        elif square < number:
            x + 0.1
            print(str(x) + " * " + str(x) + " != " + str(number))
            print("False")
            print("Adding...")
            x += 1
        elif square > number:
            print(str(x) + " * " + str(x) + " > " + str(number))
            print("False")
            x -= 1
            number /= 10
            x /= 10
            print("----------------")
            print("")
            print("The square of " + str(number) + " a little more than " + str(x))
            print("")
            print("----------------")
            break
        

find_square(input("Enter number to find square of: "))
