def readInput(fileName):

    with open(fileName) as file:
        lines = file.readlines()
    return (lines)

def findRow(line):
    code = line[:7]
    row = [0, 127] # total no. of rows separated in max min to iteratively reduce
    max_idx = len(code) - 1


    for i in range(max_idx + 1):
        if (code[i] == 'F'):
            row[1] -= 2**(max_idx - i)
        else:
            row[0] += 2**(max_idx - i)
        
    return row[0]

def findColumn(line):
    code = line[7:10]
    col = [0, 8]

    max_idx = len(code) - 1

    for i in range(max_idx + 1):
        if (code[i] == 'L'):
            col[1] -= 2**(max_idx - i)
        else:
            col[0] += 2**(max_idx - i)
        
    return col[0]

def getCoordinates(line):
    coords = [findRow(line), findColumn(line)]
    return (coords)

def seatID(line):
    coords = getCoordinates(line)
    ID = 8 * coords[0] + coords[1]
    return (ID)

def main():
    
    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-kof/day5-input.txt"
    
    lines = readInput(fileName)
    seatIDs = np.array([seatID(line) for line in lines])
    print ("Max seat ID: ", seatIDs.max()) ## Solution to part a
    
    ## For part b we need to find the missing IDs which aren't at the front or back
    
    seatIDs.sort() ## sorting the array we can subtract the next from previous number
    ## All that's left to check is where the missing number is (we will have a difference that's not 1)
    myIDIdx = np.where(seatIDs[1:] - seatIDs[:-1] != 1)[0][0]
    mySeatID = seatIDs[myIDIdx] + 1
    print ("My seat ID: ", mySeatID)




    return (0)

if __name__ == "__main__":
    import sys
    import numpy as np
    # fileName = "../data-kof/day5-input.txt"
    main()