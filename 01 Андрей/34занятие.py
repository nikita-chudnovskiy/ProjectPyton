# b = []
# for i in range(5):
#     a = int(input())
#     b.append(a)
# if 11 in b:
#     print('Да')
# if 11 not in b:
#     print('Нет')

d = 0
f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()
# print(text[0:201])
# print(len(text))

# for i in text:
#     if i == 'а':
#         d = d+1
# print(d)

words = text.split()
for t in words:
    if t[0] == 'ф':
        print(t)

# lens = []
# words = text.split()
# for g in words:
#     lens.append(len(g))
# print(max(lens))

# words = text.split()
# for rg in words:
#     if len(rg) == 23:
#         print(rg)