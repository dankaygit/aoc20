def readInput(fileName):

    instructions= []
    with open(fileName) as file:
        lines = file.readlines()    
    
    ## The input file contains coordinates (action+value pairs) 
    ## with a letter first then a number
    ## We separate the letter and number and 
    ## also strip the linebreak symbol. Finally we convert into an int
    ## Returns a list of lists with pairwise entries, action + value
    instructions = [[line[0], int(line[1:].rstrip())] for line in lines]
    return (instructions)


def updateDirection(coordinates, direction):
    if coordinates[0] == 'L':
        direction = (direction - coordinates[1]/90)%4
    else:
        direction = (direction + coordinates[1]/90)%4

    return (int(direction))

def rotateCoords(wCoords, coordinates):
    direction = coordinates[0]
    rotation = coordinates[1]

    if rotation == 180:
        return ([-wCoords[0], -wCoords[1]])

    if rotation == 270:
        if direction == 'L':
            direction = 'R'
        else:
            direction = 'L'
        rotation = 90

    if rotation == 90:
        if direction == 'R':
            newCoords = [wCoords[1], -wCoords[0]]
        else:
            newCoords = [-wCoords[1], wCoords[0]]

    return (newCoords)


def solvePartA(instructions, directions, gridDirections):
    currentCoords = [0,0]
    direction = directions['E']

    ## Define what to do for different actions
    for coordinates in instructions:
        action = coordinates[0]
        if action in ['L', 'R']:
            direction = updateDirection(coordinates, direction)
            continue
        elif action in ['N', 'E', 'S', 'W']:
            gridCoords = gridDirections[directions[action]]
        else:
            gridCoords = gridDirections[direction]
        
        currentCoords[0] += gridCoords[0]*coordinates[1]
        currentCoords[1] += gridCoords[1]*coordinates[1]

    return (abs(currentCoords[0]) + abs(currentCoords[1]))

def solvePartB(instructions, directions, gridDirections):
    wCoords = [10, 1]
    boatCoords = [0, 0]

    for coordinates in instructions:
        action = coordinates[0]
        step = coordinates[1]
        if action in ['N', 'E', 'S', 'W']:
            gridCoords = gridDirections[directions[action]]
            wCoords[0] += step * gridCoords[0]
            wCoords[1] += step * gridCoords[1]
        elif action in ['L', 'R']:
            wCoords = rotateCoords(wCoords, [action, step])
        else:
            boatCoords[0] += step * wCoords[0]
            boatCoords[1] += step * wCoords[1]

    return (abs(boatCoords[0]) + abs(boatCoords[1]))

def main():
    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day12-input.csv"

    directions = {'N' : 0, 'E' : 1, 'S': 2, 'W': 3}
    gridDirections = {0 : [0,1], 1 : [1,0], 2: [0,-1], 3: [-1,0]}
    instructions = readInput(fileName)

    solA = solvePartA(instructions, directions, gridDirections)
    print ("Solution to part A is:", solA)
    
    solB = solvePartB(instructions, directions, gridDirections)
    print ("Solution to part B is:", solB)

    return (0)

if __name__ == "__main__":
    import sys
    import numpy as np
    import math
    
    main()