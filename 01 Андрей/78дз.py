a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 == a1-1 and b2 == b1+1:
    print('YES')
elif a2 == a1+1 and b2 == b1+1:
    print('YES')
elif a2 == a1 and b2 == b1+1:
    print('YES')
elif a2 == a1-1 and b2 == b1:
    print('YES')
elif a2 == a1+1 and b2 == b1:
    print('YES')
elif a2 == a1 and b2 == b1-1:
    print('YES')
elif a2 == a1-1 and b2 == b1-1:
    print('YES')
elif a2 == a1+1 and b2 == b1-1:
    print('YES')
else:
    print('NO')