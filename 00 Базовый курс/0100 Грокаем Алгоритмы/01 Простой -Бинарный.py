# Логорифм это операция обратная возведению в степень. log 100 = 100**2
                                                       #log 8 = 2**3
import random

# O -большое ОПИСЫВАЕТ СКОРОСТЬ РАБОТЫ АЛГОРИТМА !!!
# O(n)  Предположим список размера n
# (Простой поиск должен проверить каждый элемент поэтому придется выполнить n операций)

# А теперь другой пример для проверки списка размером n бинарному поиску потребуется log n операций
# O(log n ), или логарифмическое время. Пример: бинарный поиск.

# O(n) О-большое n количество операций

# Простой поиск | Бинарный поиск

# 100     100 мс         7 мс
# 10000   10 секунд      14 мс
# 1000000 11 дней        32 mc

def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False
    count =0
    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_item:
            search_res = True
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return search_res


lst = [i for i in range(100000000)]
lst=sorted(lst)

if 9999999 in lst:
    print('Есть')


value =int(input('Введите элемент для поиска'))

result = binary_search(lst, value)
if result:
    print(" В списке Элемент найден!",value )
else:
    print(" В списке Элемент не найден.",value)











