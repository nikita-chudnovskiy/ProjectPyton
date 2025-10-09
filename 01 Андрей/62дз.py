# d = 0
# f = open('kd.txt','r',encoding = 'utf-8')
# text = f.read()
# f.close()

# words = text.split()
# for i in words:
#     if i[-1] == i[0]:
#         d = d+1
# print(d)

# d = []
# a = []
# for i in range(6):
#     g = int(input())
#     if g < 5:
#         a.append(g)
#     if g > 5:
#         d.append(g)
# print(d,a,sum(d),sum(a))

f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()

words = text.split()
for j in words:
    if j[::-1] == j and len(j) > 2:
        print(j)