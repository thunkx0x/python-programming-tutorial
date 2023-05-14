#!/usr/bin/python3

# Функц

def print_name():
    print('Сайн уу?, Эрхэмбуян!')

print(print_name())
print_name()

print('Сайн уу?, Эрхэмээ!')
print('Сайн уу?, Эрхэмээ!')
print('Сайн уу?, Эрхэмээ!')
print('Сайн уу?, Эрхэмээ!')
print('Сайн уу?, Эрхэмээ!')

def print_name():
    print('Сайн уу?, Эрхэмээ :)')

print_name()
print_name()
print_name()
print_name()

def print_name():
    """ Just printing name """
    print('Сайн уу?, Эрхэмбуян!')

print(print_name.__doc__)

def sum_of_numbers(a, b, c):
    return a + b + c

print(sum_of_numbers(1, 2, 3))

def sum_of_numbers(a, b, c=0):
    return a + b + c

print(sum_of_numbers(1, 2))

def sum_of_numbers(a, b, c):
    return a + b + c

print(sum_of_numbers(a=5, b=6, c=1))
print(sum_of_numbers(b=6, a=5, c=1))

# def sum_of_numbers(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
#    return a + b + c

# print(sum_of_numbers(1, 2))

def sum_of_numbers(*args):
    print(args)
    print(sum(args))

sum_of_numbers(1, 2, 141, 123, 1234)

def sum_of_numbers(*numbers):
    print(numbers)
    print(sum(numbers))

sum_of_numbers(1, 2, 141, 123, 1234)

def sum_of_numbers(*numbers, **kwargs):
    print(sum(numbers))
    print(kwargs)

dictionary = {
    'key': 'value',
    'number': 100
}

sum_of_numbers(1, 2, 141, 123, 1234, **dictionary)

def sum_of_numbers(*numbers, **kwargs):
    print(sum(numbers))
    print(kwargs['key'])

dictionary = {
    'key': 'value',
    'number': 100
}

sum_of_numbers(1, 2, 141, 123, 1234, **dictionary)

def sum_of_numbers(*numbers, **kwargs):
    print(sum(numbers))
    print(kwargs['number'])

dictionary = {
    'key': 'value',
    'number': 100
}

sum_of_numbers(1, 2, 141, 123, 1234, **dictionary)
