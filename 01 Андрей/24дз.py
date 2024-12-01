
# a = [1,2,3,4,5,6,7]
# print('Введите shift')
# b = int(input())
# for i in range(b):
#     last = [a[6]]
#     right = a[:5+1]
#     a = last+right
# print(a)

b = []
for i in range(6):
    a = int(input())
    b.append(a)
maxb = max(b)
mind = min(b)
f = []
for a in b:
    if a == maxb:
        f.append(mind)
    if a == mind:
        f.append(maxb)
    if a != maxb and a != mind:
        f.append(a)
print(f)
