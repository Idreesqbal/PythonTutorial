# Modules are functions that are prebuilt by the programmers of python or you can make it
# by your very own.

#import my_module
# The text above shows how to import a module to your code.
# if the module that you have created exist inside your own repository
# then you need to write simply 'Import my_module
# then you can access functions inside the module like this: e.g course = my_module.function(name of the function)
# if the name of the module is too long then you can rename it using 'as' : import my_module as md
# if you wanted a specific function inside your module then state: from my_module import function1
# then you don't need to actually use the my_module.function1().
# if you have more than 1 function to insert from your own module then you need to state like this:
# from my_module import function1, function2
# if you wanted to import everything inside your module then you state like this :
# from my_module import * (star states that we want you import everything from that module)
import sys
print(sys.path)
# importing sys, and then sys.path will tell us where are the python file exist and where it
# will look everytime you want to import something
# let's say that we want to import a module written by other people and copied it in our desktop
# if u want to import that file in the future e.g import file1 it will show you an error as
# it is not where the python will look for it while importing it.
# if you want to add it into your python paths then you state:
sys.path.append('Location of the file')

import os
# this will print the location where the operating system underlines
print(os.__file__)  # this will print the location of all the standard libraries that we are using so far
# it is very interesting to study those standard file libraries since you can learn alot from just looking at those code


