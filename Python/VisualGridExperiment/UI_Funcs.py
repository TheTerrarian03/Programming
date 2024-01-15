def userPickAction():
    action = input("Enter action here: (examples: actions, graph points, enter equation, quit):\n>> ")
    result = processAction(action)
    if result == 0:
        print("Invalid action")
    elif result == 1:
        return 1

def printActions():
    print("Choices:\n1. actions - print actions\n2. graph points - re-plot points in graph\n3. enter eqa")

def processAction(actionPicked):
    actions = ["actions", "graph points", "enter equation", "quit"]

    if actionPicked in actions:
        # code
        pass
    else:
        return 0