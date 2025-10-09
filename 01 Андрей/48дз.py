d = 0
f = open('kd.txt','r',encoding = 'utf-8')
text = f.read()
f.close()

# words = text.split()
# for i in words:
#     if i[-2:] == 'то':
#         print(i)

# words = text.split()
# for i in words:
#     b = 0
#     for g in i:
#         if g == 'а':
#             b = b+1
#     if b == 3:
#         print(i)
#
# words = text.split()
# for i in words:
#     print(i[0],end='')