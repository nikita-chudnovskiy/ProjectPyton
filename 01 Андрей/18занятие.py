# a = [1, 2, 3, 4, 5, 'cat']
# print(*a)
# a.append('Andrey')
# print(*a)
# print(a[5])
# a[2]=2024
# print(*a)
# print(a[1:5])

# sss = [16, 9, 1, 18, 34, 0, 5, 27, 33, 100, 4]
# print(sss[:])
#
# print(len(sss))

# a = []
# for i in range(5):
#     b = input()
#     a.append(b)
# print(a)

a = []
while True:
    s = int(input())
    a.append(s)
    if s == 0:
        break
print(sum(a))
print(max(a))
print(min(a))