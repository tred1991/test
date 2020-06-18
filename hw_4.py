# Задание 1
# def exept():
#     try:
#         a = input("Write text: ")
#         print(a[2], a[-2], a[0:4], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")
#     except : pass
# Задание 2
a = input("Value 1: ")
b = input("Value 2: ")
if a.isdigit() is not True or b.isdigit() is not True:
    print(a + ' ' + b)
else:
    s = float(a) + float(b)
    print(s)
# Задание 3
def song(row=3, la=3, end=0):
    a = 1
    while a <= row:
        result = "la-"*(la-1) + "la."
        if end != 0:
            result = "la-"*(la-1) + "la!"
        print(result)
        a += 1
    return result
d = song(row=3, la=10, end=1)

# Задание 4
def write_number():
    while True:
        a = input("Write number:")
        if a.isdigit() is True:
            break
    return a

b = write_number()

def write_world():
    while True:
        a = input("Write world:")
        a.find(' ')
        if a.find(' ') == -1:
            break
    return a
b = write_world()

def is_year_leap(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print("true")
    else:
        print("false")
    return year
d = is_year_leap(year=2000)

def triangle(a, b, c):
    if int(c) < (int(a) + int(b)) and int(b) < (int(a) + int(c)) and int(a) < (int(c) + int(b)):
        print("YES")
    else:
        print("NO")
d = triangle(a=5, b=4, c=6)

x1 = float(0.5)
y1 = float(1.5)
x2 = float(2.0)
y2 = float(4.0)
def  distance():
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d
f = distance()
print(f)
