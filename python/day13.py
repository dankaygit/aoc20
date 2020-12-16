def readFile(fileName):
    busses = []
    earliestTime = 0
    with open(fileName) as file:
        earliestTime = int(file.readline().rstrip())
        busses = file.readline().split(',')
    
    return ([earliestTime, busses])

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return int(a * b / gcd(a, b))

def extractTimeTable(busList):
    runningBusses = []
    for bus in busList:
        if bus.isdigit():
            runningBusses.append(int(bus))

    return (runningBusses)

def extractTimeTableDelays(busList):
    runningBusses = []
    for bus in busList:
        if bus.isdigit():
            runningBusses.append([int(bus), busList.index(bus)])
    return (runningBusses)

def solvePartA(data):
    earliestTime = data[0]
    runningBusses = np.array(extractTimeTable(data[1]))
    minID = runningBusses.min()

    busIDX = 0
    waitTime = 0
    for time in range(earliestTime, earliestTime + minID):
        currentTimeTable = time % runningBusses
        if 0 in currentTimeTable:
            busIDX = np.where(currentTimeTable==0)[0][0]
            print (busIDX)
            waitTime = time - earliestTime
            break
            
    busID = runningBusses[busIDX]
    solA = busID*waitTime
    return (solA)

def solvePartB(data):
    busDelays = np.array(extractTimeTableDelays(data[1]))

    timestamp = max(busDelays[:,0]) - busDelays[busDelays[:,0].argmax(),1]
    sortedDelays = busDelays[(-busDelays[:,0]).argsort()]
    minstep = 1

    for i in range(1, len(busDelays)):
        previousBus = sortedDelays[i-1]
        currentBus = sortedDelays[i]
        minstep = lcm(minstep, previousBus[0])
        # print ("current minstep is: ", minstep)

        while ((timestamp + currentBus[1]) % currentBus[0]) != 0:
            timestamp += minstep
        
        i += 1

    return (timestamp)

    ## Aye aye aye...
    ## Brute forcing it below clearly did not work and boy did it not work
    ## How I ever could think that this below would work is a mistery 

    # while (notFound):
    #     sum = ((timestamp + busDelays[:,1]) % busDelays[:,0]).sum()
    #     if sum == 0:
    #         notFound = False
    #         break 
    #     else: 
    #         if not (timestamp % minstep*1000000): 
    #             print (timestamp)
    #         timestamp += minstep

    # return (timestamp)

def main(fileName):
    data = readFile(fileName)
    
    solA = solvePartA(data)
    print ("Solution A is: ", solA)

    solB = solvePartB(data)
    print ("Solution B is: ", solB)

if __name__ == "__main__":
    import sys
    import numpy as np
    

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day13-input.csv" 


    main(fileName)
