# g = []
# for i in range(5):
#     a = int(input())
#     g.append(a)
# f = sum(g)
# h = f/len(g)
# print(h)

# f = []
# b = 0
# import random
# for i in range(100):
#     a = random.randint(1,50)
#     f.append(a)
# print(f)
# for i in f:
#     if i == 1:
#         b = b+1
# print(b)

d = 0
f = open('kd (1).txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if len(i) > 1 and i[0] == 'т':
#         print(i)

# words = text.split()
# for i in words:
#     if i[-1] == 'ы':
#         print(i)

# words = text.split()
# for i in words:
#     if len(i) >2 and i[2] == 'а':
#         print(i)

# lens = []
# words = text.split()
# for i in words:
#     lens.append(len(i))
# maxlen = max(lens)
# for i in words:
#     if len(i) == maxlen:
#         print(i)

uwords = []
words = text.split()
for i in words:
    if i not in uwords:
        uwords.append(i)
print(uwords)
