# Задача №2951. Стоимость покупки
# Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
#
# Входные данные
# Программа получает на вход три числа: a,-rub b - kop, n- n-пирожков.
#
# Выходные данные
# Программа должна вывести два числа: стоимость покупки в рублях и копейках.
#
# Примеры
# входные данные
# 10
# 15
# 2
# выходные данные
# 20 30
# входные данные
# 2
# 50
# 4
# выходные данные
# 10 0
a,b,n = map(int,input().split())
print(a*n + b*n//100, b*n%100, sep=',')