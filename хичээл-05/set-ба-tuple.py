#!/usr/bin/python3

# Set ба tuple хэрхэн ажиллах талаар

tutorials = ['C', 'C++', 'Java', 'Python']
print(tutorials)

tutorials = ['C', 'C++', 'Java', 'Python']
print(type(tutorials))

tutorials = ['C', 'C++', 'Java', 'Python']       # Энэ бол list дөрвөлжин хаалт ашиглана
print(dir(tutorials))

tutorials = ('C', 'C++', 'Java', 'Python')       # Энэ бол tuple дугуй хаалт ашиглана
print(tutorials)
print(type(tutorials))
# tutorials[0] = 'Php'
print(dir(tutorials))

tutorials = ('C', 'C++', 'Java', 'Python')       # Энэ бол tuple
tutorials.count('C')                             # 'C' гэх утга хэд байгааг тоолж байна 
tutorials.index('C++')                           # 'C++' хэд дэхь индекс болохыг олж байна

# nums_a = {1, 2, 3, 4, 5, 2, 3} # Set үүсгэж байна хэрвээ давхардсан элемент байвал оруулахгүй
# print(nums_a)
# input()
# nums_a = {1, 2, 3, 4, 5}       # Set үүсгэж байна хэрвээ давхардсан элемент байвал
# print(nums_a)
# print(dir(nums_a))
# input()
# nums_b = {4, 5, 6, 7, 8}       # оруулахгүй
# nums_a.intersection(nums_b) эсвэл print(nums_a & nums_b) ашиглаарай

nums_a = {1, 2, 3, 4, 5}         # Set үүсгэж байна хэрвээ давхардсан элемент байвал
nums_b = {4, 5, 6, 7, 8}         # оруулахгүй

print(nums_a | nums_b)           # Нэгдлийг хэвлэнэ 'Union'
print(nums_a & nums_b)           # Огтлолцлыг хэвлэнэ 'intersection'
print(nums_a - nums_b)           # nums_b байгаа элементүүдийг nums_a ээс хасна
print(nums_b - nums_a)           # nums_a байгаа элементүүдийг nums_b ээс хасна
print(nums_a ^ nums_b)           # Union - Intersection буюу нэгдлээс огтлолцлыг хасна
