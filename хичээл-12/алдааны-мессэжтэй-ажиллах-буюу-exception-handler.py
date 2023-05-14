#!/usr/bin/python3

# Алдааны мессэжтэй ажиллах буюу exception handler

# print(1 / 0)

# try:
#     print(1 / 0)
# except Exception as e:
#     print(e)
# else:
#     print('code runs successfully')
# finally:
#     print('exiting...')

# try:
#     print(1 / 0)
# except Exception as e:
#     print('toog 0t huvaaj bolohgui t1ee')
# else:
#     print('code runs successfully')
# finally:
#     print('exiting...')

# try:
#     f = open('found.txt')

# except Exception as e:
#     print(e)

# else:
#     print(f.read())

# finally:
#     print('exiting...')

# try:
#     f = open('not_found.txt')

# except Exception as e:
#     print(e)

# else:
#     print(f.read())

# finally:
#     print('exiting...')

# try:
#     f = open('not_found.txt')

# except Exception as e:
#     print('File oldsongui')

# else:
#     print(f.read())

# finally:
#     print('exiting...')

# try:
#     f = open('found.txt')

# except Exception as e:
#     print('File oldsongui')

# else:
#     print(f.read())
#     # print(f.read(), end='')

# finally:
#     print('exiting...')

# try:
#     print(1 / 0)
#     f = open('not_found.txt')

# except ZeroDivisionError:
#     print('Toog 0t huvaaj bolohgui')

# except FileNotFoundError:
#     print('File oldsongui')

# else:
#     print(f.read())
#     # print(f.read(), end='')
# 
# finally:
#     print('exiting...')

try:
    print(1 / 1)
    f = open('not_found.txt')

except ZeroDivisionError:
    print('Toog 0t huvaaj bolohgui')

except FileNotFoundError:
    print('File oldsongui')

else:
    print(f.read())
    # print(f.read(), end='')

finally:
    print('exiting...')

try:
    print(1 / 1)
    f = open('not_found.txt')

except ZeroDivisionError:
    print('Toog 0t huvaaj bolohgui')

except FileNotFoundError:
    print('File oldsongui')
