import random
a = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
# for i in range(100):
#     print(random.choice(a),end='')

# b = input()
# if b[-1] == 'ь':
#     print(b[-2])
# else:
#     print(b[-1])

# f = 'меч'
# f2 = sorted(f)
# print(f2)

# dor = input()
# d = list(dor)
# random.shuffle(d)
# for i in d:
#     if i != ' ':
#         print(i,end='')

f = open('kd (1).txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if len(i) > 2 and i[0:2] == 'но':
#         print(i)

# words = text.split()
# for i in words:
#     if i[0] == i[-1] and len(i) > 2:
#         print(i)

# words = text.split()
# for i in words:
#     if 'ф' in i:
#         print(i)

# words = text.split()
# for i in words:
#     if len(i) > 15:
#         print(i)

# words = text.split()
# for i in words:
#     if i == i[::-1] and len(i) > 3:
#         print(i)

# words = text.split()
# for i in words:
#     b = 0
#     for g in i:
#         if g == 'а':
#             b = b+1
#     if b == 2:
#         print(i)

words = text.split()
for i in words:
    b = 0
    d = 0
    for s in i:
        if s == 'а':
            b = b+1
        if s == 'о':
            d = d+1
    if b == 1 and d == 1:
        print(i)