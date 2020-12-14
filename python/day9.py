def findSum(input, index):
    summands = input[(index - 25) : index]
    diff = input [index] - summands

    solutions = []

    for d in diff:
        if d in summands:
            solutions.append(d)
    
    return (solutions)


def solvePartA(input):
    index = 25
    summands = findSum(input, index)

    while summands:
        index += 1
        summands = findSum(input, index)
    
    return ([index, input[index]])

def findContiguous(input, index):
    found = False
    
    targetNum = input[index]
    currentHigh = index
    currentLow = currentHigh - 2
    currentSum = input[currentLow:currentHigh].sum()

    while not found:
        while currentSum < targetNum:
            currentLow -= 1
            currentSum += input[currentLow]

            if currentSum == targetNum:
                minIdx = input[currentLow:currentHigh].argmin()
                maxIdx = input[currentLow:currentHigh].argmax()
                return ([currentLow + minIdx, currentLow + maxIdx])

        currentHigh -= 1
        currentLow = currentHigh - 2
        currentSum = input[currentLow:currentHigh].sum()

def solvePartB(input, indexA):
    highLowIndices = findContiguous(input, indexA)

    resultB = input[highLowIndices].sum()
        
    return (resultB)


def main(fileName):
    
    solA = solvePartA(input)
    print ("Solution A is: ", solA[1])

    solB = solvePartB(input, solA[0])
    print ("Solution B is: ", solB)

if __name__ == "__main__":
    import sys
    import numpy as np

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day9-input.csv" 

    input = np.genfromtxt(fileName, dtype = int)

    main(input)
