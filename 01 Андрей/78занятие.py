# j = int(input())
# l = int(input())
# n = int(input())
# if j >= l and j >= n:
#     print(j)
# elif l >= j and l >= n:
#     print(l)
# elif n >= l and n  >= j:
#     print(n)

# d = int(input())
# a = int(input())
# b = int(input())
# if d == a and d == b:
#     print(3)
# elif d != a and d != b and a != b:
#     print(0)
# else:
#     print(2)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == a2 and b1 == b2:
    print('NO')
elif a1 == a2 or b1 == b2:
    print('YES')
elif a1 != a2 and b1 != b2:
    print('NO')