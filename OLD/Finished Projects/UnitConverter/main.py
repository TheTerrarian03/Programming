import menu
import option1
import option2
import option3
import option4
import option7


while True:
    option = menu.main()
    print("option = " + str(option))

    if option == 1:
        o = option1.main()
    elif option == 2:
        o = option2.main()
    elif option == 3:
        o = option3.main()
    elif option == 4:
        o = option4.main()
    elif option == 7:
        o = option7.main()
    elif option == "EXIT":
        break

    print(o)
    if o == "RETURN_TO_MENU":
        continue
    elif o == "EXIT":
        break


quit()
