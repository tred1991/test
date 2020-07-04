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
    def __init__(self, full_name='', age=''):
        self.age = age
        self.full_name = full_name

    def name_from_full_name(self):
        return self.full_name[:self.full_name.find(' ')]

    def surname_from_full_name(self):
        return self.full_name[self.full_name.find(' ')+1:]

    def d_print(self):
        d = self.name_from_full_name()
        d1 = self.surname_from_full_name()
        print(d, d1, sep='\n')

f = Person(full_name="Peter Petrov")
g = f.d_print()



