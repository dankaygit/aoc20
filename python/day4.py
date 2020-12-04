def main(fileName):
    
    import numpy as np
    
    # Read in the lines into a list
    
    with open(fileName) as file:
        lines = file.readlines()
    
    lines = np.array(lines)
    
    # Next we need to recognise which lines actually belong together into one line as the entries of one document
    # TODO: 1. Find each "\n" entry and then take all elements before it, put them together into a single string in a new condensed list

    passes = []
    idx = 0
    while (idx < len(lines) - 1):
        nextString = lines[idx]
        passport = ""

        while (nextString != '\n'):
            passport += nextString
            
            idx += 1
            if (idx >= len(lines) - 1): break
            nextString = lines[idx]
        
        idx += 1
        passes.append(passport.replace('\n', ' ').strip(' '))

    valid = 0

    for passp in passes:
        if (passp.count(' ') == 7):
            valid += 1
        elif (passp.count(' ') == 6 and not 'cid' in passp):
            valid += 1

    print ("Number of valid passes for part 1: ", valid)

    return (0)



        



    # TODO: 2. Check whether it's a valid passport or NPID (i.e. check whether 8 entries exist and if it's 7, check that only cid is missing)




if __name__ == "__main__":
    fileName = input("Enter inputFileName (Watch out for relative path): ")
    main(fileName)