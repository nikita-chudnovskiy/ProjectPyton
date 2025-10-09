# o = []
# for i in range(5):
#     l = int(input())
#     o.append(l)
# for idx in range(1,4):
#     if o[idx] > o[idx-1] and o[idx] > o[idx+1]:
#         print(o[idx])

# b = []
# for i in range(6):
#     k = int(input())
#     b.append(k)
# for idx in range(0,6):
#     if b[idx] == 0:
#         print(b[idx-1])

a = []
for i in range(5):
    t = int(input())
    a.append(t)
for idx in range(1,5):
    if a[idx] > a[idx-1]:
        print('+')
    else:
        print('-')