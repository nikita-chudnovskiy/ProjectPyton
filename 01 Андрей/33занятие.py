# a = []
# while True:
#     b = int(input())
#     a.append(b)
#     if b == 2025:
#         break
# print(min(a))

# s = 0
# a = 'Люблю кушать арбузы'
# print(a[6:12])
# for i in a:
#     if i == 'у':
#         s = s+1
# print(s)

# a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# b = input()
# g = a.index(b)
# print(g)

# d = 0
# a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# b = input()
# for i in b:
#     if i == 'а':
#         d = d+1
# print(d)

a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
b = input()
for i in b:
    if i in a:
        h = a.index(i)
        h = h+1
        print(a[h],end = '')
    if i not in a:
        print(i,end = '')