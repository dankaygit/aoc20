def validatePasses(fileName):
    
    import numpy as np

    # Read in the lines into a list

    with open(fileName) as file:
        lines = file.readlines()

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
            if (idx > len(lines) - 1): break
            nextString = lines[idx]
        
        idx += 1
        passes.append(passport.replace('\n', ' ').strip(' '))
    
    # TODO: 2. Check whether it's a valid passport or NPID (i.e. check whether 8 entries exist and if it's 7, check that only cid is missing)

    validPasses = []

    for passp in passes:
        if (passp.count(' ') == 7):
            validPasses.append(
                dict(x.split(":") for x in passp.split(" "))
                )
        elif (passp.count(' ') == 6 and not 'cid' in passp):
            validPasses.append(
                dict(x.split(":") for x in passp.split(" "))
                )

    print ("Number of valid passes for part 1: ", len(validPasses))

    return (validPasses)


def validateEntries(ppt):
    import re
    byr = int(ppt['byr']) >= 1920 and int(ppt['byr']) <= 2002
    iyr = int(ppt['iyr']) >= 2010 and int(ppt['iyr']) <= 2020
    eyr = int(ppt['eyr']) >= 2020 and int(ppt['eyr']) <= 2030
    hgt = ('cm' in ppt['hgt'] and (int(ppt['hgt'][:-2]) >= 150 and int(ppt['hgt'][:-2]) <= 193 ) ) or ('in' in ppt['hgt'] and (int(ppt['hgt'][:-2]) >= 59 and int(ppt['hgt'][:-2]) <= 76 ) )
    hcl = ppt['hcl'].startswith('#') and re.match("[a-f0-9]+", ppt['hcl'][1:]).end() == 6
    ecl = ppt['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = len( ppt['pid'] ) == 9
    
    return (byr and iyr and eyr and hgt and hcl and ecl and pid)


def main():
    import numpy as np
    import re
    fileName = input("Enter inputFileName (Watch out for relative path): ")
    validPasses = validatePasses(fileName)

    validatedDicts = np.array([validateEntries(ppt) for ppt in validPasses])

    print("Number of valid passports for part b: ", validatedDicts.sum())

    return (0)


if __name__ == "__main__":
    main()
    