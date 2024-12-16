a = int(input())
a1 = a // 100
a2 = a % 100 // 10
a3 = a % 10

n1 = max(a1, a2, a3)
n2 = min(a1, a2, a3)
sr = (a1 + a2 + a3) - max(a1, a2, a3) - min(a1, a2, a3)
if n1 - n2 == sr:
    print('Число интересное')
else:
    print('Число не интересное')
