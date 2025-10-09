# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i)

# b = 0
# g = input()
# for i in g:
#     b = b+1
# print(b)

# k = 0
# n = input()
# for i in n.split():
#     k = k+1
# print(k)

# y = []
# while True:
#     s = int(input())
#     if s == 0:
#         break
#     if s not in y:
#         y.append(s)
#     if s in y:
#         pass
# print(y)

# g = 0
# import random
# while True:
#     w = random.randint(0,100)
#     g = g+1
#     if w == 5:
#         break
# print(g)


def count(g,b):
    l = 0
    for i in g:
        if i == b:

            l = l+1
    return(l)
# b = count('Привет, как дела?','е')
# print(b)

f = open('geroynashegovremeni.txt',encoding='utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if i[-3:] == 'тся':
#         print(i)

words = text.split()
for i in words:
        e = count(i,'а')
        if e == 2:
            print(i)
