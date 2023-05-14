#!/usr/bin/python3

# for, while давталт

numbers = [2, 4, 6, 8, 10]

for num in numbers:
    print(num)

for num in numbers:
    print(num + 10)

for num in numbers:
    print(num * 2)

for num in range(100):
    print(num)

numbers = range(5)
print(numbers)

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        break
    print(num)

for num in nums:
    if num == 3:
        continue
    print(num)

for num in range(10):
    print(num)

for num in range(5, 10):
    print(num)

for num in range(5, 10, 2):
    print(num)

nums = [1, 2, 3]

for num in nums:
    for char in 'abc':
        print(num ,char)

for num in nums:
    for char in 'abc':
        for char in 'abc':
            for char in 'abc':
                for char in 'abc':
                    print(num, char)

num = 10
i = 0

while i < num:
    print(i)
    i += 1
