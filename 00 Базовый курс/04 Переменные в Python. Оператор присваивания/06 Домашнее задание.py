import math

# 9 во 2 степени + 6 в 4 степени

print((9 ** 2) + (6 ** 4))
print(pow(6, 4))

# Корень 8 - корень 12
a = math.sqrt(8)
b = math.sqrt(12)
print(a - b)
print(math.sin(45) + math.cos(45))

# Размер туфель
t = int(input('Введите размер скальных туфель'))
print('Размер скальных туфель', t - 2)

# Сумма баллов за 3 теста
test1 = int(input('введите балл '))
test2 = int(input('введите балл '))
test3 = int(input('введите балл '))
itog = test1 + test2 + test3
print('итоговый бал', itog)

# Введите зарплата
salary = int(input('Введите зарплату'))

salary_th = salary // 1000

print('Ваша зарплата %s тысяч рублей.' % (salary_th))

# Сумма перевода с комиссией
sum_perevoda = float(input('Введите сумму перевода с комиссией 5 %'))

sum_perevoda += sum_perevoda / 100 * 5

print(sum_perevoda)

# Конкатенация 5630
per1 = (input())
per2 = (input())
per3 = (input())
per4 = (input())
itog = per1 + per2 + per3 + per4
print(itog)

# След четное
s = int(input())
print(s + 2 - (s % 2))
