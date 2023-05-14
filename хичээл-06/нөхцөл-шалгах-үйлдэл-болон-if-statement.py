#!/usr/bin/python3

# Нөхцөл шалгах үйлдэл болон if statement

# True False утга True 1 False 0 хоёртын тооллын систем нойл нэг

print(10 > 5)
print(10 < 5)

if True:
    print('True statement')

if False:
    print('True statement')

# 10 < 5
# 10 == 5 False
# 10 > 5  True  
# 10 < 5  False
# 10 != 5 True
# 'abc' == 'abc' True
# 'abc' == 'cbd' False

a = 10
b = 30

if a > b:
    print('A is greater than B')

if a < b:
    print('A is lower than B')

a = 30
b = 10

if a > b:
    print('A is greater than B')
else:
    print('B is greater than A')

a = 5
b = 10

# if a > b:
    #    print('A is greater than B') # энэ код if гэдэг блокон дотор зөвхөн байх ёстой
#    print('A is greater than B')
#    print('A is greater than B')
#    print('A is greater than B')
#    print('A is greater than B')
# a = 30 # аль блокон дотороо кодоо бичэч байгаагаа сайн анхаараарай
# else:
#    print('B is greater than A')

if a > b:
    if a == b:
        print('A is greater than B')
    print('A is greater than B')
    print('A is greater than B')
    print('A is greater than B')
# a = 30 # аль блокон дотороо кодоо бичэч байгаагаа сайн анхаараарай
else:
    print('B is greater than A')

age = 20
university = True

# if age >= 20 and university == True:
if age >= 20 and university:
    print('Age is greater than 20 also in university')
else:
    print('Something is wrong')

age = 20
university = False

if age >= 20 and university:
    print('Age is greater than 20 also in university')
else:
    print('Something is wrong')

if age >= 20 or university:
    print('Age is greater than 20 also in university')
elif age > 18 and university == False:
    print('Age is greater than 18 also not going university')
else:
    print('Something is wrong')

if age >= 20 and university:
    print('Age is greater than 20 also in university')
elif age > 18 and university == False:
    print('Age is greater than 18 also not going university')
else:
    print('Something is wrong')

if age >= 20 and university:
    print('Age is greater than 20 also in university')
elif age > 18 and not university:
    print('Age is greater than 18 also not going university')
else:
    print('Something is wrong')

if age >= 20 and university:
    print('Age is greater than 20 also in university')
elif age > 18 and university:
    print('Age is greater than 18 also not going university')
else:
    print('Something is wrong')
