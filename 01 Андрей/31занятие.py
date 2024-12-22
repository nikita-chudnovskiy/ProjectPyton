# a = [2,7,6,2,7,9]
# b = []
# for i in a:
#     if i in b:
#         pass
#     if i not in b:
#         b.append(i)
# print(b)

# s = []
# for i in range(3):
#     a = int(input())
#     s.append(a)
# f = sorted(s)
# print(f[1])

# e = []
# b = []
# for i in range(5):
#     s = int(input())
#     e.append(s)
# for i in e:
#     if i <15:
#         b.append(i)
# print(b)

# a = 'картошка'
# print(a[3:])
# for i in a:
#     print(i)

# g = 0
# a = input()
# for i in a:
#     if i == 'б':
#         g = g+1
# print(g)

# a = input()
# b = a.split()
# print(len(b))

bedwords = ['идиот','тупой','слаб']
a = input()
f = a.split()
for i in f:
    if i in bedwords:
        print('***', end = ' ')
    if i not in bedwords:
        print(i, end = ' ')