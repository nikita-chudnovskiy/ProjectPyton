# a = [3,8,56,9]
# for i in a:
#     print(i*i)

# a = [2,4,6,8,10]
# b = []
# for i in a:
#     if i < 7:
#         b.append(i)
# print(b)

# g = []
# while True:
#     a = input()
#     if a not in g:
#         if a == 'стоп':
#             break
#         g.append(a)
# print(g)

# a = [2,7,4,9]
# print(a[1:])

a = [2,87,81,4,32]
print(a[::-1])
f = [2,32,12,6,5]
for i in f:
    if i in a:
        print(i)