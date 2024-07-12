# This is the most  useless calendar!


def main():
    date = input("What is the date of the calendar's to-do list?"
                 "The Format is: MMDDYYYY\n")
    if date == "04152020":
        todo_04152020()


def todo_04152020():
    one = "1. Work on Spanish stuff until MATH MEETING AT 10:30AM"
    two = "2. MATH MEETING AT 10:30AM"
    three = "3. Continue Spanish stuff, hopefully finish"
    four = "4. Fill our P.E. Journal for 2 days"
    five = "5. Work on Science notes and lab (due Friday)"
    six = "6. Make extra ELA video"
    seven = "7. Choir warm-up assignment"
    specific_item = input("Is there a specific item to show?\n")
    if specific_item == "n" or specific_item == "no":
        print(one, two, three, four, five, six, seven)
    elif specific_item == "1":
        print(one)
    elif specific_item == "2":
        print(two)
    elif specific_item == "3":
        print(three)
    elif specific_item == "4":
        print(four)
    elif specific_item == "5":
        print(five)
    elif specific_item == "6":
        print(six)
    else:
        print(seven)


main()
