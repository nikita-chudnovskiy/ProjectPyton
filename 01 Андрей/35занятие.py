f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if len(i) == 3:
#         print(i)

# words = text.split()
# for i in words:
#     if i[-1] == 'ь':
#         print(i)

# words = text.split()
# for i in words:
#     if 'ъ' in i:
#         print(i)

# o = []
# words = text.split()
# for i in text:
#     if i not in o:
#         o.append(i)
# print(o)

# words = text.split()
# for i in words:
#     if len(i) > 1 and i[1] == 'а':
#         print(i)

# words = text.split()
# for i in words:
#     if len(i) > 2 and i[2] == 'с':
#         print(i)

a = 'йцукенгшщзхъфывапролджэячсмитьбюё'
counts = []
for i in range(33):
    counts.append(0)
print(counts)
for i in text:
    if i in a:
        b = a.index(i)
        counts[b]= counts[b]+1
print(counts)