# Знакочередующаяся сумма

n = int(input())
total = 0
for i in range(n + 1):
    if i % 2 == 0:
        total -= i # Остаток от деления 0 то знак -
    else:
        total += i
print(total)
