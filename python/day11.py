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

def applySeatingRulesA(seatMap, seatCoords):
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

## For part B I need a function which returns the value of the next
## visible neighbour in every direction
## This function returns all the next visible neighbours in a list

def findVisibleNeighbours(seatMap, seatCoords):
    ## Create list of surrounding seat positions to check (don't forget to remove the actual seat)
    relPos = itertools.product([-1,0,1], [-1,0,1])
    checkSeats = []

    ## For every relative position (which isn't [0,0]) we need to find the nearest actual neighbour
    for pos in relPos:
        nextCoords = [seatCoords[0] + pos[0], seatCoords[1] + pos[1]]
        if pos[0] == 0 and pos[1] == 0:
            continue
        ## Make sure that the coordinates are actually in the map (borders)
        if nextCoords[0] not in range(len(seatMap)) or nextCoords[1] not in range(len(seatMap[0])):
            continue
        else: 
            while (seatMap[nextCoords[0]][nextCoords[1]] == '.'):
                nextCoords[0] += pos[0]
                nextCoords[1] += pos[1]
                if nextCoords[0] not in range(len(seatMap)) or nextCoords[1] not in range(len(seatMap[0])):
                    nextCoords[0] -= pos[0]
                    nextCoords[1] -= pos[1]
                    break
            checkSeats.append(nextCoords)

    return (checkSeats)

def applySeatingRulesB(seatMap, seatCoords):
    seatState = seatMap[seatCoords[0]][seatCoords[1]]
    
    ## If the seat is actually floor, do nothing, especially don't call findVisibleNeighbour
    if seatState == '.':
        return (seatState)
    
    ## Get the visible neighbours
    ## NOTE: This calls the same function findVisibleNeighbours with the same result in every iteration. 
    # We shouldn't have that!! Rather we should save the result of the function after
    # the first iteration of calling applySeatingRulesB and then retrieve the list for thes coords
    checkSeats = findVisibleNeighbours(seatMap, seatCoords)

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
        if count >= 5: return ('L')
        else: return (seatState)

def seatRound(seatMap, part = 'A'):
    ## Which seatRound are we doing (this is to reduce duplicate code)
    applySeatingRules = applySeatingRulesA
    if part == 'B': 
        applySeatingRules = applySeatingRulesB
    
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
    newMap = seatRound(seatMap, 'A')
    while (newMap != previousMap):
        previousMap = newMap
        newMap = seatRound(previousMap, 'A')
    
    numOccupied = countOccupieds(newMap)
    end = time.time()
    print ("In the end, {} seats are occupied.".format(numOccupied) )
    print ("Your code took friggin' {} seconds to complete part A!".format(round(end-start, 2)))

def solvePartB(seatMap):
    start = time.time()
    previousMap = seatMap
    newMap = seatRound(seatMap, 'B')
    while (newMap != previousMap):
        previousMap = newMap
        newMap = seatRound(previousMap, 'B')
    
    numOccupied = countOccupieds(newMap)
    end = time.time()
    print ("In the end, {} seats are occupied.".format(numOccupied) )
    print ("Your code took friggin' {} seconds to complete part B!".format(round(end-start, 2)))
    

def main(seatMap):
    
    solvePartA(seatMap)
    solvePartB(seatMap)


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
