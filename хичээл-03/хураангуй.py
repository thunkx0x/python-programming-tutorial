#!/usr/bin/python3

# Хураангуй

tutorial = 'Python programming tutorial'

# Тэмдэгт мөрийг том болгож байна
print(tutorial.upper())
# Тэмдэгт мөрийг жижиг болгож байна
print(tutorial.lower())

# 'Programming' үгийг тоолж байна
print(tutorial.count('programming'))

# 'Python' үгийг 'Java' аар сольж байна
print(tutorial.replace('Python', 'Java'))

# 'Python' үгийн index ийг хайж байна
print(tutorial.index('Python'))

name = 'ErkhemBuyn'
age = 17
utube = 'Evekon'

print(f'{name} is {age} old.')
