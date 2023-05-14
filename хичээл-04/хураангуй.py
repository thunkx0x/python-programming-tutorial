#!/usr/bin/python3

# Хураангуй

names = ['Evekon', 'David', 'John', 'Alice']

# Jack утгийг List лүү оруулж байна
names.append('Jack')

# Evekon утгийг хэд байгааг тоолж байна
names.count('Evekon')

# David хэд дэхь индекс болохыг олно. Хэрэв элемент байхгүй тохиолдолд -1 ирнэ
names.index('David')

# Hako нэрийг 3 дахь индекс дээр оруулж байна
names.insert(3, 'Hako')

# Эрэмбэлж байна
names.sort()

# List утгуудыг устгаж байна
names.clear()
