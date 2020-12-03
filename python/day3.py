import numpy as np

forest = np.genfromtxt("../data-ec/day3-input.txt", dtype = str, comments = None)

def countTrees(forest, slope = [1, 1]):

    pos = 0
    height = 0
    trees = 0

    while (height < forest.size - 1):
        pos = (pos + slope[0]) % 31
        height += slope[1]

        if (height > forest.size - 1 ):
            break

        if (forest[height][pos] == '#'):
            trees += 1

    return (trees)

slopes = np.array([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])

trees = [countTrees(forest, slope) for slope in slopes]
trees = np.array(trees)

# trees = np.array([countTrees(forest, slope) for slope in slopes])

print ("For slopes :", slopes)
print ("Number of trees: ", trees)
print ("Product of trees: ", trees.prod())

