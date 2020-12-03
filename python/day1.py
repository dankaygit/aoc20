import numpy as np
# import pandas as pd

targetYear = 2020

data = np.genfromtxt( "./data-ec/day1-input.csv", delimiter = '/n', dtype = int)
small_nums = np.array([num for num in data if num <= targetYear/2])
large_nums = np.array([num for num in data if num > targetYear/2])

# for (small, big) in np.outer(small_nums, large_nums):

sums = []
summands = np.array([0,0])
for s in small_nums:
    for l in large_nums:
        summands = np.array([s,l])
        if (s+l == targetYear):
            print ("summands are: ", s, l)
            print ("product is: ", s * l)


sum = 0 

for s1 in data:
    for s2 in data:
        for s3 in data:
            sum = s1 + s2 + s3
            if sum == targetYear:
                print ("summands: ", s1, s2, s3)
                print ("product: ", s1 * s2 * s3)
                break


        



