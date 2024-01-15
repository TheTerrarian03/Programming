import time

def getInt(prompt="", greaterThanZero=True):
    while True:
        inp = input(prompt)
        try:
            inp = int(inp)
            if (greaterThanZero) and (inp < 0):
                print("Error: please enter an integer greater than 0!")
                continue
            return inp
        except ValueError:
            if greaterThanZero:
                print("Error: please enter an integer greater than 0!")
            else:
                print("Error: please enter an integer!")

def calcFib(index, debug):
    lastNum = 0
    currNum = 1

    for i in range(index):
        placeHolder = currNum
        currNum = lastNum + currNum
        lastNum = placeHolder
        if debug:
            print(f"Current number: {currNum}")
    
    return currNum

# beginning variables
indexTo = getInt("Enter how what index you want to calculate (the first num, 0, does not count):\n$ ")
printOut = False

start_time = time.time()
answer = calcFib(indexTo, printOut)
print(answer)
print(f"It took a total of {time.time() - start_time} seconds!")