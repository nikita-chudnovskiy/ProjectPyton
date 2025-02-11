# a = [4,8,2,15,13,25]
# print(a[-2:])

# a = input()
# if 'снег' in a:
#     print('Есть')
# if 'снег' not in a:
#     print('Нет')

# shotchik = 0
# a = input()
# b = input()
# words1 = a.split()
# words2 = b.split()
# for i in words1:
#     if i in words1 and i in words2:
#         shotchik = shotchik+1
# print(shotchik)

# d = 'Привет Андрей'
# for i in d:
#     print(i)

# s = 0
# a = input()
# for i in a:
#     if i == 'а':
#         s = s+1
#     if i != 'а':
#         pass
# print(s)

c = 0
a = input()
b = [',','.','?','!']
for i in a:
    if i in b:
        c = c+1
print(c)