# import random
# t = []
# for i in range(10):
#     r = random.randint(1,100)
#     t.append(r)
# print(t)

# f = int(input())
# for idx in range(0,10):
#     if t[idx] == f:
#         print(idx)

# f = int(input())
# for idx in range(0,10):
#     if t[idx] < f:
#         print(idx)

# for idx in range(0,10):
#     print(t[idx])

# for i in t:
#     print(i)

# names = []
# scores = []
# for i in range(4):
#     y= input()
#     b = int(input())
#     names.append(y)
#     scores.append(b)
# for idx in range(0,4):
#     if scores[idx] == 5:
#         print(names[idx])

file = open('geroynashegovremeni.txt',encoding = 'utf-8')
text = file.read()
j = file.close()

# lens = []
# words = text.split()
# for i in words:
#     lens.append(len(i))
# for idx in range(0,len(lens)):
#     if lens[idx] == 10:
#         print(words[idx])

words = text.split()
for i in words:
    if i[0] == i[-1] and len(i) > 2:
        print(i)