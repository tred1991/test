# Задание 1
a = input("Write text: ")
print(a[2], a[-2], a[0:4], a[:-2], a[::2], a[1::2], a[::-1],a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")

# Задание 2
a = input("Write text: ")
if len(a)%2 == 0:
  print(a[len(a)//2:], a[0:len(a)//2])
else:
  print(a[len(a)//2+1:], a[0:len(a)//2+1])

# Задание 3
a = input("Write year: ")
b = int(a)
if (b%4 == 0 and b%100 != 0) or b%400 == 0:
  print("YES")
else:
  print("NO")

# Задание 4
a = input("Number 1: ")
b = input("Number 2: ")
c = input("Number 3: ")
if int(c)==(int(a)**2+int(b)**2)**0.5 or int(b)==(int(a)**2+int(c)**2)**0.5 or int(a)==(int(c)**2+int(b)**2)**0.5:
 print("YES")
else:
  print("NO")

# Задание 5
a = input("Number 1: ")
b = input("Number 2: ")
c = input("Number 3: ")
if int(a)>int(b) and int(a)<int(c):
  a, b = b, a
elif a>b and a>c and b<c:
  a, b, c = b, c, a
elif a>b and a>c and b>c:
  a, b, c = c, b, a
elif b>a and b>c and a>c:
  a, b, c = c, a, b
elif b>a and b>c and a<c:
  a, b, c = a, c, b
print(a, b, c)

# Задание 6
a = input("Number 1: ")
b = input("Number 2: ")
c = input("Number 3: ")
if int(a)==int(b)==int(c):
  print("3")
elif a==b or a==c or b==c:
  print("2")
else:
  print("0")

# Задание 7
i=0
while i<=10:
  print(i)
  i=i+1

i=20
while i>=1:
  print(i, end=" ")
  i=i-1

i = input("Writenamber: ")
b = int(i)+1
s=0
while b>0:
  b=b-1
  if b%2 != 1:
    b=b/2
    s=s+1
print(s)

# Задание 8
l = [0,1,2,3,4,5,6]
for i in l:
  print(i)
  l.remove(i)

l = input("Write text: ")
s=[]
for i in l:
  print(i)
  s = l[i:]
  print(s)






