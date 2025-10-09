import random
# g = []
# for i in range(10):
#     b = random.randint(1, 100)
#     g.append(b)
# print(g)
# print(max(g))
# f = sorted(g)
# print(f[-2])

g = ['как дела?','как ты?','как жизнь','как поживаешь?','как вы?']
h = ['здравствуй','привет','здравствуйте','здарово','добрый день']
a = random.randint(0, 4)
d = random.randint(0, 4)
print(h[a],end=', ')
print(g[d])