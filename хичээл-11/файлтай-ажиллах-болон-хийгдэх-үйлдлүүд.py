#!/usr/bin/python3

# Файлтай ажиллах болон хийгдэх үйлдлүүд

# open('lorem.txt')
# open('lorem.txt', 'r')
# open('lorem.txt', 'w')
# open('lorem.txt', 'rw')
# open('lorem.txt' ,'rb')
# open('lorem.txt', 'wb')

f = open('lorem.txt', 'r')

# print(dir(f))
# print(f.name)
print(f.read()) 

f = open('lorem.txt', 'r').read()

print(f)

f = open('lorem.txt', 'r')

print(f)

f = open('lorem.txt', 'r')

print(f.read())

f.close() # файлаа заавал хаах ёстой. учир нь python гэлтгүй бүх програмчлалын хэл дээр яаж байгаа вэ гэхлээр энэхүү open('lorem.txt', 'r') файлыг нээх үед манай RAM дээр ерөнхийдөө object хадгалж байгаа гэсэн үг. f.close() функц кодыг бичихгүй RAM-д хаа гэж хэлэхгүй бол RAM маань тэрхүү файлын object-ийг хадгалаадал байна гэсэн үг. Програм маань ажиллах тоолонд object-ийг хадгаласаар манай RAM ерөнхийдөө мэдэгдэхүйц дүүрч эхлээд компьютер маань гацаж эхлэх болно.

f = open('lorem.txt', 'r')

print(f.readlines())

f.close()

f = open('lorem.txt', 'r')

for line in f.readlines():
    print(f'Line: {line}')

f.close()

f = open('lorem.txt', 'r')

for line in f.readlines():
    print(f'Line: {line}', end='')

f.close()

f = open('lorem.txt', 'r')

for line in f.readlines():
    print(f'Line: {line}', end='END')

f.close()

f = open('lorem.txt', 'r')

for line in f.readlines():
    line = line.strip()
    print(f'Line: {line}')

f.close()

# f = open('lorem.txt', 'r')

# f.close()

with open('lorem.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        print(f'Line: {line}') # заавал f.close() ийг дуудах шаардлагагүй. энэхүү блокны төгсгөлд ерөнхийдөө ийм байгаа f.close()

with open('lorem.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        print(f'Line: {line}')

# print(f.read()) # уншиж болохгүй яагаад гэвэл файлаа хаацан болохоор f.close() энийг хийцэн болохоор дахиж хийх боломжгүй.

with open('lorem.txt', 'r') as f:
    content = f.read()

print(content)

# with open('example.txt', 'w') as f:
#     f.write('Test output')

# with open('example.txt', 'w') as f:
#     print(dir(f))

with open('example.txt', 'w') as f:
    print(f.writelines('test output'))

with open('example.txt', 'w') as f:
    f.writelines('test output')

with open('example.txt', 'w') as f:
    for i in range(10):
        f.write(f'Line {i}: some text')

with open('example.txt', 'w') as f:
    for i in range(10):
        f.write(f'Line {i}: some text\n')
