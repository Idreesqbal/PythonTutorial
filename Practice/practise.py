class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, fname):
        first, last = fname.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

class Devs(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class Manager(Employee):
    def __init__(self, first, last, pay, mng=None):
        super().__init__(first, last, pay)
        if mng is None:
            self.mng = []
        else:
            self.mng = mng

    def add_emp(self, emp):
        if emp not in self.mng:
            self.mng.append(emp)

    def remove_emp(self, emp):
        if emp in self.mng:
            self.mng.remove(emp)
