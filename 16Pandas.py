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
print(ser1['USA'])  # you always pass the index "Labels"

# If you wanted to add two series, this example would look like this:
# ser1 + ser2  # the result of this addition will be shown as float number since panda's are precise.

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])  #
print(df)  # This will print a 5 by 4 data visualization of your screen.
#  There is 2 way to get any column in the table.
print(df['W'])  # First way
print(df.W)  # Second way
print(df[['W', 'Z']])  # this is the way if you wanted to print more than 1 column
df['new'] = df['W'] + df['Y']  # This is the way if you wanted to create more column from
#  From the already existed columns
print(df)
df.drop('new', axis=1, inplace=True)  # axis is very important in this scenario, if you put the axis equale to 0,
# then it will refer to the rows, if you put it equale to 1 then it will refer to the columns.
# for example if you want to delete a row then you say: df.drop('A', axis = 0)
# One thing to note is that if u wanted to drop to acually take place for real then you should
# specify inplace=True, becuase by defualt is it false, and the reason is you not to lose data.

# There is 2 way to select rowns in panda's

print(df.loc['C'])  # the first way !

print(df.iloc[2])  # The second way !

print(df.loc['B', 'Y'])  # This is they way to select a row and the column of your choice

print(df.loc[['A', 'B'], ['W', 'Y']])
print(df[df > 0])  # This is the way to get conditional selection from the tables basically
# shows which values from the table is actually bigger than the zero 0 .
print(df['W'] > 0)  # This is the way to get columns which are bigger than the zero 0.
print(df[df['W'] > 0])  # This will print out everything in the "W" column which is bigger than 0
print(df[df['Z'] < 0])  # This is second example.

print(df[df["W"] < 0][['X']])  # This will print the X column of the df table
# where the conditional selection is as follow: 'W' < 0

print(df[(df['W'] > 0)&(df['Y'] > 1)])  # this is a way to pass on multiple condition.
#  people often write 'and' but that will throw an error.
print(df[(df['W'] > 0)|(df['Y'] > 1)])  # this a way to actually do the 'OR' conditional selection.
# people make the same mistake as they make with and conditional selection so be careful to not to make the same
# mistake.

print(df.reset_index())  # This wil replace the index of labels with numerical numbers.
# Which means instead of lables we will have numerical index starting from [0,1,2,3...]
print(df.reset_index('States', inplace=False))  # The result of the operation is temporary if you want to
# make it permanent then go on and make the "inplace" equal to True, by default it is 'False'
newind = 'CA NY WY OR CO'.split()
df['States'] = newind  # This is a method to create a new column and saving it into the table
print(df)
df.set_index('States', inplace= False)  # This is method to actually selecting a column as new
# index columns, by default it won't take place automatically, you need to mention is explicitly
# by writing 'inplace = True' and then it will be permanently
# print(df.set_index('labels', inplace=True))  # this is a way to return back

