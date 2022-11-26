from collections import Counter
s='abracadabra'
worlds =['nicky','micky','lucy','lucy','lucy'] # lucy 3 раза
#
# print(Counter(s)) # Похожа на словарь ключи буду буквы а значение сколько раз встречалась
#
print(Counter(worlds))

name =Counter(worlds)

print(name['lucy']) # обращение по ключу lucy

