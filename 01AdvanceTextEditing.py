pi = 3.14159265
import datetime

tag = 'h1'
text = 'This is headline'
person = {'name': 'idrees', 'age': 28}
l = ['jane', 23]
sentence = '<{0}>{1}<{0}>'.format(tag, text)
sentence1 = 'My name is {0[name]} and i am {1[age]} years old'.format(person, person)  # Using Dictionary
sentence4 = 'My name is {name} and i am {age} years of old.'.format(**person)  # Using kwargs
sentence2 = 'My name is {0[0]} and i am {0[1]} years of old.'.format(l)  # Using list
sentence6 = 'pi is equal to {:.3f}'.format(pi)  # specifying the amount of number after decimals.
sentence7 = '1 MB is equal to {:,} bytes'.format(1000 ** 2)  # helpful for number separating value
sentence8 = '1 MB is equal to {:,.2f} bytes'.format(5000 ** 2)  # adding 2 zero after number


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', 24)
for i in range(1, 11):  # specifying the amount of zero before the actual number
    sentence5 = 'The value is {:03}'.format(i)
    print(sentence5)
sentence3 = 'My name is {0.name} and i am {0.age} years old.'.format(p1)
sentence9 = datetime.datetime(2020, 10, 16, 10, 11, 34)
sentence10 = '{:%B %d %Y}'.format(sentence9)
sentence11 = '{0:%B %d %Y} fell on {0:%A} and was the {0:%j} day of the year'.format(sentence9)
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)
print(sentence6)
print(sentence7)
print(sentence8)
print(sentence9)
print(sentence10)
print(sentence11)
