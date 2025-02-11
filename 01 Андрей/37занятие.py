# b = 0
# bukva = input()
# f = open('kd.txt','r',encoding = 'utf-8')
# text = f.read()
# f.close()

# words = text.split()
# for i in words:
#     if len(i) == 7:
#         print(i)
#
# words = text.split()
# for i in words:
#     if i[0] in 'аоеёюиэуыя':
#         print(i)

# words = text.split()
# for i in words:
#     b = 0
#     for d in i:
#         if d == 'а':
#             b = b+1
#     if 3 == b:
#         print(i)

# words = text.split()
# for i in words:
#     b = 0
#     for d in i:
#         if d in 'аёеюиуыяэоАОЮЭЯЁЕУЫИ':
#             b = b+1
#     if b == 0:
#         print(i)

f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()

f = open('pd.txt','r',encoding = 'utf-8')
text1 = f.read()
f.close()

b = 0
words = text.split()
for i in words:
    if i in text and i in text1:
        b = b+1
print(b)