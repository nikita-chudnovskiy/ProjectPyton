# t = input()
# for i in t:
#     if i in ('1234567890'):
#         print(i,end=' ')

# j = [1,6,34,9,8]
# h = int(input())
# m = []
# for i in j:
#     if i > h:
#         m.append(i)
# print(m)

# def get_index(r,k):
#     if k not in r:
#         return(-1)
#     if k in r:
#          for idx in range(0,len(r)):
#              if r[idx] == k:
#                  return(idx)
# p = get_index([6,53,7,25,10],25)
# print(p)

# import random
# w = 0
# q = 0
# y = []
# for i in range(8):
#     l = random.randint(0,10)
#     y.append(l)
# print(y)
# for u in y:
#     if u > 5:
#         w = w+1
#     if u < 5:
#         q = q+1
# print(w,q)

import random
y = []
for i in range(8):
    l = random.randint(0,10)
    y.append(l)
# print(y[-3:])
# print(y[::-1])
print(y)
for idx in range(2,8):
    if y[idx] > y[idx-2]:
        print(y[idx])
