#!/usr/bin/python3

# Хураангуй 

# Жишээ - 1
nums = [1, 2, 3, 4, 5, 6, 7]
# 'nums' list-ийн дагуу гүйж байна
for i in nums:
    # Хэрвээ i == 3 байвал програм 3 ийн тоог хэвлэхгүй дараагийн давталт луу орно
    if i == 3:
        continue
    # Хэрвээ i == 5 байвал давталт маань break хийж давталтаас гарна
    elif i == 5:
        break
    print(i)

# Жишээ - 2
# 0 - 100 хүртэл бүх тэгш тоог хэвлэж байна
for i in range(0, 100, 2):
    print(i)

# Жишээ - 3
f = 52
i = 1
# Давталт эхэлж байна, нөхцөл нь 'f' != 'i' буюу энэ хоёр ялгаатай байх л юм бол үргэлжлээд байна
while i != f:
    print(i)
    i += 1
