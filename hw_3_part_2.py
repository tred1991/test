# Задание 4
a = input("Number 1: ")
b = input("Number 2: ")
c = input("Number 3: ")
if int(c) < (int(a)+int(b)) and int(b) < (int(a)+int(c)) and int(a) < (int(c)+int(b)):
    print("YES")
else:
    print("NO")

# Задание 10
a = "We are not what we should be! " \
    "We are not what we need to be. " \
    "But at least we are not what we used to be " \
    "(Football Coach)"

# 10.1
print(a)
count = 0
for i in a.split(' '):
    count += 1
print(count)

# 10.2
for i in a.split(' '):
    if i.find('!') != -1:
        print(i.strip('!'))
    elif i.find('.') != -1:
        print(i.strip('.'))
    elif i.find('(') != -1:
        print(i.strip('('))
    elif i.find(')') != -1:
        print(i.strip(')'))
    else:
        print(i)

# 10.3
l = []
for i in a.split(' '):
    l.append([i])
l.sort()
print(l)

# Задание 9
while True:
    t = input("Enter text without spaces: ")
    t.find(' ')
    if t.find(' ') == -1:
        break

# Задание 8
# 8.1
l = [0, 1, 2, 3, 4, 5, 6]
len = len(l)
while len >= 0:
    len -= 1
    l.pop(0)
    print(l)

# 8.2
l = "123456"
for i in l:
    j = l.index(i)
    print(l[j:])

# 8.3
l = [0, 5, 3, 2, 4, 6]
i = 0
while i < len(l):
    min = l[i]
    if l[i] < min:
        min = l[i]
    l.remove(min)
    print(l)





