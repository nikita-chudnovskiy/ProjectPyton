import fastapi


n = int(input())
x1 = 1
x2 = 1
for i in range(n):
    print(x1, end=" ")
    x1, x2 = x2, x2 + x1
