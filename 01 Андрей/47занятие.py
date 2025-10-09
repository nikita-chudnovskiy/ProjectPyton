# b = []
# for i in range(5):
#     import random
#     a = random.randint(1, 200)
#     b.append(a)
# print(b)
# c = int(input())
# for i in b:
#     if i < c:
#         print(i)

fg = open('kd.txt',encoding='utf-8')
text = fg.read()
fg.close()

words = text.split()
# for i in words:
#     if i[0] == i[-1] and len(i) > 3:
#         print(i)

# for i in words:
#     if i[-3:] == 'тся':
#         print(i)

# for i in words:
#     if len(i) >3 and i[:3] == 'при':
#         print(i)

# for i in words:
#     if i[:3] == 'при' and i[-3:] == 'тся':
#         print(i)

# for i in words:
#     if len(i) > 12:
#         print(i)

for i in words:
     b=0
     for g in i:
         if g == 'о':
             b = b+1
     if b == 2:
         print(i)