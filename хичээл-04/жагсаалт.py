#!/usr/bin/python3

# Жагсаалт Massive 

# print('List - ийн тухай')
a = 5
b = 15
c = 51
d = -1234

a = [5, 15, 51, -1234, 13, 'test', 'admin']
print(a)
print(a[2])
print(len(a))
print(a[0])
print(a[6])
print(a[-1])
print(a[-2])
# print(a[10])
print(a[:2])
print(a[:5])
print(a[1:4])
print(a[2:4])
print(a[2:6])
print(a[2:6:2])
print(a[::-1]) # reverse хийх

# a.insert(1, 'yeah2')
# print(a)
# a.insert(7, 'yeah8')
# print(a)
# a.insert(10, 'yeah8')
# print(a)

a = [5, 15, 51, -1234, 13, 'test', 'admin']
print(a.index(51))

a = [5, 15, 51, -1234, 13, 'test', 51, 'admin']
print(a.index(51))

# a = [5, 15, -1234, 13, 'test', 'admin']
# print(a.index(51))

a = [5, 15, -1234, 13, 'test', 'admin']
a.pop()
print(a)

a = [5, 15, -1234, 13, 'test', 'admin']
a.pop()
a.pop()
print(a)

a = [5, 15, -1234, 13, 999, -1]
a.sort()
print(a)

a = [5, 15, -1234, 13, 999, -1]
a.sort(reverse=True)
print(a)

a = [5, 15, -1234, 13, 999, -1]
print(sorted(a))
print(a)
