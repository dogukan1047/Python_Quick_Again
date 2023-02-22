def dailyTemperatures(temperatures):
    myList = [0] * len(temperatures)
    myStack = []

    for ix, temperature in enumerate(temperatures):
        while myStack and temperature > myStack[-1][0]:
            stackTemp, stackIndex = myStack.pop()
            myList[stackIndex] = ix - stackIndex
        myStack.append([temperature, ix])

    return myList



listem=[73,74,75,71,69,72,76,73]
dailyTemperatures(listem)