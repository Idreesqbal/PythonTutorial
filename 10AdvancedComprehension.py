nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 my_list = []
for n in nums:
   my_list.append(n)
   print(my_list)
my_list = [n for n in nums]  # list comprehension is making the job
# so much easier and more readable the creating a for loops for sure.
# first n is actually to say how we want our new list to look like.
# e.g if we want a squared version then:
[x**2 for x in nums]
# Extended example:
 my_list = [x for x in nums if x%2 == 0] #will give u even set of even numbers
# A : Another elegant way is to use maps with 'Lambda''s to the same job
my_list = map(lambda x: x**2, nums)
my_list  = filter(lambda x: x%2 == 0, nums)
print(my_list)
#  example 2
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
# ^ this piece of code will make a combination of abcd with 0123
# but we can do the same thing easily with list comprehension as follow:
my_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]

# Dictionaries Comprehensions

names = ['idrees', 'ahmad', 'ameen']
heroes = ['batman', 'superman', 'spiderman']
my_dic = {}
for name, hero in zip(names, heroes):  # Hard way
    my_dic[name] = hero
print(my_dic)

# We can do the same thing with dictionaries comprehensions as follow:
my_dic = {name: hero for name, hero in zip(names, heroes)}
# you can also make restriction to the dictionary for example:
my_dic = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}

# Set Comprehensions
num = [1,2,3,4,5,6,7,8,9] # set is used to store set of unique numbers or values

my_set = set() #Hard way
for n in num:
    my_set.add(n)
print(my_set)

my_set  = {n for n in nums} # and this is it the easiest way
print(my_set)

my_generator = (n*n for n in nums) # this is the way we use to generators to create the same list




