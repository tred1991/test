# Exercise 1
# 1. добавить аргументы в список
# 2. отсортировать список
# 3. вывести второе по возростанию число в списке
# ощибка инднкса не пойму почему

# def second_number(*numb):
#     a = list(numb)
#     # a.extend(*numb)
#     a.sort(reverse=True)
#     # return a[2]
#     for i in a:
#         i += 1
#         if a[i] < a[0]:
#             c = a[i]
#             return c
#
#
# d = second_number(10, 14, 5, 5, 6, 11, 23, 23)
# print(d)


# Exercise 3
class Person():
    """Main class with mandatory data"""
    def __init__(self, full_name='', age=''):
        """determinate variables for Person class"""
        self.age = age
        self.full_name = full_name
        word = full_name.split()
        if len(word) != 2:
            raise AssertionError('incorect data')
        if int(age) < 1900 or int(age) > 2020:
            raise AssertionError('wrong year')

    def __str__(self):
        """formatting data for print"""
        return "<Person object: {} {}>".format(self.full_name, self.age)

    def name_from_full_name(self):
        """method for select name from full_name argument"""
        return self.full_name[:self.full_name.find(' ')]

    def surname_from_full_name(self):
        """method for select surname from full_name argument"""
        return self.full_name[self.full_name.find(' ')+1:]

    def d_print(self):
        """method for prant results of another methods from class"""
        d = self.name_from_full_name()
        d1 = self.surname_from_full_name()
        print(d, d1, sep='\n')

f = Person(full_name="Peter Petrov", age='1991')
g = f.d_print()


class Employee(Person):
    """Expanded class with new parameters"""

    def __init__(self, full_name='', age='', position='', salary='', expir=''):
        """determinate new variables for Employee class"""
        Person.__init__(self, full_name, age)
        self.position = position
        self.salary = salary
        self.expir = expir
        if int(expir) < 0 or int(salary) < 0:
            raise AssertionError('incorect digital value')

    def __str__(self):
        """formatting data for print"""
        return "<Employee object: {} {} {} {} {}>".format(self.full_name, self.age, self.position, self.salary, self.expir)

    def position_level(self):
        """definition of position level via expiriance"""
        if int(self.expir) < 3:
            pos = "Junior — " + self.position
        elif 3 >= int(self.expir) <= 6:
            pos = "Middle — " + self.position
        else: # int(self.expir) > 6:
            pos = "Senior — "  + self.position
        return pos

    def more_salary(self, add):
        """finding new value for salary via value of add arg"""
        ss = int(add) + int(self.salary)
        return ss

s = Employee(full_name="Peter Petrov", age='1991', position='QA', salary='123', expir='5')
r = print(s.more_salary(add=5), s.position_level())


class ITEmployee(Employee):
    """class with new arg skills"""

    def __init__(self, full_name='', age='', position='', salary='', expir=''):
        """determinate new variables for ITEmployee class"""
        Employee.__init__(self, full_name, age, position, salary, expir)
        self.skills = []

    def __str__(self):
        """formatting data for print"""
        return "<Employee object: {} {} {} {} {} {}>".format(self.full_name, self.age, self.position, self.salary, self.expir, self.skills)


    def add_skill(self, new_skill):
        """add one new skill for employee"""
        self.skills.append(new_skill)
        return self.skills

    def add_skills(self, *new):
        """add list of skills"""
        self.skills.append(new)
        return self.skills

it = ITEmployee(full_name="Peter Petrov", age='1991', position='QA', salary='123', expir='5')
itpr = print(it.add_skill(new_skill="ref"), it.add_skills("rterte", "eretyty"))

class Perimeter():

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        """formatting data for print"""
        return "<Perimeter object: {} {}>".format(self.a, self.b)

    def squre(self):
        S = self.a * self.b
        return S

    def perim(self):
        P = (int(self.a) + int(self.b)) * 2
        return P

res = Perimeter(a=10, b=5)
resprint = print(res.squre(),res.perim())

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """formatting data for print"""
        return "<Perimeter object: {} {}>".format(self.x, self.y)

    def distance_zero_point(self):
        len = ((self.x**2)+(self.y**2))**0.5
        return len

    def distance_between(self, x1, y1):
        lenpoint = ((self.x**2 + x1**2)+(self.y**2 + y1**2))**0.5
        return lenpoint

respoint = Point(x=5,y=8)
resp = print(respoint.distance_zero_point(), respoint.distance_between(x1=10, y1=15))


class Student():

    def __init__(self, full_name='', specialty='', year=2008):
        self.full_name = full_name
        self.specialty = specialty
        self.year = year
        self.marks = []

    def __str__(self):
        """formatting data for print"""
        return "<Student object: {} {} {}>".format(self.full_name, self.specialty, self.year)

    def add_mark(self, rating):
        self.marks.append(rating)
        return self.marks

    def average(self):
        av = sum(self.marks)/len(self.marks)
        return av

    def years(self, current):
        diff = current - self.year
        return diff

resmark = Student(full_name='Ivan Ivanov', specialty='metrology', year=2009)
printmark = print(resmark.add_mark(5), resmark.add_mark(4), resmark.average(), resmark.years(current=2020), sep=' -- ')












