# First topic of the day: Classes and variable in OOP
class employee():
    pass


emp_1 = employee()
emp_2 = employee()
emp_1.name = 'idrees'
emp_1.age = 34
emp1.email = 'Idreesqbal@gmail.com'


# in this example you see that if i need to create information about any of the employees
# then i need to this everyone manually which is extreamly time consuming

class Employee2():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.' + last + '@company.com'


#  Topic 2nd, Class Variables
# we have 2 types of variables in general, class variable and instance variable
# class variable is created when you want it to be applied for every instances of that class
# instance variable is created when you would mutate it in the future.

class Emplyoee3():
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Here you see that we set the raise amount
        # to self because we know that class variable which is now set to 1.04 won't be the same
        # forever, if we ever need to change it we could just do like this:
        emp1.raise_amount = 2.04  # this will apply the raise amount change just for the emp_1 .
        # if there exist another employees this change won't be applied to them

# 3rd Topic of today: Class method and staticMethod
    # Class methods are used to minupulate the class data it self.
    # e.g.
    @classmethod
    def from_string(cls, emp_str):
        first, last, age = emp_str.split('-')
        return cls(first, last, age)
    # ^ what is this code doing you might ask? imagine that you have a list of employees information
    # and you wanted to take them all in, but they are all formatted as CSV file ...
    # if u do them all manually then it costs a lots of time which we don't want.
    # instead we can use the class method to do this job automatically so we don't have to do it.
    # in that example above from_string method take emp_str as input, and then it splits them as
    # first, last, pay just like a normal input of the class.

    # Example1: new_emp_1 = Emplyoee3.from_string('john-doe-25')
    @classmethod
    def from_today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)
    @staticmethod # Static method is used as normal function that hasn't anything to do with the instance or the class

    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    #Example:
    my_date = datetime.date(2016, 7, 11)
    print(Employee3.is_workday(my_date))

    def __add_(self, other): # this will able this class to be able to add two payment of employees
        return self.pay + other.pay


# Property decorator : it allows us to define a method but we can access it like attribute.
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)



