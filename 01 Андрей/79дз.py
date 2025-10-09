g1 = int(input())
h1 = int(input())
g2 = int(input())
h2 = int(input())
if g2 == g1-1 and h2 == h1+1:
    print('YES')
elif g2 == g1+1 and h2 == h1+1:
    print('YES')
elif g2 == g1-1 and h2 == h1-1:
    print('YES')
elif g2 == g1+1 and h2 == h1-1:
    print('YES')
else:
    print('NO')