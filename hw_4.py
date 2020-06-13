# try:
#     a = input("Write text: ")
#     print(a[2], a[-2], a[0:4], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")
# except : pass

# Задание 2
a = input("Value 1: ")
b = input("Value 2: ")
if a.isdigit() is not True or b.isdigit() is not True:
    print(a + ' ' + b)
else:
    s = float(a) + float(b)
    print(s)
