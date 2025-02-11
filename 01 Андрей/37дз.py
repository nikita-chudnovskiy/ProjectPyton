# b = 0
# bukva = input()
f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if i[-1] == bukva:
#         b = b+1
#         print(b)

# words = text.split()
# for i in words:
#     if i[-1] == i[0]:
#         print(i)

# words = text.split()
# for i in words:
#     if len(i) > 4 and i[-4:] == 'ться':
#         print(i)

# words = text.split()
# for i in words:
#     if len(i) == 7:
#         print(i)

words = text.split()
for i in words:
    if i[0] in 'аоеёюиэуыя':
        print(i)