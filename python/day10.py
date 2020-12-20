def prepDifferences(fileName):
    jolts = np.genfromtxt(fileName)
    jolts.sort()
    jolts = np.insert(jolts, 0, 0)
    jolts = np.append(jolts, jolts[-1] + 3)
    differences = jolts[1:] - jolts[:-1]

    return (differences)

def solvePartA(differences):
    numOfOnes = (differences == 1).sum()
    numOfThrees = (differences == 3).sum()

    return (numOfOnes * numOfThrees)

def findFixedPoints(differences):
    fixedPoints = np.empty(len(differences) + 1, dtype=np.bool)
    fixedPoints[0] = True
    fixedPoints[len(fixedPoints) - 1] = True
    for i in range(0,len(differences)- 1):
        if differences[i] == 1 and differences[i+1] != 3:
            fixedPoints[i+1] = False
        else:
            fixedPoints[i+1] = True
    return (fixedPoints)

def countPockets(fixedPoints):
    pockets = dict.fromkeys([0,1,2,3,4,5])
    pockets = dict.fromkeys(pockets, 0)
    counter = 0
    for point in fixedPoints:
        if point == True:
            pockets[counter] += 1
            counter = 0
        else:
            counter += 1
    return (pockets)

def solvePartB(differences):
    fixedPoints = findFixedPoints(differences)
    pockets = countPockets(fixedPoints)
    solB = 1
    for size in pockets:
        combinations = 0
        if size < 3:
            minimum = 0
        else:
            minimum = 1
        for k in range(minimum, size + 1):
            combinations += comb(size, k)
        solB *= int(combinations**pockets[size])
    
    return (solB)


def main(fileName):
    differences = prepDifferences(fileName)
    

    solA = solvePartA(differences)
    print ("Solution A is: ", solA)

    solB = solvePartB(differences)
    print ("Solution B is: ", solB)

if __name__ == "__main__":
    import sys
    import numpy as np
    from scipy.special import comb
    

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day10-input.csv" 


    main(fileName)
