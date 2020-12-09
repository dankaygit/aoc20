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

def prettifyRules(rules):
    
    
    newRules = []
    ## First we split up the string into a list of each parent and child
    for r in rules:
        newRules.append(r.split('bag')[:-1])
    
    ## Now we do string operations to trim the strings, such that 
    # each child string in the new sublist starts with the number 
    # of times it appears in the parent bag (for easy extraction)
    # For bags without kids, we make the list have only the parent
    # as an entry
    for i in range(len(newRules)):
        currentRule = newRules[i]
        currentRule [0] = currentRule[0].rstrip()
        for b in range(1, len(currentRule)):
            index = re.search(r"\d", currentRule[b])
            if index == None:
                currentRule.pop(b)
            else:
                currentRule[b] = currentRule[b][index.start():].rstrip()
    
    return (newRules)

def findDirectChildren(prettyRules, parent = "shiny gold", tally = 1):
    
    ## 1. Find list entry with parent bag info (index)
    ## 2a. extract children from this entry (all list elements after 1st)
    ## 2b. when extracting, split the entry into amount + name
    ## 3. append list of children with new children + tally*previousTally
    
    ## TO BE DONE IN findAllChildren function
    ## 4a. for each child, rerun findChildren and keep track of totalTally
    ## 4b. If findChildren == [], do nothing
    
    startidx = 0
    for r in prettyRules:
        if r[0] == parent:
            startidx = prettyRules.index(r)
    
    directKids = prettyRules[startidx][1:]
    children = []
    for kid in directKids:
        children.append(kid.split(' ', 1))

    for child in children:
        child[0] = int(child[0])*tally

    return children

def findAllChildren(prettyRules):

    children = findDirectChildren(prettyRules, "shiny gold")
    totalTally = 0
    for child in children:
        totalTally += child[0]
        nextChildren = findDirectChildren(prettyRules, child[1], child[0])
        if nextChildren:
            children += nextChildren
            
    return ([children, totalTally])    

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

    rules = prettifyRules(rules)
    children, totalTally = findAllChildren(rules)
    
    print ("Total number of bags inside shiny gold: ", totalTally)

def main(fileName):
    

    rules = extractRules(fileName)
    solvePartA(rules)
    solvePartB(rules)

if __name__ == "__main__":
    import sys
    import numpy as np
    import re

    ## I want to have the option of adding command line option or just run normally
    try:
        fileName = sys.argv[1]
    except IndexError:
        fileName = "data-ec/day7-input.txt" 

    main(fileName)
