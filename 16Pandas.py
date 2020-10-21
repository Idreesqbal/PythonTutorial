import numpy as np
import pandas as pd
from numpy.random import randn

lables = ['a', 'b', 'c']
my_date = [10, 20, 30]
arr = np.array(my_date)
d = {'a': 10, 'b': 20, 'c': 30}
print(pd.Series(data=my_date))  # This will print up a indexed version of the date.
print(pd.Series(my_date, lables))
print(pd.Series(d))
# These is big difference between numpy and panda's, panda's can hole verity of object as data.
# for example:
print(pd.Series([sum, print, len]))
print(pd.Series(lables))  # so you can see that the panda's are accepting variety of object as data.

ser1 = pd.Series([1, 2, 3], ['USA', 'Germany', 'USSR'])
print(ser1)
# when you want to access the data between a series, you can do like list.
# for example:
print(ser1['USA']) # you always pass the index "Labels"

# If you wanted to add two series, this example would look like this:
# ser1 + ser2  # the result of this addition will be shown as float number since panda's are precise.

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])#
print(df )