# # Задание 4
# a = input("Number 1: ")
# b = input("Number 2: ")
# c = input("Number 3: ")
# if int(c) < (int(a)+int(b)) and int(b) < (int(a)+int(c)) and int(a) < (int(c)+int(b)):
#     print("YES")
# else:
#     print("NO")

# Задание 10
a = "We are not what we should be! " \
    "We are not what we need to be. " \
    "But at least we are not what we used to be " \
    "(Football Coach)"
print(a)
count = 0
for i in a.split(' '):
    count += 1
print(count)

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




