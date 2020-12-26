def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def readFile(fileName):
    instructions = []
    with open(fileName) as file:
        for line in file:
            line = line.split('=')
            for i in range(len(line)):
                line[i] = line[i].strip()
            instructions.append(line)
    return (instructions)

def convertTo36Binary(decimal):
    intLen = 36
    binary = ''
    highestBit = math.ceil(math.log2(decimal))
    for i in range(highestBit, 0, -1):
        if decimal % 2**i < decimal:
            binary += '1'
            decimal -= 2**i
        else:
            binary += '0'
    
    if decimal == 1:
        binary += '1'
    else:
        binary += '0'


    ## Sanity check here!    
    if len(binary) != highestBit + 1:
        print ('wrong number of bits at the end')
        
    missingBits = intLen - len(binary)
    binary =  '0' * missingBits + binary
    
    return (binary)
    
def applyMaskToValue(value, mask):
    binValue = convertTo36Binary(value)
    newValue = ''

    for i in range(len(mask)):
        if mask[i] != 'X':
            newValue += mask[i]
        else:
            newValue += binValue[i]

    # Converts binary (even in a string) to decimal
    newValue = int(newValue, 2)
    return (newValue)

def applyMaskToAddress(address, mask):
    binValue = convertTo36Binary(address)
    addresses = ['']

    for i in range(len(mask)):
        if mask[i] == 'X':
            toAppend = []
            for j in range(len(addresses)):
                toAppend.append(addresses[j] + '1')
                addresses[j] += '0'
            addresses += toAppend
        elif mask[i] == '1':
            for j in range(len(addresses)):
                addresses[j] += '1'
        else:
            for j in range(len(addresses)):
                addresses[j] += binValue[i]

    # Convert binary back to decimal 
    for i in range(len(addresses)):
        addresses[i] = int(addresses[i], 2)
    return (addresses)

def progressBarB(counter, length):
    empty = ' '*(length-counter) + 'X'
    progress = '-' * counter + empty
    print (progress)

def solvePartA(instructions):
    mask = instructions[0][1]
    lookUp = [[],[]]
    
    for line in instructions:
        index = 0
        address = 0
        value = 0

        if line[0] == 'mask':
            mask = line[1]
        
        else:
            address = int(re.sub('[^0-9]', '', line[0]))
            value = int(line[1])
            writeValue = applyMaskToValue(value, mask)

            ## Check whether address is in the lookup table.
            ## If it is then we don't need to add it to the table
            ## Instead, we just set the index to the index of the address
            ## Otherwise append the lookup table and set index to last index.
            if address not in lookUp[0]:
                lookUp[0].append(address)
                index = len(lookUp[0]) - 1
                lookUp[1].append(writeValue)

            else:
                index = lookUp[0].index(address)
                lookUp[1][index] = writeValue

    total = 0
    for value in lookUp[1]:
        total += value

    return (total) 


def solvePartB(instructions):
    mask = instructions[0][1]
    lookUp = [[],[]]
    i = 1
    length = len(instructions)

    for line in instructions:
        # print ('Line{}: '.format(i), line)
        # progressBarB(i, length)
        printProgressBar(i, length)
        i += 1
        index = 0
        address = 0
        value = 0

        if line[0] == 'mask':
            mask = line[1]
        
        else:
            address = int(re.sub('[^0-9]', '', line[0]))
            value = int(line[1])
            # writeValue = applyMaskToValue(value, mask)
            addresses = applyMaskToAddress(address, mask)

            ## Check whether address is in the lookup table.
            ## If it is then we don't need to add it to the table
            ## Instead, we just set the index to the index of the address
            ## Otherwise append the lookup table and set index to last index.
            for address in addresses:
                if address not in lookUp[0]:
                    lookUp[0].append(address)
                    index = len(lookUp[0]) - 1
                    lookUp[1].append(value)
                else:
                    index = lookUp[0].index(address)
                    lookUp[1][index] = value

    total = 0
    for value in lookUp[1]:
        total += value

    return (total) 


def main(fileName):
    instructions = readFile(fileName)
    

    solA = solvePartA(instructions)
    print ("Solution A is: ", solA)

    solB = solvePartB(instructions)
    print ("Solution B is: ", solB)

if __name__ == "__main__":
    import sys
    import numpy as np
    import re
    import math

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day14-input.txt" 


    main(fileName)
