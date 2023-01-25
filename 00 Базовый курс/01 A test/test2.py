"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def ne_chet(in_num):
    if(in_num % 2) == 1:
        return True
    else:
        return False

# # Применение filter() для удаления нечетных чисел
out_filter = list(filter(ne_chet,numbers))

print(out_filter)
