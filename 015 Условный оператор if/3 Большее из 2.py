# Вывести самое большое
a = int(input())
b = int(input())

if a > b:
    print(a, 'Первое больше')
else:
    print(b,'Второе больше')

print(max(a,b))