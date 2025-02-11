f = open('pd.txt','r',encoding = 'utf-8')
text1 = f.read()
f.close()

# words = text1.split()
# for i in words:
#     if i.count('а') == 2 and i[0] == 'в':
#         print(i)

# b = []
# for i in range(6):
#     a = int(input())
#     b.append(a)
# g = []
# for a in b:
#     if a < 10:
#         g.append(a)
# print(g)

# for i in range(150,201):
#     print(i)

# a = int(input())
# for i in range(1,a+1):
#     print(i)

# h = []
# while True:
#     a = input()
#     h.append(a)
#     if a == 'stop':
#         break
# print(h[1])

# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i, end=' ')

# words = text1.split()
# for i in words:
#     if len(i) >=3 and i[2] == 'к':
#         print(i)

# words = text1.split()
# for i in words:
#     if len(i) == 5 and i.count('я') >=1:
#         print(i)

words = text1.split()
for i in words:
    if len(i) >=2 and i[::-1] == i:
        print(i)