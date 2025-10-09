# import os
# f = os.listdir('.')
# for i in f:
#     if os.path.isfile(i):
#         f = open(i,encoding='utf-8')
#         l = f.read()
#         print(i,len(l))

# import os
# d = 0
# t = os.listdir('.')
# for k in t:
#     if k[-3:] == '.py':
#         d = d+1
# print(d)

import os
f = input()
g = input()
if os.path.exists(f) and os.path.isfile(f):
        f = open(f,encoding="utf-8")
        text = f.read()
        f.close()
        r = 0
        for i in text:
            if i == g:
                r = r+1
        print(r)
