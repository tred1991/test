from hw_4 import song
# songf = open('text.txt', 'w')
# f.write(song(5,5,1))
# f.close()
#
# f = open('text.txt', 'r')
# f.read()
# print(f)
# f.close()
# for i in f:
#     f.write(index + '\n')
# f = open('text.txt', 'r')

# f = open('text1.txt', 'x')
# f.write(song(5,5,1))
# f.close()
#
# f = open('text.txt')
# for line in f:
#     print(line)
# f.close()

import urllib.request
response = urllib.request.urlopen('https://www.google.com.ua/?hl=ru')
print(response.read())
b'{\n  "args": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.5"\n  }, \n  "origin": "95.56.82.136", \n  "url": "https://httpbin.org/get"\n}\n'