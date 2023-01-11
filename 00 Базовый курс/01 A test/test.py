year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = int(input())
if 1 <= num <= 12:
    print(year[num - 1])
else:
    print('Введите число от 1 до 12')