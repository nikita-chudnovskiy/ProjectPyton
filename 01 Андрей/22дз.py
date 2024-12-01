# f = []
# g = []
# for i in range(6):
#     a = int(input())
#     if a == 0:
#         g.append(a)
#     else:
#         f.append(a)
# print(f+g)

a = []
for i in range(6):
    b = int(input())
    a.append(b)
print(*a[::-1])