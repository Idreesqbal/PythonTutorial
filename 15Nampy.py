import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mt = np.array(my_mat)
print(mt)
np.arange(0, 10)  # It will create an array of numbers inside a list starting from
# zero until 9 not including 10
print(np.zeros(3))  # it will create a 1dimensional array of 0's ([0,0,0])
print(np.zeros((5, 5)))  # this will create a 5rows by 5columns array of elements. all zero elements
np.ones(4)
np.ones((4, 4))
print(np.linspace(0, 5, 10))  # will create a 1D vectors consisting of equally 100 number between 0 and 5
print(np.eye(4))  # will create a linear identity matrix.
print(np.random.rand(4))  # is used to print 4 numbers from 1-0 inside a list
print(np.random.randn(4))  # is used to print 4 number randing from +0 to -0 in a dimension list.
print(np.random.randint(1, 100, 10))  # this will make a list 10 random numbers from 1 - 100.
arr = np.arange(25)
print(arr.reshape(5, 5))  # while choosing the reshape, make sure to have an equal size like 5by5
print(arr.argmax())  # this will return the index position of the highest value
print(arr.argmin())  # this will return the index location of the lowest value
print(arr.shape)  # this will return the shape of an array!
#  Just like list, you can create an array of elements using nampy,
# list and numpy array are the same in terms of slicing and indexing of array for example:
print(arr[12])  # just like the list, we can index the elements of an array using indexing method
# if we wanted to slice a portion of an array then we can do it just like list, for example:
print(arr[:3])  # this will print the elements from 0 to element number 3.

# NOTES~
# you might be thinking then what is the difference between a list and an array of elements ?
# the difference is in the CASTING. you can cast a value to the elements of the an array for example
arr[:4] = 5  # this is called casting, where we declared that the elements staring from 0 until 4,
# will get the value of 5.
# One important thing to note is that it will chance the value of arr permanently so be careful.
### If you wanted to get a copy of an array first then make a change into it then you should
# specifically specify that you want to do that. for exmple:
arr_copy = arr.copy()
print(arr_copy)
bool_ary = arr_copy < 4
print(arr_copy[arr_copy < 3])

## Numpy operations
print(np.linspace(0.01, 1, 100).reshape(10, 10))
