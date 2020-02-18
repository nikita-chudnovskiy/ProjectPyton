a1, a2, a3, a4 = map(int, input().split())
b1, b2, b3, b4 = map(int, input().split())

if a1+a2+a3+a4 > b1+b2+b3+b4:
    print(1)
else:
    if a1+a2+a3+a4 < b1+b2+b3+b4:
        print(2)
    else:
        print('DRAW')
