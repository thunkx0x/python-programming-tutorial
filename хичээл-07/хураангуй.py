#!/usr/bin/python3

# Хураангуй 

# Dictionary үүсгэж байна
student = {
    'name': 'ErkhemBuyn',
    'age': 17,
    'courses': [
        'C',
        'Java',
        'Python'
    ],
    2: 'test'
}

# Нэрийг хэвлэж байна
print(student['name'])

# Бүх 'key' ийг хэвлэж байна
print(student.keys())

# Бүх түлхүүрийн утгийг хэвлэж байна
print(student.values())
# Түлхүүр болон утгийг хэвлэж байна
print(student.items())

# Шинэ түлхүүр нэмж байна
student['address'] = 'Selenge'
