a,b =map(int,input().split())
y =a*b
while b > 0:
    a, b = b, a % b
    c = y / a
print('НОД:', a)
print('НОК' ,c)     # Наименьшееобщее краное