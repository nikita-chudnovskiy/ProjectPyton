# import os
# n = os.listdir()
# for i in n:
#     if os.path.isfile(i):
#         f = open(i,encoding='utf-8')
#         text = f.read()
#         f.close()
#         if len(text) > 500:
#             print(i,len(text))

# names = []
# lens = []
# import os
# j = os.listdir()
# for d in j:
#     if os.path.isfile(d):
#         f = open(d,encoding='utf-8')
#         text = f.read()
#         f.close()
#         names.append(d)
#         lens.append(len(text))
# m1 = min(lens)
# for i in names:
#     f = open(i,encoding='utf-8')
#     text1 = f.read()
#     f.close()
#     if  len(text1) == m1:
#         print(i)

import os
t = input()
if os.path.exists(t) and os.path.isfile(t):
    t_copy = input()
    f = open(t,encoding='utf-8')
    text = f.read()
    f.close()
    f1 = open(t_copy,'w',encoding='utf-8')
    f1.write(text)
    f1.close()
    print("Файл успешно скопирован")
else:
    print('Такого файла не существует')