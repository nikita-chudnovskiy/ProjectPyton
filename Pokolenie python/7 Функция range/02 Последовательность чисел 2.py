m = int(input())
n = int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)

elif m > n:
    for i in range(m + 1, n, -1):
        print(i - 1)

else:
    print(n)