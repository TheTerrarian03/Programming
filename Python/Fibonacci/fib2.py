import time, math

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
    a = ((1+math.sqrt(5))/2) ** index
    b = ((1-math.sqrt(5))/2) ** index
    c = a - b
    d = (1/(math.sqrt(5)))
    e = c * d

    return round((1/(math.sqrt(5))) * ((((1+math.sqrt(5))/2) ** index) - (((1-math.sqrt(5))/2) ** index)))

# beginning variables
indexTo = getInt("Enter how what index you want to calculate (the first num, 0, does not count):\n$ ")
printOut = False

start_time = time.time()
answer = calcFib(indexTo, printOut)
print(answer)
print(f"It took a total of {time.time() - start_time} seconds!")
