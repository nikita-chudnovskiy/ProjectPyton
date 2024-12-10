# a = []
# for i in range(5):
#     b = int(input())
#     a.append(b)
# for i in a:
#     if i >6:
#         print(i)

# b = []
# f = []
# for i in range(4):
#     a = int(input())
#     b.append(a)
# for i in b:
#     if i >10 and i <20:
#         f.append(b)
# print('Элементов в f:',len(f))

# g = [1, 3, 5, 8, 9]
# print(g[::-1])

# d = []
# while True:
#     a = input()
#     d.append(a)
#     if a == 'break':
#         break
# print(d)

# d = []
# while True:
#     a = input()
#     d.append(a)
#     if a == 'break':
#         break
# print('Введите слово:')
# x = input()
# if x in d:
#     print('Есть')
# if x not in d:
#     print('Нет')

b = ['Яблоко', 'машина']
a = input()
if a == b[0] or a == b[1]:
    print('Есть')
else:
    print('Нет')
