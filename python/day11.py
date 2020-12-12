def readInput(fileName):

    seatMap = [] 
    with open(fileName) as file:
        seatMap = file.readlines()
    
    for i in range(len(seatMap)):
        seatMap[i] = list(seatMap[i].rstrip())

    return (seatMap)

def countOccupieds(seatMap):
    count = 0
    for row in range(len(seatMap)):
        for column in range(len(seatMap[0])):
            count+= seatMap[row][column] == '#'
    return (count)

def applySeatingRules(seatMap, seatCoords):
    seatState = seatMap[seatCoords[0]][seatCoords[1]]
    

    ## If the seat is actually floor, do nothing.
    if seatState == '.':
        return (seatState)
    
    ## Create list of surrounding seat positions to check (don't forget to remove the actual seat)
    relPos = itertools.product([-1,0,1], [-1,0,1])
    checkSeats = []
    for pos in relPos:
        nextCoords = [seatCoords[0] + pos[0], seatCoords[1] + pos[1]]
        
        ## Make sure that the coordinates are actually in the map (borders)
        if nextCoords[0] in range(len(seatMap)) and nextCoords[1] in range(len(seatMap[0])):
            checkSeats.append(nextCoords)
    checkSeats.remove(seatCoords)

    ## Define the two rules
    if seatState == 'L':
        for seat in checkSeats:
            if seatMap[seat[0]][seat[1]] == '#':
                return ('L')
        return ('#')
    if seatState == '#':
        count = 0
        for seat in checkSeats:
            count += seatMap[seat[0]][seat[1]] == '#'
        if count >= 4: return ('L')
        else: return (seatState)

def seatRound(seatMap):
    newSeatMap = []
    for row in range(len(seatMap)):
        newSeatRow = []
        for column in range(len(seatMap[0])):
            newSeatRow.append(applySeatingRules(seatMap, [row, column]))
        newSeatMap.append(newSeatRow)
    
    return (newSeatMap)

def solvePartA(seatMap):
    start = time.time()
    previousMap = seatMap
    newMap = seatRound(seatMap)
    while (newMap != previousMap):
        previousMap = newMap
        newMap = seatRound(previousMap)
    
    numOccupied = countOccupieds(newMap)
    end = time.time()
    print ("In the end, {} seats are occupied.".format(numOccupied) )
    print ("Your code took friggin' {} seconds to complete!".format(round(end-start, 2)))
    

def main(seatMap):
    
    solvePartA(seatMap)
    # solvePartB(program)


if __name__ == "__main__":
    import itertools
    import time
    import sys
    import numpy as np

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day11-input.txt" 

    seatMap = readInput(fileName)

    main(seatMap)
