n = int(input())                    # Ввод целого числа
total = 0
for i in range(n):                  # Перебор чисел до n
    if i % 3 == 0 or i % 5 == 0:    # Поиск чисел кратных 3 и 5
        total += i                  # Суммирование кратных чисел 3 и 5
print(total)