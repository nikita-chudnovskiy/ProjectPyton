# for i in range(0,11):
#     print(i)

# g = []
# for i in range(0,101):
#     g.append(i)
# print(sum(g))

# j = 0
# for i in range(4):
#     f = int(input())
#     if f == 10:
#         j = j+1
# print(j)

# x = [5,82,9,14,29,57,4]
# k = int(input())
# for idx in range(0,7):
#     if x[idx] == k:
#         print(x[idx+1])

# import os
# files = os.listdir()
# for i in files:
#     if os.path.isfile(i):
#
#         f = open(i,encoding='utf-8')
#         text = f.read()
#         f.close()
#         print(i,':',len(text))

# import os
# files = os.listdir()
# d = input()
# for i in files:
#     if os.path.isfile(i):
#         f = open(i,encoding='utf-8')
#         text = f.read()
#         f.close()
#         if d in text:
#             print(i)

# import os
# d = os.listdir()
# for i in d:
#     if i[-4:] == '.txt':
#         print(i)