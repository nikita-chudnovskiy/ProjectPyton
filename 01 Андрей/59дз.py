b = 0
f = open('geroynashegovremeni.txt','r',encoding = 'utf-8')
text1 = f.read()
f.close()

# words = text1.split()
# for i in words:
#     if len(i) > 1:
#         b = b+1
# print(b)

# words = text1
# for i in words:
#     if i != ' ':
#         b = b+1
# print(b)

words = text1.split()
g = []
for i in words:
    g.append(len(i))
y = (max(g))
for i in words:
    if len(i) == y:
        print(i)