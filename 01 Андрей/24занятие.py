# g = []
# for i in range(4):
#     a = int(input())
#     g.append(a)
# f = sorted(g)
# print(f[2])

# f = []
# while True:
#     a = input()
#     f.append(a)
#     if a == 'stop':
#         break
# while True:
#     g = input()
#     if g in f:
#         print(f.index(g))
#     if g not in f:
#         f.append(g)

# d = []
# for a in range(1,1000+1):
#     d.append(a)
# print(d)

# d = []
# for i in range(6):
#     a = int(input())
#     d.append(a)
# print(sum(d))
# print(max(d))

f = []
for i in range(3):
    a = int(input())
    f.append(a)
print(f[::-1])