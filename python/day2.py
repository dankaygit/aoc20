import numpy as np
import pandas as pd

# data = np.genfromtxt( "../data-ec/day2-input.csv", delimiter = ' ', dtype = str, names = ["minmax", "reqlet", "password"])
data = pd.read_csv("../data-ec/day2-input.csv", delimiter = ' ', dtype = str, names = ["minmax", "reqlet", "password"])

data['reqlet'] = data['reqlet'].str.replace(':', "")


# This extracts the min and max values directly into a new 3 column dataframe (middle column is the separator '-')
minimax = pd.DataFrame((data['minmax'].str.partition('-'))[[0,2]].values, columns = ['min', 'max'])
minimax['min'] = minimax['min'].astype(int)
minimax['max'] = minimax['max'].astype(int)

# How do I add (in one step) this to a new 
# data = pd.DataFrame(data, (data['minmax'].str.partition('-'))[[0,2]] )

data2 = (data.join(minimax)).drop(columns = 'minmax')
del minimax

### Tried and failed to define the following two functions such that I can directly pass it to data2.apply()

def isValidOld(row):
    letter, password, minVal, maxVal = row["reqlet"], row["password"], row["min"], row["max"]
    return (password.count(letter) >= minVal) and (password.count(letter) <= maxVal)

def isValidNew(row):
    letter, password, pos1, pos2 = row["reqlet"], row["password"], row["min"]-1, row["max"]-1
    return (password[pos1] == letter ) != (password[pos2] == letter )

oldValids = data2.apply(isValidOld, axis = 1)
result1 = oldValids.sum()
print ('# of valid passwords in part 1: ', result1 )

newValids = data2.apply(isValidNew, axis = 1)
result2 = newValids.sum()
print ('# of valid passwords in part 2: ', result2 )