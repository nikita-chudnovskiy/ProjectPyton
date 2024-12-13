# 10.5 = 1 год
n: float = float(input())
if n > 2:
    age = 21 + (n - 2) * 4
    print(int(age))
elif n <= 2:
    print(n * 10.5)
