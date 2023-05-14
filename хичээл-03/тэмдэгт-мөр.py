#!/usr/bin/python3

# Тэмдэгт мөр

# print('Сайн уу? Ертөнц!')
a = 'Сайн уу? Ертөнц!'
print(a)

a = 'Сайн уу? Ертөнц! ' + 'Гарагууд минь.'
print(a)

# a = 'Сайн уу? Ертөнц! ' + 123
# print(a)

a = 'Сайн уу? Ертөнц!'
b = 'Гарагууд минь.'
print(a + b)

# a = 'Сайн уу? Ертөнц!'
# b = 'Гарагууд минь.'
# print(a - b)

# Индекс 01234567...
a = 'Сайн уу? Ертөнц!'
print(a[2])

a = 'Сайн уу? Ертөнц!'
print(a[0])

a = 'Сайн уу? Ертөнц!'
print(a[0:4])

a = 'Сайн уу? Ертөнц!'
print(a[:4])

a = 'Сайн уу? Ертөнц!'
print(a[1:4])

a = 'Сайн уу? Ертөнц!'
print(a[9:])

a = 'Сайн уу? Ертөнц!'
print(a[9:-1])

print('Сайн уу? Ертөнц!'.upper())
print('Сайн уу? Ертөнц!'.lower())

tutorial = "Python programming language"

print(tutorial.upper())
print(tutorial.lower())
print(tutorial.count('programming'))
print(tutorial.replace('Python', 'Java'))
print(tutorial.index('language'))

# tutorial = "Java programming anyway"

# print(tutorial.upper())
# print(tutorial.lower())
# print(tutorial.count('programming'))
# print(tutorial.replace('Java', 'Python'))
# print(tutorial.index('language'))

name     = 'Evekon'
age      = 17
gender   = 'Male'

# print(name + age + gender)
print(name + gender)
print(f'{name} is {age} old.')
print('{} is {} old.'.format(name, age))
print(name + str(age) + gender)
print("Name: "+name)
print("Name:",name)
print("Name: "+name+"")
