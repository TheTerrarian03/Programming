number = 0

while True:
    user_input1 = input("Please enter a number to find the (aproximate) square of: ")
    try:
        float(user_input1)
        break
    except ValueError:
        print("is not a valid number. Try again. ")
        print()


