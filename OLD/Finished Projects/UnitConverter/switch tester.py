def get_quarter_classes(quarter_num):
    switcher = {
        1: "Geometry, Computer Science Intro, and Spanish.",
        2: "English, Environmental Science, and Gym.",
        3: "Geometry, Computer Science Intro, and Spanish.",
        4: "English, Environmental Science, and Gym."
    }
    return switcher.get(quarter_num, "Invalid quarter")


print("Welcome to Logan's Class getter thingamabob.")
while True:
    ui1 = input("Please enter the quarter: ")
    try:
        ui2 = int(ui1)
        if 1 <= ui2 <= 4:
            print("Your classes are: " + get_quarter_classes(ui2))
            break
        else:
            print("Error, please try again.")
    except ValueError:
        print("Error, please try again.")
