import time
y = 0
x = 0


while True:
        if x == 60:
            x = 0
            y = y + 1

        elif y == 1 and x == 0:
            print("One minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y == 1 and x == 1:
            print("One minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y == 1 and x == 2:
            print("One minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y == 1 and x == 3:
            print("One minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y == 1 and x == 4:
            print("One minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y == 1 and x == 5:
            print("One minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y > 1 and x == 0:
            print("Another minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y > 1 and x == 1:
            print("Another minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y > 1 and x == 2:
            print("Another minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y > 1 and x == 3:
            print("Another minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y > 1 and x == 4:
            print("Another minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        elif y > 1 and x == 5:
            print("Another minute down! The time is:", y,"-",(x))
            x = x + 1
            time.sleep(1)
        else:
            print(y,"-",(x))
            x = x + 1
            time.sleep(1)
