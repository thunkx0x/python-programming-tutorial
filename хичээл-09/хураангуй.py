#!/usr/bin/python3

# Хураангуй

def sum_of_numbers(*args, **kwargs):
    """Will return sum of numbers"""
    print(kwargs['name'])
    return sum(args)

teacher = {
    'name': 'ErkhemBuyn',
    'more': 'https://github.com/thunkx0x'
}

print(sum_of_numbers(6, 2, 3, 4, 5, **teacher))
