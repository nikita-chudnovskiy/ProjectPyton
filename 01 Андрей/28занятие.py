# a = []
# while True:
#     b = int(input())
#     a.append(b)
#     if b == 0:
#         break
# print(sum(a))
# print(a[::-1])

# a = []
# g = []
# for i in range(4):
#     b = int(input())
#     a.append(b)
# for i in a:
#     if i < 10:
#         g.append(i)
#     if i > 10:
#         pass
# print(g)

# a = []
# for i in range(5):
#     h = int(input())
#     a.append(h)
# f = sorted(a)
# print(f)
# print(f[3])

# a = [2,10,5,4,3]
# b = []
# for i in a:
#     b.append(i*2)
# print(b)

# a = [1,3,5,7,9,10]
# b = []
# c = []
# for i in a:
#     if i <5:
#         b.append(i)
#     if i > 5:
#         c.append(i)
# print(b,c)

# a = [1,2,3,4,5]
# s = []
# for i in a:
#     if i < 4:
#         s.append(i)
# print(s)

b = [1,3,4,2]
d = [5,10,20,6]
f = b+d
print(sorted(f))