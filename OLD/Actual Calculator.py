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

    e = (input("Do you want to convert again? (y/n): "))

    if e == "y":
        main8()
    if e == "n":
        print("Ok. Bye. :)")


main8()