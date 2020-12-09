def runProgram(program):
    jumper = 0
    lines = []
    acc = 0
    
    while jumper not in lines:
        lines.append(jumper)
        op = program.op[jumper]
        
        if op == 'acc':
            acc += program.val[jumper]
            jumper += 1
        elif op == 'jmp':
            jumper += program.val[jumper]
        else: jumper += 1
    
        if jumper == len(program): 
            print ("Program terminated")
            break
    
    return (acc, jumper)

def swapOp(program, line):
    swappedProgram = pd.Series.copy(program)
    if (program.op[line] == 'jmp'):
        swappedProgram['op'][line] = 'nop'
    elif program.op[line] == 'nop': 
        swappedProgram['op'][line] = 'jmp'
    else: raise("Op was acc")
    return (swappedProgram)

def solvePartA(program):
    acc, _ = runProgram(program)
    return (acc)

def solvePartB(program):
    startT = time.time()
    change_bool = (program.op == 'jmp') | (program.op == 'nop')
    change_idx = pd.Series(range(len(change_bool)))[change_bool]
    jumper = 0
    counter = 0
    acc, jumper = runProgram(program)

    for idx in change_idx:
        if jumper == len(program): 
            print ("Found the correct swap after {} swaps in {} secs.".format(counter, round(time.time() - startT, 3)))
            print ("Swap index was:", idx)
            print ("Accumulator =", acc)
            return (acc)
        
        nextProgram = swapOp(program, idx)
        acc, jumper = runProgram(nextProgram)
        counter += 1
    
    endT = time.time()
    print ("Program didn't terminate after ", endT)
    return (0)
    


def main(program):
    
    solA = solvePartA(program)
    print ("Part A: Accumulator =", solA)
    solvePartB(program)


if __name__ == "__main__":
    import time
    import sys
    import pandas as pd

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-kof/day8-input.csv" 

    program = pd.read_csv(fileName, sep = ' ', names = ["op", "val"])

    main(program)
