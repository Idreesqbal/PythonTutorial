# List is used to store iterable ordered sequence of datatype inside []
course = ['History', 'Math', 'Physics', 'CompSci']  # Example of a list
print(len(course))  # len is used to print length of iterable elements inside a list
print(course[2])  # List's elements can accessed by indexing starting from zero 0; this will print 3rd el inside the
# list
print(course[2:5])  # It will print the elements ranging from element 2nd until exclusive element 5th.
# for more info read 02AdvanceTextSlicing.py
course.append('Arts')  # Append function is used to add a iterable element to the end of a list like : string,
# list or tuple
# Example: course.append(['Criminology', 'Aerospace']) will result in creating list inside the list
# Example: course.append('Arts') will result in adding 'Arts' to the end of the list
course.insert(0, 'Chemistry')  # Insert function take 2 arguments, 1st: index 2nd: element
# and it is used to insert element in a specific index;
# in this example "Chemistry" will be inserted into 0 (first) element of our list.
course2 = ['Anatomy', 'Physiology']
course.extend(course2)  # Extend function is used to extend the list unlike 'append' method.
# Example: in above procedure, course 2 elements will be added to course element
# without creating a list inside a list
course.remove('Math')  # Removing elements by Value.
course.pop()  # By default it will remove the last element of a list
# you can also give it an index Example: course.pop(2) will remove 3rd el.
course.reverse()  # Results in permanent reversing the list.
course.sort()  # Results in permanent sorted list. By default it sorts in Ascending order.
course.sort(reverse=True)  # Results in permanent sorted list but in reverse order.
sorted_list = sorted(course)  # Results in temporary sorted version of the list without output.
# which u can access by creating a variable.

num1 = [1, 2, 3, 4, 5, 6, 7]
min(num1)  # Returns the minimum value in the list.
max(num1)  # Returns the maximum value in the list.
sum(num1)  # Returns the sum of operable values in list.
print(course.index('Math'))  # Index function will return the positional index of the value.
print('Arts' in course)  # 'in' function is used to check if a value exists inside a list.

for index, course in enumerate(course, start=1):  # Enumerate function is used to index a list elements accordingly.
    print(index, course)  # using unpacking technique, we can customise our enumerate outputs.

course_str = ', '.join(course)  # Join function is used to convert a list into string
# using ',' as delimiter.

new_list = course_str.split(' - ')  # is used to convert a string into list, using '-' as delimiter.

# TUPLES ARE IMMUTABLE, MEANS YOU CAN'T CHANGE ANY BROUGHT CHANGE.
# TUPLES are used to store unordered iterable elements inside () unlike list with []


# Sets are values that are unique or have no duplicate stored inside {}.
# Example: cs_course = {'History', 'Math', 'Physic'}
# It is used to remove duplicates.
cs_course = {'History', 'Math', 'Physics', 'CompSci'}
art_course = {'History', 'Math', 'Art', 'Design'}
print(cs_course.intersection(art_course))  # Intersection function will return the common element
# Between these two sets.
print(cs_course.difference(art_course))  # Difference function will return which elements
# are in cs_course and not in art_course.
print(cs_course.union(art_course))  # Union function will return the union of both sets.


