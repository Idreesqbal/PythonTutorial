student = {'Name': 'john', 'age': 25, 'course': ['Math', 'CompSci']}  # Dictionaries are used to store key value data
# inside {}
print(student['Name'])  # This will search for the value Name and returns the result
print(student.get('Name'))  # Get function will do the same job.
print(student.get('Name', 'Not Found')) # get function take 2nd custom argument incase it doesn't
# find a value for 'Name

student['phone'] = 555-55-555-55  # it will check if the 'Phone' Exists inside the students then it will update 'phone'
# if not it will add 'phone' value at the end of our dictionary with its value

student.update({'Name': 'jane'})  # Update function will the same job as the example ^
del student['age']  # Removes the 'age'
age = student.pop('age')  # Second method to remove elements from our dic and maybe assign it to a variable

print(len(student))  # len function return the length of the dic.
print(student.values())  # Values function will return the values of our dic.
print(student.keys())  # Keys function will return the keys of our dic.
print(student.items())  # Will basically return everything inside our dic.
# By default python loops through the keys.
# using items() method will make sure that python loops through keys and value.
for key, value in student.items():  # Using unpacking we can print keys and values.
    print(key, value)
