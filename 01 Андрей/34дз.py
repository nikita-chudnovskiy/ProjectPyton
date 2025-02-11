d = 0
f = open('kd (1).txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# a = input()
# for i in text:
#     if i == a:
#         d = d+1
# print(d)

# a = input()
# words = text.split()
# for b in words:
#     if b == a:
#         d = d+1
# print(d)

# f = []
# for i in text:
#     if i not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
#         d = d+1
# print(d)
# s = d/len(text)*100
# print(s)

# words = text.split()
# for i in words:
#     if i[::-1] == i:
#         print(i)

# print(text[0:501])
# for i in text:
#     if i not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- ':
#         text = text.replace(i,'')
# print(len(text))
#
# words = text.split()
# for i in words:
#     if len(i) == 15:
#         print(i)