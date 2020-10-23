import numpy as np
import pandas as pd
import random

from numpy.random.mtrand import randn

outside = ['g1', 'g1', 'g1', 'g2', 'g2', 'g2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])   # this is how you make multilevel
# indexing or better known as hierarchy indexing

print(hier_index)
print(df)

print(df.loc['g1'].loc[1])  # This is the way to get the data from inside

##############GROUPING
data = {
    'Company': ['Google', 'Google', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charles', 'Amy', 'Viennese', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}
da = pd.DataFrame(data)  # This will create a dataframe
print(da)
grouping = da.groupby('Company')  # This will group the table by Company
print(grouping.sum())  # you should assign a variable to your da.group()
# bcoz this will not printout anything it will store the result in the memory
# after assigning, the variable be accesable to another option and blocks
# Sum will will printout the sum result of the table based on company grouping.
print(grouping.mean())  # this will printout the average base on the company
print(grouping.sum())  # this will printout the sum based of the grouping company
print(grouping.std())  # will printout the standard deviation of the grouping
print(grouping.sum().loc['FB'])  # this will also printout the result of summing
# but it will also the get your the specific 'FB' row
print(grouping.count())  # this will printout the result of counting the unique elements
# residing inside the table
print(grouping.max())  # will printout the highest value based on grouping
print(grouping.min())  # will printout the lowest value based on grouping
print(grouping.describe())  # this printout every possible outcome
print(grouping.describe().transpose()) # printsout v2 of description
 #### Merging
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']}, index=[8, 9, 10, 11])

