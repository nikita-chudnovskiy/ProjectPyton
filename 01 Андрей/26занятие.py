# b = []
# g = 0
# for i in range(4):
#     a = input()
#     b.append(a)
# for i in b:
#     if 'cat' in i:
#         g = g + 1
# print('обнаружено раз:',g)

# g = []
# f = []
# while True:
#     a = int(input())
#     f.append(a)
#     if a == 0:
#         break
# for i in f:
#     if i < 10 and i != 0:
#         g.append(i)
# print(g)

# f = 90
# while True:
#     print(f)
#     f = f+1
#     if f == 101:
#         break

# a = 100
# while True:
#     print(a)
#     a = a-1
#     if a == 89:
#         break

login = input()
password = input()
if login == 'andrey1':
    if password == 'andrey2':
        print('Доступ разрешён')
if login != 'andrey1' or password != 'andrey2':
        print('Доступ запрещён')