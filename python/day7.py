fileName = "../data-ec/day7-input.txt" 

def extractRules(fileName):
    rules = []
    with open (fileName) as file:
        rules = file.read().split('.\n')
    
    return (rules)

def findDirectParents(rules, bag = "shiny gold bag"):
    parents = []
    for rule in rules:
        if bag in rule:
            parent = rule.split(" ")[:3]
            parents.append(parent[0] + " " + parent[1] + " " + parent[2].rstrip('s'))
    
    if bag in parents:
        parents.remove(bag)

    return parents

def solvePartA(rules):
    goldBag = "shiny gold bag"
    ## Find the direct parents of the shiny gold bag
    directParents = findDirectParents(rules, goldBag)
    parents = directParents

    # Now for every direct parent in List parents, 
    # we iteratively find the direct parents and append
    # them to the parents list such that eventually there
    # are no more direct parents to find

    # Loop over list parents
    for parent in parents:
        # search for parents of current parrent
        parentParents = findDirectParents(rules, parent)
        # if you find any, append them to the parents list
        if parentParents:
            for parentParent in parentParents:
                parents.append(parentParent)

    # We might have duplicates so take the unique set of 
    # parents, which now includes all parents of shiny gold.
    parents = set(parents)
        
    print ("Number of parent bags: ", len(parents))

def solvePartB(rules):
    
    numIndices = [i for i, c in enumerate(rules[0]) if c.isdigit()]

    findKids(rules, bag)

def main(fileName):
    rules = extractRules(fileName)
    solvePartA(rules)
    solvePartB(rules)

if __name__ == "__main__":
    import sys

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day7-input.txt" 

    main(fileName)
