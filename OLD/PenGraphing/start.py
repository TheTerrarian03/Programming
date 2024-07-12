import Variables as v


def main():
    print("Welcome to my Pen Graphing Python Project! :D")
    print()
    while True:
        temp_var = input("Specify a min X value (default 1): ")
        try:
            int(temp_var)
            break
        except ValueError:
            print("Please enter an integer!")
    v.GraphXMIN = temp_var
    while True:
        temp_var = input("Specify a max X value: ")
        try:
            int(temp_var)
            break
        except ValueError:
            print("Please enter an integer!")
    v.GraphXMAX = temp_var
    while True:
        temp_var = input("Specify a min Y value (default 1): ")
        try:
            int(temp_var)
            break
        except ValueError:
            print("Please enter an integer!")
    v.GraphYMIN = temp_var
    while True:
        temp_var = input("Specify a max Y value: ")
        try:
            int(temp_var)
            break
        except ValueError:
            print("Please enter an integer!")
    v.GraphYMAX = temp_var

    print()


if __name__ == '__main__':
    print("ERROR")
