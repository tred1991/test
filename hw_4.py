# Задание 1
# def exept():
#     try:
#         a = input("Write text: ")
#         print(a[2], a[-2], a[0:4], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")
#     except : pass
# Задание 2
# a = input("Value 1: ")
# b = input("Value 2: ")
# if a.isdigit() is not True or b.isdigit() is not True:
#     print(a + ' ' + b)
# else:
#     s = float(a) + float(b)
#     print(s)
# # Задание 3 кажется некрасивое решение
# def song(row=3, la=3, end=0):
#     result = ("la-"*(la-1) + "la.\n")*row
#     if end != 0:
#         result = ("la-"*(la-1) + "la!\n")*row
#     return result
# d = song(row=3, la=10, end=1)
# print(d)
#
# # Задание 4
# def write_number():
#     while True:
#         a = input("Write number:")
#         if a.isdigit() is True:
#             break
#     return a
#
# b = write_number()
#
# def write_world():
#     while True:
#         a = input("Write world:")
#         a.find(' ')
#         if a.find(' ') == -1:
#             break
#     return a
# b = write_world()
#
# def is_year_leap(year):
#     if (year%4 == 0 and year%100 != 0) or year%400 == 0:
#         a = True
#     else:
#         a = False
#     return a
# d = is_year_leap(year=2000)
# print(d)
# print(type(d))
#
# def triangle(a, b, c):
#     if int(c) < (int(a) + int(b)) and int(b) < (int(a) + int(c)) and int(a) < (int(c) + int(b)):
#         g = True
#     else:
#         g = False
#     return g
# d = triangle(a=5, b=4, c=6)
# print(d)
# print(type(d))

def  distance(x1,x2,y1,y2):
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d
f = distance(0.5,1.5,2.7,9.6)
print(f)

# Задание 5
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

words = []
def match_ends(words):
    i = 0
    for item in words:
        if len(item) >= 2 and item[0] == item[-1]:
            i += 1
    return i

res = match_ends(['qq', 'fdgds', 'r', 'ertyuue', '1234561'])
print(res)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

# l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# l1 = []
# l2 = []
# def front_x(words):
#     if words[0] == 'x':
#         l1.append(words)
#         sorted(l1)
#     else:
#         l2.append(words)
#         sorted(l2)
#     l3 = l1 + l2
#     return words
#
# l4 = sorted(l1, key=front_x)
# l5 = sorted(l2, key=front_x)
# l6 = sorted(l, key=front_x)
# print(l6, l1, l2, sep='\n')

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use sorted() function and a custom key= function to extract the last element form each tuple.

l = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
def sort_last(tuples):
    return tuples[-1]
l1 = sorted(l, key=sort_last)
print(l1)