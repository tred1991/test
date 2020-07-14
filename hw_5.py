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

    def __init__(self, full_name='', age='', position='', salary='', expir='', skills=''):
        """determinate new variables for ITEmployee class"""
        Employee.__init__(self, full_name, age, position, salary, expir)
        self.skills = []

    def __str__(self):
        """formatting data for print"""
        return "<Employee object: {} {} {} {} {} {}>".format(self.full_name, self.age, self.position, self.salary, self.expir, self.skills)


    def add_skill(self, new_skill):
        """add one new skill for employee"""
        self.skills.append(new_skill)

    def add_skills(self, *new):
        """add list of skills"""
        if new:
            self.skills.append(new)

it = ITEmployee(full_name="Peter Petrov", age='1991', position='QA', salary='123', expir='5', skills=['volly'])
itpr = print(it.add_skill(new_skill="ref"), it.add_skills("rterte","eretyty"))







